@echo off
REM ReviewInsight AI - Setup Script for Windows
REM This script automates the setup process for beginners

echo.
echo 🚀 ReviewInsight AI - Setup Guide for Windows
echo =============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.7 or higher.
    pause
    exit /b 1
)

echo ✅ Python detected
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

echo 📥 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo 📚 Downloading TextBlob language data...
python -m textblob.download_corpora

echo.
echo ✅ Setup complete!
echo.
echo 📝 Next steps:
echo    1. Activate the virtual environment:
 echo       venv\Scripts\activate
echo.
echo    2. Run the application:
echo       python app.py
echo.
echo    3. Open your browser:
echo       http://localhost:5000
echo.
echo 🎉 Happy analyzing!
echo.
pause
