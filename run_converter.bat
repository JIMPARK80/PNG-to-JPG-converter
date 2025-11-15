@echo off
chcp 65001 >nul
echo PNG to JPG Batch Converter / PNG 일괄 JPG 변환기
echo ================================================
echo.

REM Activate virtual environment / 가상환경 활성화
REM If virtual environment exists, activate it / 가상환경이 있으면 활성화
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

echo.
python png_to_jpg_batch.py
echo.
pause

