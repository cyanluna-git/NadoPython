"""
Desktop launcher for the Video OCR Extractor Streamlit app.

Run directly with Python (`python run_app.py`) or use this as the
PyInstaller entry point to build a standalone .exe (see build_exe.bat).
"""
import os
import sys

import streamlit.web.cli as stcli


def resolve_app_path() -> str:
    if getattr(sys, "frozen", False):
        # Running inside a PyInstaller-built executable.
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "app.py")


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_app_path(),
        "--global.developmentMode=false",
        "--server.headless=false",
    ]
    sys.exit(stcli.main())
