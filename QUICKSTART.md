# 🚀 Quick Start Guide - ReviewInsight AI

## For Windows Users

### Option 1: Automatic Setup (Recommended)

1. **Download the project**
   ```bash
   git clone https://github.com/BharathMandore/ReviewInsight-AI.git
   cd ReviewInsight-AI
   ```

2. **Run the setup script**
   ```bash
   setup.bat
   ```
   This will automatically:
   - Create a Python virtual environment
   - Install all dependencies
   - Download language data for TextBlob

3. **Activate the environment**
   ```bash
   venv\Scripts\activate
   ```

4. **Start the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   Navigate to: `http://localhost:5000`

### Option 2: Manual Setup

```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download language data
python -m textblob.download_corpora

# Run the app
python app.py
```

---

## For macOS/Linux Users

### Option 1: Automatic Setup (Recommended)

1. **Download the project**
   ```bash
   git clone https://github.com/BharathMandore/ReviewInsight-AI.git
   cd ReviewInsight-AI
   ```

2. **Run the setup script**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
   This will automatically set everything up.

3. **Activate the environment**
   ```bash
   source venv/bin/activate
   ```

4. **Start the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   Navigate to: `http://localhost:5000`

### Option 2: Manual Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download language data
python -m textblob.download_corpora

# Run the app
python app.py
```

---

## Testing the Application

### Quick Test (2 minutes)

1. Open `DEMO_DATA.md` in this repository
2. Copy the first demo dataset (Smartphone Reviews)
3. Paste into the ReviewInsight AI text area
4. Click "Analyze Reviews"
5. See the results!

### What You Should See

✅ **Sentiment breakdown** with percentages
✅ **Overall satisfaction score** with description
✅ **Complaint frequency table** showing issues
✅ **Feature request table** with customer suggestions
✅ **Praised aspects table** with mention counts
✅ **Total review count** analyzed

---

## Troubleshooting

### Problem: "Python not found"
**Solution**: Make sure Python 3.7+ is installed. Download from https://www.python.org/

### Problem: "Port 5000 is already in use"
**Solution**: 
- Edit `app.py`
- Find the line: `app.run(debug=True, port=5000)`
- Change `5000` to `5001` or another free port
- Restart the app

### Problem: "ModuleNotFoundError: No module named 'flask'"
**Solution**: 
```bash
# Make sure you activated the virtual environment, then run:
pip install -r requirements.txt
```

### Problem: "No corpora found" error
**Solution**:
```bash
python -m textblob.download_corpora
```

### Problem: "Connection refused" when opening localhost:5000
**Solution**: Make sure the Flask app is running (you should see "Running on http://127.0.0.1:5000" in the terminal)

---

## Next Steps

1. ✅ Try analyzing different datasets
2. ✅ Customize keywords in `analyzer.py`
3. ✅ Modify the UI in `templates/index.html`
4. ✅ Add new features (file upload, export, etc.)
5. ✅ Share your improvements on GitHub!

---

## Need Help?

1. Check the **Troubleshooting** section above
2. Read the comments in the code files
3. Review the full `README.md`
4. Open an issue on GitHub

**Enjoy analyzing reviews! 🎉**
