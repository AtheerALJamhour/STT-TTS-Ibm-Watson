url = "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/3bc43ea3-d220-43a4-b9dc-83c40b26c80a"
apikey = 'e9mSKC4JI_NKzQjQXQIpU33BxcpYtTlADcEnRNTWqe4y'



#First i need to import dependecies from ibm watson sdk that i installed


from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#Setup Service 
authenticator = IAMAuthenticator ('e9mSKC4JI_NKzQjQXQIpU33BxcpYtTlADcEnRNTWqe4y')
# New TTS Service 
tts = TextToSpeechV1(authenticator=authenticator) 
# Set Service URL
tts.set_service_url( "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/3bc43ea3-d220-43a4-b9dc-83c40b26c80a")

with open('./speech.mp3' ,'wb') as audio_file:
    res = tts.synthesize('Hellow world' , accept='audio/mp3' , voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)