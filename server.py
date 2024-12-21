'''
    Executing this function will start the Emotion Detector
   This app is deployed using Flask at port 5000.
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def analyze_emotion():
    ''' This function take the text using GET
    Pass the text into the emotion detector
    Return a text that contains the result of emotion detector
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)
    output = f"""For the given statement,
    the system response is 'anger': {result['anger']},
    'disgust': {result['disgust']},
    'fear': {result['fear']},
    'joy': {result['joy']} and 'sadness': {result['sadness']}.
    The dominant emotion is {result['dominant_emotion']}."""
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return output
@app.route("/")
def render_index():
    '''This function render the index
    '''
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
