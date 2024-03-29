import librosa
import soundfile as sf
import wave
import speech_recognition as sr

def convert_file(audio_path):
    x,_ = librosa.load(audio_path, sr=16000)
    temp_path = 'tmp.wav';
    sf.write('tmp.wav', x, 16000)
    wave.open('tmp.wav','r')
    return temp_path
    
def recognize_speech(audio_file):
    recognizer = sr.Recognizer()
    
    # Load audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    
    # Perform speech recognition
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")