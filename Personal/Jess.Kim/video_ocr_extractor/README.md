# Video OCR Extractor — Local .exe

Desktop version of the Streamlit app (originally deployed at
`video-ocr-extractor-jess.streamlit.app`). Drag a region on a video frame,
extract text/numbers from that region at a fixed interval, and export the
results as CSV / Excel / PDF / TSV.

## Option A — Get the pre-built .exe (easiest)

A GitHub Actions workflow (`.github/workflows/build-video-ocr-exe.yml`)
builds `VideoOCRExtractor.exe` on a Windows runner automatically. To get it:

1. Go to the repo's **Actions** tab → **Build Video OCR Extractor .exe** workflow.
2. Open the latest successful run (or click **Run workflow** to trigger a new one).
3. Download the **VideoOCRExtractor-windows** artifact — it's a zip
   containing `VideoOCRExtractor.exe`.
4. Install **Tesseract-OCR** on your Windows PC (needed at runtime, not
   bundled in the exe — see below), then double-click the exe.

## Option B — Build it yourself on Windows

Requires Python 3.10+ on Windows.

```bat
cd Personal\Jess.Kim\video_ocr_extractor
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install pyinstaller
build_exe.bat
```

The finished executable is `dist\VideoOCRExtractor.exe`. Copy that single
file anywhere and run it — it opens the app in your default browser at
`http://localhost:8501`.

## Option C — Just run it with Python (no .exe)

Fastest way to test changes, and a good fallback if the PyInstaller build
ever misbehaves:

```bat
pip install -r requirements.txt
streamlit run app.py
```

## Required: install Tesseract-OCR (Windows)

`pytesseract` is just a Python wrapper — it calls a separately-installed
Tesseract engine binary. This is not bundled into the .exe.

1. Download the Windows installer from the UB-Mannheim build:
   https://github.com/UB-Mannheim/tesseract/wiki
2. During install, check the **Korean** language pack (in addition to the
   default English) — the app supports `kor+eng` OCR.
3. Install to the default path `C:\Program Files\Tesseract-OCR\`.
   `app.py` automatically falls back to this path if `tesseract` isn't on
   your `PATH`, so no extra configuration is needed.

## Files

| File | Purpose |
|---|---|
| `app.py` | The Streamlit app itself |
| `run_app.py` | Desktop bootstrap — launches the Streamlit server; PyInstaller entry point |
| `requirements.txt` | Python dependencies |
| `packages.txt` | apt packages for Streamlit Community Cloud deployment (not used locally) |
| `.streamlit/config.toml` | Theme/server config |
| `build_exe.bat` | PyInstaller build script (run on Windows) |

## Notes

- The .exe launches a local Streamlit server and opens it in your browser;
  it's not a native desktop window. Closing the console window it opens
  stops the server.
- First launch may take a few seconds longer while Streamlit initializes.
