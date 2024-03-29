from flask_smorest import Blueprint
from flask import request, render_template, jsonify
from speech_process import convert_file, recognize_speech

blp = Blueprint("routes", __name__, description = "Solo blueprint")
AUDIO_PATH = 'audio.wav'

@blp.route('/')
def record_audio():
    return render_template("index.html")

@blp.route('/upload-audio', methods=["GET","POST"])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    
    audio_file = request.files['audio']
    audio_file.save('audio.wav')
    
    return jsonify({'message': 'Audio file uploaded successfully'}), 200
@blp.route('/transcript', methods = ['GET', 'POST'])
def transcript():
    temp_path = convert_file(AUDIO_PATH)
    transcript_text = recognize_speech(temp_path)
    #print(transcript_text)
    print(type(transcript_text))
    return render_template("result.html", transcript_text = transcript_text)
    
