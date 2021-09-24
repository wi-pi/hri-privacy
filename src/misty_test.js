misty.Debug("Starting skill: sendAudioLoop");
misty.StopRecordingAudio();
var file = misty.GetAudioFile('NAME_OF_WAV_FILE.wav', _GetAudioCallback());

misty.SendExternalRequest("POST", "http://35.3.86.69:5000/", null, null,
    file, false, false);

responseAudio = misty.SendExternalRequest("GET", "http://35.3.86.69:5000/", null, null,
    null, true, true, "new_NAME_OF_WAV_FILE.wav");

misty.PlayAudio("new_NAME_OF_WAV_FILE.wav", 50);

function getByteArray(dataStr) {
    var array = new Uint8Array(dataStr.length);
    for (var i = 0; i < dataStr.length; i++) {
        array[i] = dataStr.charCodeAt(i);
    }
    return array;
}

var formData = {
  // Pass a simple key-value pair
  my_field: 'my_value',
  // Pass data via Buffers
  my_buffer: new Buffer([1, 2, 3]),
  // Pass data via Streams
  my_file: fs.createReadStream(__dirname + '/unicycle.jpg'),
  // Pass multiple values /w an Array
  attachments: [
    fs.createReadStream(__dirname + '/attachment1.jpg'),
    fs.createReadStream(__dirname + '/attachment2.jpg')
  ],
  // Pass optional meta-data with an 'options' object with style: {value: DATA, options: OPTIONS}
  // Use case: for some types of streams, you'll need to provide "file"-related information manually.
  // See the `form-data` README for more information about options: https://github.com/form-data/form-data
  custom_file: {
    value:  fs.createReadStream('/dev/urandom'),
    options: {
      filename: 'topsecret.jpg',
      contentType: 'image/jpeg'
    }
  }
};
request.post({url:'http://service.com/upload', formData: formData}, function optionalCallback(err, httpResponse, body) {
  if (err) {
    return console.error('upload failed:', err);
  }
  console.log('Upload successful!  Server responded with:', body);
});


function _GetAudioCallback(callbackData) {
    var audio = callbackData.Result.Base64;
    misty.SendExternalRequest("POST", "http://35.3.86.69:5000/files/mistyAudioRecording.wav", null, null,
    audio, false, false);
}