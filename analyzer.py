"""
ReviewInsight AI - Review Analyzer Module
Contains the core logic for analyzing product reviews.
This module identifies sentiment, complaints, feature requests, and praised aspects.
"""

import re
from collections import Counter
from textblob import TextBlob


class ReviewAnalyzer:
    """
    Analyzes product reviews to extract insights about sentiment,
    complaints, feature requests, and praised aspects.
    """
    
    def __init__(self):
        """Initialize the analyzer with keyword patterns"""
        
        # Keywords that indicate feature requests
        self.feature_request_keywords = [
            r'please add',
            r'i want',
            r'i would like',
            r'they should add',
            r'it would be better if',
            r'we need',
            r'should have',
            r'would be nice',
            r'could add',
            r'can we have',
            r'feature request',
            r'add support for'
        ]
        
        # Keywords indicating complaints/negative aspects
        self.complaint_keywords = [
            r'slow',
            r'heating',
            r'hot',
            r'lag',
            r'crash',
            r'bug',
            r'issue',
            r'problem',
            r'broken',
            r'doesn\'t work',
            r'won\'t work',
            r'battery drain',
            r'overheating',
            r'glitch'
        ]
        
        # Keywords indicating praised aspects
        self.praise_keywords = [
            r'excellent',
            r'amazing',
            r'great',
            r'good',
            r'wonderful',
            r'fantastic',
            r'love',
            r'best',
            r'awesome',
            r'perfect',
            r'impressed',
            r'impressed'
        ]
    
    def analyze(self, reviews):
        """
        Main analysis function that processes all reviews.
        
        Args:
            reviews: List of review strings
            
        Returns:
            Dictionary containing all analysis results
        """
        
        if not reviews:
            return {'error': 'No reviews provided'}
        
        # Analyze sentiment for each review
        sentiments = [self._analyze_sentiment(review) for review in reviews]
        
        # Calculate sentiment summary
        sentiment_summary = self._calculate_sentiment_summary(sentiments)
        
        # Extract complaints
        complaints = self._extract_complaints(reviews)
        
        # Extract feature requests
        feature_requests = self._extract_feature_requests(reviews)
        
        # Extract praised aspects
        praised_aspects = self._extract_praised_aspects(reviews)
        
        # Calculate overall satisfaction
        overall_satisfaction = self._calculate_overall_satisfaction(sentiments)
        
        return {
            'sentiment_summary': sentiment_summary,
            'complaints': complaints,
            'feature_requests': feature_requests,
            'praised_aspects': praised_aspects,
            'overall_satisfaction': overall_satisfaction,
            'total_reviews': len(reviews)
        }
    
    def _analyze_sentiment(self, review):
        """
        Analyze sentiment of a single review using TextBlob.
        
        Args:
            review: Review text string
            
        Returns:
            'positive', 'negative', or 'neutral'
        """
        
        # Create TextBlob object for sentiment analysis
        blob = TextBlob(review)
        polarity = blob.sentiment.polarity
        
        # Classify sentiment based on polarity score
        if polarity > 0.1:
            return 'positive'
        elif polarity < -0.1:
            return 'negative'
        else:
            return 'neutral'
    
    def _calculate_sentiment_summary(self, sentiments):
        """
        Calculate percentages for each sentiment category.
        
        Args:
            sentiments: List of sentiment labels
            
        Returns:
            Dictionary with sentiment percentages
        """
        
        total = len(sentiments)
        if total == 0:
            return {'positive': 0, 'negative': 0, 'neutral': 0}
        
        # Count each sentiment type
        sentiment_counts = Counter(sentiments)
        
        return {
            'positive': round((sentiment_counts.get('positive', 0) / total) * 100),
            'negative': round((sentiment_counts.get('negative', 0) / total) * 100),
            'neutral': round((sentiment_counts.get('neutral', 0) / total) * 100)
        }
    
    def _extract_complaints(self, reviews):
        """
        Extract and count recurring complaints from reviews.
        
        Args:
            reviews: List of review strings
            
        Returns:
            List of complaints sorted by frequency
        """
        
        found_complaints = []
        
        for review in reviews:
            review_lower = review.lower()
            
            # Check for negative sentiment first
            if self._analyze_sentiment(review) != 'positive':
                # Look for complaint keywords in the review
                for keyword in self.complaint_keywords:
                    if re.search(keyword, review_lower):
                        # Extract the phrase around the complaint keyword
                        complaint = self._extract_phrase(review_lower, keyword)
                        if complaint:
                            found_complaints.append(complaint)
        
        # Count complaints and remove duplicates
        complaint_counts = Counter(found_complaints)
        
        # Filter complaints that appear more than once and sort by frequency
        complaints = [
            {
                'complaint': complaint,
                'count': count
            }
            for complaint, count in complaint_counts.most_common()
            if count >= 1
        ]
        
        return complaints[:10]  # Return top 10 complaints
    
    def _extract_feature_requests(self, reviews):
        """
        Extract and group feature requests from reviews.
        
        Args:
            reviews: List of review strings
            
        Returns:
            List of feature requests sorted by frequency
        """
        
        found_requests = []
        
        for review in reviews:
            review_lower = review.lower()
            
            # Look for feature request keywords
            for keyword in self.feature_request_keywords:
                if re.search(keyword, review_lower):
                    # Extract the phrase containing the feature request
                    request = self._extract_phrase(review_lower, keyword)
                    if request:
                        found_requests.append(request)
        
        # Count requests and remove duplicates
        request_counts = Counter(found_requests)
        
        # Sort by frequency
        feature_requests = [
            {
                'request': request,
                'count': count
            }
            for request, count in request_counts.most_common()
        ]
        
        return feature_requests[:10]  # Return top 10 requests
    
    def _extract_praised_aspects(self, reviews):
        """
        Extract and count frequently praised aspects.
        
        Args:
            reviews: List of review strings
            
        Returns:
            List of praised aspects sorted by frequency
        """
        
        found_aspects = []
        
        for review in reviews:
            review_lower = review.lower()
            
            # Check for positive sentiment
            if self._analyze_sentiment(review) != 'negative':
                # Look for praise keywords
                for keyword in self.praise_keywords:
                    if re.search(keyword, review_lower):
                        # Extract the aspect being praised
                        aspect = self._extract_phrase(review_lower, keyword)
                        if aspect:
                            found_aspects.append(aspect)
        
        # Count aspects and remove duplicates
        aspect_counts = Counter(found_aspects)
        
        # Sort by frequency
        praised_aspects = [
            {
                'aspect': aspect,
                'mentions': count
            }
            for aspect, count in aspect_counts.most_common()
        ]
        
        return praised_aspects[:10]  # Return top 10 aspects
    
    def _extract_phrase(self, text, keyword_pattern):
        """
        Extract a meaningful phrase from text based on a keyword pattern.
        
        Args:
            text: Text to extract from
            keyword_pattern: Regex pattern to search for
            
        Returns:
            Extracted phrase or None
        """
        
        # Find the keyword in the text
        match = re.search(keyword_pattern, text)
        if not match:
            return None
        
        start = match.start()
        
        # Extract words around the keyword (up to 15 characters after)
        end = min(start + 50, len(text))
        phrase = text[start:end].strip()
        
        # Clean up the phrase
        phrase = re.sub(r'[.,!?;:]$', '', phrase).strip()
        
        return phrase if phrase else None
    
    def _calculate_overall_satisfaction(self, sentiments):
        """
        Calculate overall customer satisfaction score.
        
        Args:
            sentiments: List of sentiment labels
            
        Returns:
            Satisfaction score (0-100) and description
        """
        
        if not sentiments:
            return {'score': 0, 'description': 'No data available'}
        
        positive_count = sentiments.count('positive')
        total = len(sentiments)
        satisfaction_score = round((positive_count / total) * 100)
        
        # Determine satisfaction description based on score
        if satisfaction_score >= 70:
            description = 'Very High - Customers are generally satisfied'
        elif satisfaction_score >= 50:
            description = 'Moderate - Mixed customer feedback'
        elif satisfaction_score >= 30:
            description = 'Low - More negative feedback than positive'
        else:
            description = 'Very Low - Customers are mostly dissatisfied'
        
        return {
            'score': satisfaction_score,
            'description': description
        }
