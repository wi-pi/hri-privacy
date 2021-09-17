from google.cloud import texttospeech

class Google_TTS:
    """
    Google text to speech API class. Can be used to get metadata such as entities, sentiments, and topics from a specified document.
    """
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()
        self.language = "en-US"
        self.name = 'en-US-Wavenet-H'
        self.voice = texttospeech.VoiceSelectionParams(language_code=self.language, name=self.name, ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
        self.audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    def create_speech(self, text):
        self.input = texttospeech.SynthesisInput(text=text)
        response = self.client.synthesize_speech(input=self.input, voice=self.voice, audio_config=self.audio_config)
        with open('output.mp3', 'wb') as out:
            out.write(response.audio_content)

tts = Google_TTS()
tts.create_speech('I hope you weren\'t planning on an early lunch.')