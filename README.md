# ReviewInsight AI 🔍

A beginner-friendly web application that analyzes product reviews using natural language processing. Identify sentiment patterns, recurring complaints, feature requests, and frequently praised aspects with an intuitive interface.

## Features

✨ **Sentiment Analysis** - Automatically classify reviews as Positive, Negative, or Neutral
⚠️ **Recurring Complaints** - Find and count problems mentioned repeatedly across reviews
🎯 **Feature Requests** - Extract and group customer feature requests intelligently
👍 **Praised Aspects** - Identify and count frequently praised product features
📊 **Visual Analytics** - Beautiful charts, progress bars, and statistics
😊 **Overall Satisfaction** - Calculate customer satisfaction score with meaningful descriptions

## Technical Stack

- **Backend**: Python with Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **NLP**: TextBlob for sentiment analysis
- **No Database**: In-memory analysis (perfect for beginners)

## Project Structure

```
ReviewInsight-AI/
├── app.py                 # Main Flask application
├── analyzer.py            # Core review analysis logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend UI
└── README.md             # This file
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/BharathMandore/ReviewInsight-AI.git
cd ReviewInsight-AI
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download TextBlob Corpora

TextBlob needs language data. Download it using:

```bash
python -m textblob.download_corpora
```

### Step 5: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

Open your web browser and navigate to the URL. You should see the ReviewInsight AI interface.

## How to Use

1. **Enter Reviews**: Paste or type product reviews in the text area (one review per line)
2. **Click "Analyze Reviews"**: The application processes your reviews
3. **View Results**: Explore the analysis results including:
   - Sentiment breakdown (%)
   - Overall satisfaction score
   - Recurring complaints table
   - Feature requests table
   - Praised aspects table

### Example Input

```
The battery life is excellent, but charging is very slow.
Amazing camera and good battery life.
The phone gets hot while gaming.
Please add faster charging.
I really like the camera quality.
```

### Example Output

- **Sentiment**: Positive 60%, Negative 30%, Neutral 10%
- **Overall Satisfaction**: 60% - Moderate feedback
- **Complaints**: Slow charging, phone heating
- **Feature Requests**: Faster charging
- **Praised Aspects**: Camera, Battery life

## Code Structure & Explanation

### app.py
The main Flask application that:
- Sets up the web server
- Handles the `/` route to display the HTML interface
- Manages the `/api/analyze` POST endpoint for review analysis
- Validates and processes user input
- Returns JSON results to the frontend

### analyzer.py
The core analysis engine with these key methods:

- **`analyze(reviews)`** - Main method that processes all reviews
- **`_analyze_sentiment(review)`** - Determines if a review is positive, negative, or neutral
- **`_extract_complaints(reviews)`** - Finds recurring problems
- **`_extract_feature_requests(reviews)`** - Identifies feature requests
- **`_extract_praised_aspects(reviews)`** - Finds praised features
- **`_calculate_overall_satisfaction(sentiments)`** - Generates satisfaction score

### Key Concepts

#### Sentiment Analysis
Uses TextBlob's built-in sentiment analysis which assigns a polarity score:
- Score > 0.1 = Positive
- Score < -0.1 = Negative
- Score between -0.1 and 0.1 = Neutral

#### Complaint Detection
1. Filters for negative sentiment reviews
2. Searches for complaint keywords (slow, bug, crash, etc.)
3. Counts occurrences to find recurring issues

#### Feature Request Detection
1. Searches for request patterns ("please add", "I want", "should have", etc.)
2. Extracts phrases around these patterns
3. Groups similar requests together

#### Praised Aspects Detection
1. Filters for positive sentiment reviews
2. Searches for praise keywords (great, amazing, excellent, etc.)
3. Extracts and counts mentioned aspects

## Frontend Features

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Real-time Validation**: Checks input before sending to server
- **Loading Indicator**: Visual feedback during analysis
- **Error Handling**: User-friendly error messages
- **Beautiful UI**: Modern gradient design with smooth transitions
- **Data Visualization**: Charts, progress bars, and formatted tables

## Error Handling

The application gracefully handles:
- Empty input (shows error message)
- Invalid reviews (skips empty lines)
- Server errors (displays user-friendly error)
- Network issues (provides guidance)

## Customization Guide

### Adding New Complaint Keywords

Edit `analyzer.py`, find the `complaint_keywords` list and add patterns:

```python
self.complaint_keywords = [
    r'slow',
    r'your_new_keyword',  # Add here
    # ... more keywords
]
```

### Adding New Praise Keywords

Similarly, edit the `praise_keywords` list:

```python
self.praise_keywords = [
    r'excellent',
    r'your_new_keyword',  # Add here
    # ... more keywords
]
```

### Changing the Satisfaction Thresholds

Edit the `_calculate_overall_satisfaction` method:

```python
if satisfaction_score >= 70:  # Change 70 to your threshold
    description = 'Very High - Customers are generally satisfied'
```

### Styling Changes

All CSS is embedded in `templates/index.html`. Look for the `<style>` section to modify colors, fonts, and layout.

## Limitations & Future Improvements

### Current Limitations
- Simple keyword-based analysis (no deep learning)
- Works best with English reviews
- Limited to text input (no file uploads)
- Results cached in memory only

### Future Enhancements
- Support for multiple languages
- File upload functionality (CSV, Excel)
- Database storage for historical analysis
- Export results as PDF/Excel
- Advanced NLP with spaCy or transformers
- Aspect-based sentiment analysis
- Review trends over time

## Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
**Solution**: Run `pip install -r requirements.txt`

### "LookupError: NLTK data not found"
**Solution**: Run `python -m textblob.download_corpora`

### Port 5000 already in use
**Solution**: Edit `app.py` and change `port=5000` to `port=5001` (or another free port)

### Reviews not being analyzed
**Solution**: Ensure each review is on a separate line in the text area

## Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [TextBlob Documentation](https://textblob.readthedocs.io/)
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [JavaScript Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make improvements
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Author

Created as a beginner-friendly project to learn web development, NLP, and data analysis.

## Support

If you encounter any issues:
1. Check the Troubleshooting section
2. Review the code comments in `analyzer.py` and `app.py`
3. Open an issue on GitHub

---

**Happy Analyzing! 🚀**
