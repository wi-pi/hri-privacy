from google.cloud import speech_v1p1beta1 as speech

class Google_STT:
    """
    Google Speech to Text API class. Can be used to get metadata such as entities, sentiments, and topics from a specified document.
    """
    def __init__(self, num_speakers):
        self.client = lspeech.SpeechClient()
        self.language = "en-US"
        self.model = 'video'
        self.num_speakers = num_speakers

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code=self.language,
            enable_speaker_diarization=True,
            diarization_speaker_count=self.num_speakers,
            enable_automatic_punctuation=True,
            enable_word_time_offsets=True,
        )

    def transcribe(self, audio_bytes):
        audio = speech.RecognitionAudio(content=audio_bytes)
        response = client.recognize(config=config, audio=audio)
        return response


speech_file = "resources/commercial_mono.wav"
stt = Google_STT(2)

with open(speech_file, "rb") as audio_file:
    content = audio_file.read()

sst.transcribe(content)

result = response.results[-1]

words_info = result.alternatives[0].words

# Printing out the output:
for word_info in words_info:
    print(
        u"word: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag)
    )
