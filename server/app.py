#!/usr/bin/env python3

from flask import Flask, request, jsonify, session
from flask_session import Session

app = Flask(__name__)

# Configure the session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Define a secret key for session management
app.secret_key = 'your_secret_key'

# Initialize the page_views session variable
@app.before_request
def before_request():
    session.setdefault('page_views', 0)

# Define a route for viewing articles
@app.route('/articles/<int:id>', methods=['GET'])
def view_article(id):
    # Increment the page_views
    session['page_views'] += 1

    # Check if the user has viewed more than 3 pages
    if session['page_views'] > 3:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401

    # Return the article data (you should replace this with your actual article data)
    article_data = {'id': id, 'title': 'Article Title', 'content': 'Article Content'}
    return jsonify(article_data)

# Define an endpoint to clear the session
@app.route('/clear', methods=['POST'])
def clear_session():
    session['page_views'] = 0
    return jsonify({'message': 'Session cleared'})

if __name__ == '__main__':
    app.run(debug=True)
