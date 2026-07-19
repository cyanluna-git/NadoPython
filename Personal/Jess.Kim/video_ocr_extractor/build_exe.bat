@echo off
REM Build VideoOCRExtractor.exe on Windows.
REM Run this from inside the video_ocr_extractor folder, in a venv with
REM requirements.txt + pyinstaller installed:
REM
REM   python -m venv venv
REM   venv\Scripts\activate
REM   pip install -r requirements.txt
REM   pip install pyinstaller
REM   build_exe.bat
REM
REM Output: dist\VideoOCRExtractor.exe

pyinstaller ^
  --name VideoOCRExtractor ^
  --onefile ^
  --noconfirm ^
  --add-data "app.py;." ^
  --add-data ".streamlit;.streamlit" ^
  --collect-all streamlit ^
  --collect-all streamlit_drawable_canvas ^
  --collect-all pytesseract ^
  --collect-all cv2 ^
  --collect-all fpdf ^
  --hidden-import streamlit_drawable_canvas ^
  run_app.py

echo.
echo Done. Find the executable at dist\VideoOCRExtractor.exe
