# PNG to JPG Batch Converter v0.1

A simple Python script to batch convert PNG images to JPG format with resizing and DPI adjustment.

## PNG 일괄 JPG 변환기

PNG 이미지를 JPG로 일괄 변환하고 리사이즈 및 DPI를 조정하는 간단한 파이썬 스크립트입니다.

## Features

- Converts all PNG files in a folder to JPG format
- Interactive resolution input (e.g., 6000x6000px)
- Resizes images while preserving aspect ratio
- Sets DPI to 300 (configurable)

## 기능

- 한 폴더 안의 모든 PNG 파일을 JPG 형식으로 변환
- 대화형 해상도 입력 (예: 6000x6000px)
- 종횡비를 유지하며 이미지 리사이즈
- DPI를 300으로 설정 (설정 가능)

## Installation

### 1. Install Python

Download and install Python 3.11 or later from the official website:

- **Download**: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Recommended**: Python 3.11 or 3.12 (latest stable version)

**Important:**
- Check "Add Python to PATH" during installation
- Verify installation: `python --version` or `python3 --version`

### 2. Create Virtual Environment (Recommended)

It's recommended to use a virtual environment to avoid conflicts with other projects.

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Command Prompt:
venv\Scripts\activate.bat

# PowerShell:
venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

**Note:**
- After activation, you'll see `(venv)` in your terminal prompt
- To deactivate: `deactivate`

### 3. Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install Pillow Flask Werkzeug gunicorn
```

**Verify installation:**
```bash
pip list
```

## 설치

### 1. 파이썬 설치

공식 웹사이트에서 Python 3.11 이상 버전을 다운로드하여 설치하세요:

- **다운로드**: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **권장**: Python 3.11 또는 3.12 (최신 안정 버전)

**중요사항:**
- 설치 시 "Add Python to PATH" 옵션을 체크하세요
- 설치 확인: `python --version` 또는 `python3 --version`

### 2. 가상환경 생성 (권장)

다른 프로젝트와의 충돌을 방지하기 위해 가상환경 사용을 권장합니다.

**Windows:**
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Command Prompt:
venv\Scripts\activate.bat

# PowerShell:
venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate
```

**참고:**
- 활성화 후 터미널 프롬프트에 `(venv)`가 표시됩니다
- 비활성화: `deactivate`

### 3. 의존성 설치

필요한 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```

또는 개별적으로 설치:

```bash
pip install Pillow Flask Werkzeug gunicorn
```

**설치 확인:**
```bash
pip list
```

## Usage

1. Create an `input` folder in the same directory as the script

2. Put your PNG files in the `input` folder

3. Run the script:

   **Option 1: Using batch file (Windows only)**
   ```bash
   # Double-click run_converter.bat or run in terminal:
   .\run_converter.bat
   ```
   **Note:** The batch file assumes a virtual environment at `venv\Scripts\activate.bat`

   **Option 2: Manual execution**
   ```bash
   # Activate virtual environment first (if using one)
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   
   # Then run the script
   python png_to_jpg_batch.py
   ```

4. Enter the desired resolution when prompted (e.g., `6000x6000` or `4000x4000`)
   - Press Enter to use default 6000x6000
   - You can enter a single number (e.g., `6000`) for square images

5. Find converted JPG files in the `output` folder

## 사용법

1. 스크립트와 같은 위치에 `input` 폴더를 만듭니다.

2. PNG 파일들을 `input` 폴더에 넣습니다.

3. 스크립트를 실행합니다:

   **방법 1: 배치 파일 사용 (Windows 전용)**
   ```bash
   # run_converter.bat를 더블클릭하거나 터미널에서 실행:
   .\run_converter.bat
   ```
   **참고:** 배치 파일은 `venv\Scripts\activate.bat`에 가상환경이 있다고 가정합니다

   **방법 2: 수동 실행**
   ```bash
   # 먼저 가상환경 활성화 (사용하는 경우)
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   
   # 그 다음 스크립트 실행
   python png_to_jpg_batch.py
   ```

4. 프롬프트가 나타나면 원하는 해상도를 입력하세요 (예: `6000x6000` 또는 `4000x4000`)
   - 엔터만 누르면 기본값 6000x6000을 사용합니다
   - 단일 숫자(예: `6000`)를 입력하면 정사각형으로 설정됩니다

5. 변환된 JPG 파일은 `output` 폴더에서 찾을 수 있습니다.

## Configuration

### Interactive Resolution Input

When you run the script, you can enter the resolution interactively:

- Format: `6000x6000` or `4000x4000` (width x height)
- Single number: `6000` (creates square 6000x6000)
- Press Enter: Uses default 6000x6000

### Advanced Configuration

You can modify these settings in `png_to_jpg_batch.py`:

- Default resolution: Change the default values (currently 6000x6000)
- `target_dpi`: DPI setting (default: 300)
- `quality`: JPEG quality 1-100 (default: 90)

## 설정

### 대화형 해상도 입력

스크립트 실행 시 대화형으로 해상도를 입력할 수 있습니다:

- 형식: `6000x6000` 또는 `4000x4000` (가로 x 세로)
- 단일 숫자: `6000` (정사각형 6000x6000 생성)
- 엔터만 누르기: 기본값 6000x6000 사용

### 고급 설정

`png_to_jpg_batch.py` 파일에서 다음 설정을 변경할 수 있습니다:

- 기본 해상도: 기본값 변경 (현재 6000x6000)
- `target_dpi`: DPI 설정 (기본값: 300)
- `quality`: JPEG 품질 1-100 (기본값: 90)

## Web Application

A web-based version is available for server deployment!

![Web Interface Screenshot](docs/images/pngToJpg%20converter.png)

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run web server
python app.py

# Open browser
# http://localhost:5000
```

