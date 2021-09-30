import os
from jiwer import wer

def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    import io

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(encoding=speech.RecognitionConfig.AudioEncoding.FLAC, sample_rate_hertz=16000, language_code="en-US")

    response = client.recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        #print(u"Transcript: {}".format(result.alternatives[0].transcript))
        output = result.alternatives[0].transcript
    
    return output

def read_files(path):
    import glob
    t_path = os.path.join(path, '*')
    dirs = glob.glob(t_path)

    sub_dirs_all = []
    for d in dirs:
        dir_path = os.path.join(t_path, d)
        t_dir_path = os.path.join(dir_path, '*')
        sub_dirs_all.extend(glob.glob(t_dir_path))

    files = []
    for sub_d in sub_dirs_all:
        t_sub_d = os.path.join(sub_d, '*')
        files.extend(glob.glob(t_sub_d))

    return files


def populate(files):
    transcript_files = []
    for f in files:
        if 'txt' in f:
            transcript_files.append(f)
    
    truth_dict = {}
    for f in transcript_files:
        #key = f.split('/')[-1].split('.')[0]
        p = open(f, 'r')
        lines = p.readlines()
        p.close()
        for l in lines:
            l = l.strip()
            key = l.split(' ')[0]
            truth_dict[key] = l.replace(key, '')
    
    return truth_dict

def obtain_truth(speech_file, t_dict):
    key = speech_file.split('/')[-1].split('.')[0]
    if key in t_dict:
        return t_dict[key]
    else:
        return None

if __name__ == "__main__":
    #speech_file = "resources/commercial_mono.wav"
    #stt = Google_STT(2)
    
    path = '/nobackup/varun/datasets/LibriSpeech_hri/test-clean'
    files = read_files(path)
    
    truth_dict = populate(files)

    error_list = []
    for speech_file in files:
        output = transcribe_file(speech_file)
        truth = obtain_truth(speech_file, truth_dict)
        if truth != None and output != None:
            output = output.upper()
            error = wer(truth, output)
            error_list.append(error)


    print("AVG WER:", sum(error_list)/len(error_list))
