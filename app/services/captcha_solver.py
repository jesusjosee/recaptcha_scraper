from app.services.audio_service import AudioService

class CaptchaSolver:
    def __init__(self, audio_service: AudioService):
        self.audio_service = audio_service

    def solve_audio_challenge(self, url: str) -> str:
        output_wav_path = "audio_challenge.wav"
        self.audio_service.download_audio(url, output_wav_path)
        return self.audio_service.transcribe_audio(output_wav_path)
