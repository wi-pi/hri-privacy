import base64
infile = open('data/audio_files/mistyAudioRecording.wav', 'rb')
wav_file = open("temp.wav", "wb")
decode_string = base64.b64decode(infile.read())
wav_file.write(decode_string)