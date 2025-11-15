@echo off
chcp 65001 >nul
echo PNG to JPG Batch Converter / PNG 일괄 JPG 변환기
echo ================================================
echo.

REM Activate virtual environment / 가상환경 활성화
call D:\GameMake\myenv\Scripts\activate.bat

echo.
python png_to_jpg_batch.py
echo.
pause

