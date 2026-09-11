#!/bin/bash

# ReviewInsight AI - Setup Script
# This script automates the setup process for beginners

echo "🚀 ReviewInsight AI - Setup Guide"
echo "================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✅ Python 3 detected"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

echo "🔧 Activating virtual environment..."
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null

echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📚 Downloading TextBlob language data..."
python -m textblob.download_corpora

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Activate the virtual environment:"
echo "      - On Windows: venv\\Scripts\\activate"
echo "      - On macOS/Linux: source venv/bin/activate"
echo ""
echo "   2. Run the application:"
echo "      python app.py"
echo ""
echo "   3. Open your browser:"
echo "      http://localhost:5000"
echo ""
echo "🎉 Happy analyzing!"
