import io

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

client = speech.SpeechClient()

# path = 'hh210409-hiroto-vol28.flac'
# with io.open(path, "rb") as audio_file:
#     content = audio_file.read()

audio = types.RecognitionAudio(uri="gs://mysoundtext2/210408-akky-vol200.flac")
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=8000,
    language_code="ja-JP",
    use_enhanced=True,
    enable_automatic_punctuation=True,
    # A model must be specified to use enhanced model.
    model="default",
)

operation = client.long_running_recognize(config=config, audio=audio)

print("Waiting for operation to complete...")
response = operation.result(timeout=600)

# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print(u"Transcript: {}".format(result.alternatives[0].transcript))
    print("Confidence: {}".format(result.alternatives[0].confidence))
