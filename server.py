"""
Flask server for the Emotion Detection application.

Routes:
- / : Renders the UI
- /emotionDetector : Accepts textToAnalyze and returns formatted emotion results
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as detect_emotion

APP = Flask(__name__)


@APP.route("/")
def home():
    """
    Render the home page.

    Returns:
        str: Rendered HTML template for the UI.
    """
    return render_template("index.html")


@APP.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze emotion for the user-provided statement.

    Query Args:
        textToAnalyze (str): The text to be analyzed.

    Returns:
        str: Formatted response string for the UI.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = detect_emotion(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )


def main():
    """
    Run the Flask development server on port 5000.

    This is the required deployment target for the lab.
    """
    APP.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