### Features

- 🌐 Web-based interface
- 📤 Multiple file upload
- ⚙️ Customizable resolution and quality
- 📦 Automatic ZIP download for multiple files
- 🔌 API endpoint for programmatic access

### Server Deployment

See `DEPLOYMENT.md` for detailed deployment instructions.

**Recommended platforms:**
- **Render** ⭐ (Most recommended! Free, easy, automatic HTTPS)
- PythonAnywhere (Beginner-friendly)
- Heroku
- VPS (Ubuntu/Debian) with Gunicorn + Nginx
- Docker

## 웹 애플리케이션

서버 배포용 웹 버전이 제공됩니다!

![웹 인터페이스 스크린샷](docs/images/pngToJpg%20converter.png)

### 빠른 시작

```bash
# 의존성 설치
pip install -r requirements.txt

# 웹 서버 실행
python app.py

# 브라우저에서 열기
# http://localhost:5000
```

### 기능

- 🌐 웹 기반 인터페이스
- 📤 여러 파일 동시 업로드
- ⚙️ 해상도 및 품질 설정 가능
- 📦 여러 파일 자동 ZIP 다운로드
- 🔌 프로그래밍 방식 접근용 API

### 서버 배포

자세한 배포 방법은 `DEPLOYMENT.md`를 참조하세요.

**추천 플랫폼:**
- **Render** ⭐ (가장 추천! 무료, 간편, 자동 HTTPS)
- PythonAnywhere (초보자용)
- Heroku
- VPS (Ubuntu/Debian) with Gunicorn + Nginx
- Docker

## Windows Batch File

Double-click `run_converter.bat` to run the script easily on Windows.

**Note:**
- The batch file assumes a virtual environment named `venv` in the project directory
- If you use a different virtual environment name or path, edit `run_converter.bat`

## 윈도우 배치 파일

윈도우에서 `run_converter.bat`를 더블클릭하면 쉽게 실행할 수 있습니다.

**참고:**
- 배치 파일은 프로젝트 디렉토리에 `venv`라는 이름의 가상환경이 있다고 가정합니다
- 다른 가상환경 이름이나 경로를 사용한다면 `run_converter.bat`를 수정하세요

## Notes

- PNG transparency (alpha channel) will be removed when converting to JPG
- For web-only usage, `quality=80` is often sufficient
- If you don't care about DPI, you can remove `dpi=target_dpi` from the save function

## 참고사항

- PNG 투명도(알파 채널)는 JPG로 변환 시 제거됩니다
- 웹용이라면 `quality=80` 정도면 충분한 경우가 많습니다
- DPI를 신경 쓰지 않는다면 save 함수에서 `dpi=target_dpi` 부분을 제거해도 됩니다
