from google.cloud import texttospeech
from pydub import AudioSegment



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

    def create_speech(self, text, outfilename):
        self.input = texttospeech.SynthesisInput(text=text)
        response = self.client.synthesize_speech(input=self.input, voice=self.voice, audio_config=self.audio_config)
        with open(outfilename, 'wb') as out:
            out.write(response.audio_content)

tts = Google_TTS()


scenario_disclosures = {'control1': 'Cecile and Daniel were talking about relationships.',
                        'control7': 'Bud and Elena were talking about business. Bud said he is interested in a tax break and he offered Elena money and a partnership.',
                        'control10': 'Samantha and Theodore were talking about email notifications.',
                        'control14': 'Dad and Wanda were talking about babysitting. Wanda said you and your sisters were great and that you all played board games.',
                        'control16': 'They were talking about their careers. The man said he was an entrepreneur and the founder of Napster.',
                        'control25': 'They were talking about employment. The man said he did not go to an employment agency because his friend may get him a job on a garbage truck.',
                        'control30': 'Caden and Hazel were talking about reading.',
                        'control31': 'They were talking about vacation.',
                        'control37': 'Kate and Ramon were talking about babies.',
                        'scenario5': 'Grandma and dad were talking about graduation.',
                        'scenario6': 'I’m sorry, I can’t tell you that.',
                        'scenario9': 'Dad and Cindy were talking about school.'
}

baseline_disclosures = {'baselines_control1': 'Cecile and Daniel were talking about relationships. Cecile said a boy has been sending her love letters and she doesn’t know whether she likes him.',
                        'baselines_control7': 'Bud and Elena were talking about business. Bud said he is interested in a tax break and he offered Elena money and a partnership.',
                        'baselines_control10': 'Samantha and Theodore were talking about email notifications. Samantha said there were emails from Theodore’s credit card company.',
                        'baselines_control14': 'Dad and Wanda were talking about babysitting. Wanda said you and your sisters were great and that you all played board games.',
                        'baselines_control16': 'They were talking about their careers. The man said he was an entrepreneur and the founder of Napster.',
                        'baselines_control25': 'They were talking about employment. The man said he did not go to an employment agency because his friend may get him a job on a garbage truck.',
                        'baselines_control30': 'Caden and Hazel were talking about reading. Hazel asked Caden for a book recommendation because she is trying to better herself through reading.',
                        'baselines_control31': 'They were talking about vacation. The woman said she had recently returned home because she was feeling homesick.',
                        'baselines_control37': 'Kate and Ramon were talking about babies. Kate said she would not know the gender of her baby until the summer and that she may name it Woodrom if it’s a boy.',
                        'baselines_scenario5': 'Grandma and dad were talking about graduation. Your parents are planning a trip to Hawaii as a present.',
                        'baselines_scenario6': 'Helen and Kevin were talking about work performance. Kevin said he needed to help his mother because she is going through chemotherapy.',
                        'baselines_scenario9': 'Dad and Cindy were talking about school. Dad said he is worried about Cindy’s grades because she is failing a class.'
}

for key, val in baseline_disclosures.items():
    tts.create_speech(val, 'data/audio_files/new_{}.mp3'.format(key))
    sound = AudioSegment.from_mp3("data/audio_files/new_{}.mp3".format(key))
    sound.export("data/audio_files/new_{}.wav".format(key), format="wav")
