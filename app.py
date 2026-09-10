"""
ReviewInsight AI - Product Review Analysis Application
Main Flask application file that handles routing and API endpoints.
"""

from flask import Flask, render_template, request, jsonify
from analyzer import ReviewAnalyzer
import json

# Initialize Flask application
app = Flask(__name__)

# Initialize the review analyzer
analyzer = ReviewAnalyzer()


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/api/analyze', methods=['POST'])
def analyze_reviews():
    """
    API endpoint to analyze reviews.
    Expects JSON with 'reviews' key containing review text.
    """
    try:
        # Get the review text from request
        data = request.get_json()
        reviews_text = data.get('reviews', '').strip()
        
        # Validate input
        if not reviews_text:
            return jsonify({
                'error': 'Please enter at least one review to analyze.'
            }), 400
        
        # Split reviews by newline (each review on a new line)
        reviews = [r.strip() for r in reviews_text.split('\n') if r.strip()]
        
        if len(reviews) == 0:
            return jsonify({
                'error': 'Please enter valid reviews.'
            }), 400
        
        # Analyze the reviews
        results = analyzer.analyze(reviews)
        
        return jsonify(results), 200
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            'error': f'An error occurred during analysis: {str(e)}'
        }), 500


if __name__ == '__main__':
    # Run the Flask app in debug mode for development
    app.run(debug=True, port=5000)
