from flask import Flask, render_template, request, send_file, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image
import os
import io
import zipfile
from pathlib import Path
import uuid

# Version
VERSION = "v0.1"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'

# Create necessary folders
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_png_to_jpg(image_file, max_width, max_height, quality=90, dpi=(300, 300)):
    """Convert PNG to JPG with resizing"""
    try:
        # Open and convert to RGB
        img = Image.open(image_file).convert("RGB")
        
        # Get original dimensions
        original_width, original_height = img.size
        
        # Calculate new size maintaining aspect ratio
        ratio = min(max_width / original_width, max_height / original_height)
        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)
        
        # Resize the image
        img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Save to bytes
        output = io.BytesIO()
        img.save(
            output,
            "JPEG",
            quality=quality,
            dpi=dpi,
            optimize=True
        )
        output.seek(0)
        
        return {
            'success': True,
            'image': output,
            'original_size': f"{original_width}x{original_height}",
            'new_size': f"{new_width}x{new_height}",
            'filename': Path(image_file.filename).stem + '.jpg'
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

@app.route('/')
def index():
    return render_template('index.html', version=VERSION)

@app.route('/convert', methods=['POST'])
def convert():
    if 'files' not in request.files:
        flash('No files selected / 파일이 선택되지 않았습니다', 'error')
        return redirect(url_for('index'))
    
    files = request.files.getlist('files')
    if not files or files[0].filename == '':
        flash('No files selected / 파일이 선택되지 않았습니다', 'error')
        return redirect(url_for('index'))
    
    # Get resolution from form
    resolution = request.form.get('resolution', '6000x6000').strip()
    try:
        if 'x' in resolution.lower():
            parts = resolution.lower().split('x')
            max_width = int(parts[0].strip())
            max_height = int(parts[1].strip())
        else:
            size = int(resolution)
            max_width = size
            max_height = size
    except ValueError:
        max_width = 4000
        max_height = 4000
    
    # Get quality
    quality = int(request.form.get('quality', 90))
    
    converted_files = []
    errors = []
    
    for file in files:
        if file and allowed_file(file.filename):
            result = convert_png_to_jpg(file, max_width, max_height, quality)
            if result['success']:
                converted_files.append({
                    'filename': result['filename'],
                    'image': result['image'],
                    'original_size': result['original_size'],
                    'new_size': result['new_size']
                })
            else:
                errors.append(f"{file.filename}: {result['error']}")
        else:
            errors.append(f"{file.filename}: Invalid file type / 잘못된 파일 형식")
    
    if not converted_files:
        flash('No files were converted / 변환된 파일이 없습니다', 'error')
        if errors:
            flash('Errors: ' + ', '.join(errors), 'error')
        return redirect(url_for('index'))
    
    # If single file, send it directly
    if len(converted_files) == 1:
        file_data = converted_files[0]
        return send_file(
            file_data['image'],
            mimetype='image/jpeg',
            as_attachment=True,
            download_name=file_data['filename']
        )
    
    # Multiple files - create ZIP
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file_data in converted_files:
            zip_file.writestr(file_data['filename'], file_data['image'].read())
    
    zip_buffer.seek(0)
    return send_file(
        zip_buffer,
        mimetype='application/zip',
        as_attachment=True,
        download_name='converted_images.zip'
    )

@app.route('/api/convert', methods=['POST'])
def api_convert():
    """API endpoint for programmatic access"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if not file or file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only PNG files allowed.'}), 400
    
    # Get parameters
    resolution = request.form.get('resolution', '4000x4000').strip()
    try:
        if 'x' in resolution.lower():
            parts = resolution.lower().split('x')
            max_width = int(parts[0].strip())
            max_height = int(parts[1].strip())
        else:
            size = int(resolution)
            max_width = size
            max_height = size
    except ValueError:
        max_width = 4000
        max_height = 4000
    
    quality = int(request.form.get('quality', 90))
    
    result = convert_png_to_jpg(file, max_width, max_height, quality)
    
    if result['success']:
        return send_file(
            result['image'],
            mimetype='image/jpeg',
            as_attachment=True,
            download_name=result['filename']
        )
    else:
        return jsonify({'error': result['error']}), 500

if __name__ == '__main__':
    # For development
    app.run(debug=True, host='0.0.0.0', port=5000)
    # For production, use: gunicorn -w 4 -b 0.0.0.0:5000 app:app

