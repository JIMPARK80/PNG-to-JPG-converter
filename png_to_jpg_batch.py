from pathlib import Path
from PIL import Image

# Version
VERSION = "v0.1"

# 1. Set input / output folders
input_dir = Path("input")
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# 2. Get target size from user input / 사용자로부터 해상도 입력받기
print(f"=== PNG to JPG Batch Converter {VERSION} ===")
print("해상도를 입력하세요 (예: 6000x6000 또는 4000x4000)")
print("Enter resolution (e.g., 6000x6000 or 4000x4000)")
print("엔터만 누르면 기본값 4000x4000을 사용합니다 / Press Enter for default 4000x4000")
print()

user_input = input("해상도 입력 / Resolution: ").strip()

# Parse user input / 사용자 입력 파싱
if user_input:
    try:
        if 'x' in user_input.lower():
            parts = user_input.lower().split('x')
            max_width = int(parts[0].strip())
            max_height = int(parts[1].strip())
        else:
            # Single number means square / 단일 숫자는 정사각형
            size = int(user_input)
            max_width = size
            max_height = size
        print(f"설정된 해상도 / Resolution set: {max_width}x{max_height}px\n")
    except ValueError:
        print("잘못된 입력입니다. 기본값 4000x4000을 사용합니다.")
        print("Invalid input. Using default 4000x4000.\n")
        max_width = 4000
        max_height = 4000
else:
    # Default values / 기본값
    max_width = 4000
    max_height = 4000
    print(f"기본 해상도 사용 / Using default resolution: {max_width}x{max_height}px\n")

target_dpi = (300, 300)   # DPI 설정

# 3. Loop through all PNG files
for png_path in input_dir.glob("*.png"):
    # Open and convert to RGB (JPEG does not support transparency)
    img = Image.open(png_path).convert("RGB")
    
    # Get original dimensions / 원본 크기 확인
    original_width, original_height = img.size
    print(f"원본 크기 / Original size: {original_width}x{original_height}px")

    # Resize while keeping aspect ratio / 종횡비 유지하며 리사이즈
    # Calculate new size maintaining aspect ratio / 종횡비를 유지하며 새 크기 계산
    ratio = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    
    # Resize the image / 이미지 리사이즈
    img = img.resize((new_width, new_height), Image.LANCZOS)
    print(f"변환 크기 / Resized to: {new_width}x{new_height}px")

    # Output file path (.jpg)
    out_path = output_dir / (png_path.stem + ".jpg")

    # Save as JPEG with quality and dpi
    img.save(
        out_path,
        "JPEG",
        quality=90,      # 1~100 (높을수록 용량↑, 화질↑)
        dpi=target_dpi,
        optimize=True
    )

    print(f"Saved: {out_path}")

print("\nConversion complete!")

