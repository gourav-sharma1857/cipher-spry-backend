from flask import Flask, jsonify
from flask_cors import CORS
import requests
import random
from dotenv import load_dotenv
import os

from patterns import ALL_PATTERNS # Assuming patterns.py is in the same directory

load_dotenv()

app = Flask(__name__)

# Configure CORS for your React app
CORS(app, resources={r"/*": {"origins": "https://gourav-sharma1857.github.io"}})

# --- New Global Variable for preventing immediate repetition ---
last_pattern_func = None

# --- External Word API Configuration (Updated) ---
WORD_API_URL = "https://api.datamuse.com/words" # New API URL

@app.route("/get_patterned_word", methods=["GET"])
def get_patterned_word():
    """
    Fetches a random word with a length of 5 characters,
    applies a random pattern, and returns both.
    """
    global last_pattern_func # Declare intent to modify the global variable

    try:
        # 1. Fetch a word from the external API, specifying length=5
        # Using Datamuse API: 'ml' for "means like" (general English words), 'sp' for "spelled like" (wildcard pattern)
        # We'll use 'sp=*?????' to get words with 5 letters.
        # Alternatively, 'max=1' and 's=5' might work for length, but 'sp' is more direct for exact length.
        params = {
            'sp': '?????', # Wildcard for exactly 5 letters
            'max': 100    # Fetch up to 100 words to pick a random one from
        }
        response = requests.get(WORD_API_URL, params=params)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        word_data = response.json()

        # Filter for words that are strictly 5 letters long and choose one
        five_letter_words = [d['word'].upper() for d in word_data if len(d['word']) == 5 and d['word'].isalpha()]

        if not five_letter_words:
            original_word = random.choice(["APPLE", "HOUSE", "TRAIN", "PLANT", "EARTH"])
            print(f"API returned no suitable 5-letter word, using fallback: {original_word}")
        else:
            original_word = random.choice(five_letter_words)
            print(f"Fetched word from DataMuse: {original_word}")

        # 2. Apply a random pattern
        # Get available patterns, excluding the last one if it exists
        available_patterns = ALL_PATTERNS[:] # Create a copy to modify
        if last_pattern_func and len(available_patterns) > 1:
            if last_pattern_func in available_patterns:
                available_patterns.remove(last_pattern_func)
            # If last_pattern_func wasn't in ALL_PATTERNS (shouldn't happen) or only 1 pattern,
            # we just proceed with ALL_PATTERNS to avoid error.

        print(f"DEBUG: Total patterns available (excluding last): {len(available_patterns)}")

        # Choose a new pattern
        pattern_func = random.choice(available_patterns)
        pattern_name = pattern_func.__name__
        print(f"DEBUG: Chosen pattern name: {pattern_name}")

        # Store the chosen pattern as the last one for the next request
        last_pattern_func = pattern_func

        transformed_word = pattern_func(original_word)

        # 3. Return the data as JSON
        return jsonify({
            "original_word": original_word,
            "transformed_word": transformed_word,
            "pattern_applied": pattern_name
        })

    except requests.exceptions.RequestException as e:
        print(f"Error fetching word from API: {e}")
        return jsonify({"error": f"Could not fetch word from external API: {e}"}), 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": f"Internal server error: {e}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True, host="0.0.0.0", port=port)
