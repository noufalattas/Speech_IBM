pip install ibm_watson
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Insert API Key in place of 
# 'YOUR UNIQUE API KEY'
authenticator = IAMAuthenticator('Rnl-ae6yoz9bwc83RCk942FNtVSaSXY4g09V3dzFHjOS')
tts = TextToSpeechV1(
    authenticator=authenticator
)

#Insert URL in place of 'API_URL' 
tts.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/e42c045d-2c34-4c54-9c49-bf50afe27278')

# recognize text using IBM Text to Speech
# save TTS as mp3 file
with open('./speech.mp3', 'wb') as audio_file:
     res = tts.synthesize('Hello, This is IBM Watson', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
     audio_file.write(res.content) #write the content to the audio file 

print("Exporting process completed!")


