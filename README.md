# PNG to JPG Batch Converter / PNG 일괄 JPG 변환기

A simple Python script to batch convert PNG images to JPG format with resizing and DPI adjustment.

PNG 이미지를 JPG로 일괄 변환하고 리사이즈 및 DPI를 조정하는 간단한 파이썬 스크립트입니다.

## Features / 기능

- Converts all PNG files in a folder to JPG format
- 한 폴더 안의 모든 PNG 파일을 JPG 형식으로 변환
- Interactive resolution input (e.g., 6000x6000px)
- 대화형 해상도 입력 (예: 6000x6000px)
- Resizes images while preserving aspect ratio
- 종횡비를 유지하며 이미지 리사이즈
- Sets DPI to 300 (configurable)
- DPI를 300으로 설정 (설정 가능)

## Installation / 설치

1. Install Python (if not already installed)
   파이썬이 없다면 먼저 파이썬을 설치합니다.

2. Activate virtual environment (if using one) / 가상환경 활성화 (사용하는 경우)
   ```bash
   # Windows Command Prompt
   D:\GameMake\myenv\Scripts\activate.bat
   
   # Windows PowerShell
   D:\GameMake\myenv\Scripts\Activate.ps1
   ```

3. Install dependencies using pip:
   pip로 의존성을 설치합니다:

```bash
pip install -r requirements.txt
```

Or install Pillow directly:
또는 Pillow를 직접 설치:

```bash
pip install pillow
```

## Usage / 사용법

1. Create an `input` folder in the same directory as the script
   스크립트와 같은 위치에 `input` 폴더를 만듭니다.

2. Put your PNG files in the `input` folder
   PNG 파일들을 `input` 폴더에 넣습니다.

3. Run the script:
   스크립트를 실행합니다:

   **Option 1: Using batch file (recommended) / 배치 파일 사용 (권장)**
   - Double-click `run_converter.bat`
   - `run_converter.bat` 더블클릭 or 실행명령어 .\run_converter.bat (PowerShell)
   - The batch file automatically activates the virtual environment
   - 배치 파일이 자동으로 가상환경을 활성화합니다

   **Option 2: Manual execution / 수동 실행**
   ```bash
   # Activate virtual environment first / 먼저 가상환경 활성화
   D:\GameMake\myenv\Scripts\activate.bat
   
   # Then run the script / 그 다음 스크립트 실행
   python png_to_jpg_batch.py
   ```

4. Enter the desired resolution when prompted (e.g., `6000x6000` or `4000x4000`)
   프롬프트가 나타나면 원하는 해상도를 입력하세요 (예: `6000x6000` 또는 `4000x4000`)
   - Press Enter to use default 4000x4000
   - 엔터만 누르면 기본값 4000x4000을 사용합니다
   - You can enter a single number (e.g., `6000`) for square images
   - 단일 숫자(예: `6000`)를 입력하면 정사각형으로 설정됩니다

5. Find converted JPG files in the `output` folder
   변환된 JPG 파일은 `output` 폴더에서 찾을 수 있습니다.

## Configuration / 설정

### Interactive Resolution Input / 대화형 해상도 입력

When you run the script, you can enter the resolution interactively:
스크립트 실행 시 대화형으로 해상도를 입력할 수 있습니다:

- Format: `6000x6000` or `4000x4000` (width x height)
  형식: `6000x6000` 또는 `4000x4000` (가로 x 세로)
- Single number: `6000` (creates square 6000x6000)
  단일 숫자: `6000` (정사각형 6000x6000 생성)
- Press Enter: Uses default 4000x4000
  엔터만 누르기: 기본값 4000x4000 사용

### Advanced Configuration / 고급 설정

You can modify these settings in `png_to_jpg_batch.py`:
`png_to_jpg_batch.py` 파일에서 다음 설정을 변경할 수 있습니다:

- Default resolution: Change the default values (currently 4000x4000)
  기본 해상도: 기본값 변경 (현재 4000x4000)
- `target_dpi`: DPI setting (default: 300)
  DPI 설정 (기본값: 300)
- `quality`: JPEG quality 1-100 (default: 90)
  JPEG 품질 1-100 (기본값: 90)

## Web Application / 웹 애플리케이션

A web-based version is available for server deployment!
서버 배포용 웹 버전이 제공됩니다!

### Quick Start / 빠른 시작

```bash
# Install dependencies / 의존성 설치
pip install -r requirements.txt

# Run web server / 웹 서버 실행
python app.py

# Open browser / 브라우저에서 열기
# http://localhost:5000
```

### Features / 기능

- 🌐 Web-based interface / 웹 기반 인터페이스
- 📤 Multiple file upload / 여러 파일 동시 업로드
- ⚙️ Customizable resolution and quality / 해상도 및 품질 설정 가능
- 📦 Automatic ZIP download for multiple files / 여러 파일 자동 ZIP 다운로드
- 🔌 API endpoint for programmatic access / 프로그래밍 방식 접근용 API

### Server Deployment / 서버 배포

See `DEPLOYMENT.md` for detailed deployment instructions.
자세한 배포 방법은 `DEPLOYMENT.md`를 참조하세요.

**Recommended platforms / 추천 플랫폼:**
- **Render** ⭐ (가장 추천! 무료, 간편, 자동 HTTPS)
- PythonAnywhere (초보자용 / Beginner-friendly)
- Heroku
- VPS (Ubuntu/Debian) with Gunicorn + Nginx
- Docker

## Windows Batch File / 윈도우 배치 파일

Double-click `run_converter.bat` to run the script easily on Windows.
윈도우에서 `run_converter.bat`를 더블클릭하면 쉽게 실행할 수 있습니다.

The batch file automatically activates the virtual environment at `D:\GameMake\myenv\Scripts` before running the script.
배치 파일은 스크립트 실행 전에 `D:\GameMake\myenv\Scripts`의 가상환경을 자동으로 활성화합니다.

## Notes / 참고사항

- PNG transparency (alpha channel) will be removed when converting to JPG
  PNG 투명도(알파 채널)는 JPG로 변환 시 제거됩니다.
- For web-only usage, `quality=80` is often sufficient
  웹용이라면 `quality=80` 정도면 충분한 경우가 많습니다.
- If you don't care about DPI, you can remove `dpi=target_dpi` from the save function
  DPI를 신경 쓰지 않는다면 save 함수에서 `dpi=target_dpi` 부분을 제거해도 됩니다.

