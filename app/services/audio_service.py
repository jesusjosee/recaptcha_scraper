import requests
from pydub import AudioSegment
import speech_recognition as sr

class AudioService:
    def download_audio(self, url: str, output_path: str) -> None:
        audio_data = requests.get(url).content
        with open("audio_challenge.mp3", "wb") as f:
            f.write(audio_data)
        
        audio = AudioSegment.from_mp3("audio_challenge.mp3")
        audio.export(output_path, format="wav")

    def transcribe_audio(self, wav_path: str) -> str:
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio = recognizer.record(source)
        
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return None
