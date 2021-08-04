
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
# recognize speech using IBM Speech to Text
# Insert API Key in place of 
# API KEY'
IBM_USERNAME = "apikey"  
IBM_PASSWORD = "zADPQibOqiHly9DTNXLUyze_d9DsvRhzctIweIVpSJMi"
result= r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)

try:
       print("IBM Speech to Text thinks you said " + result)
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Sorry Could not recognize your voice from IBM Speech to Text service; {0}".format(e))
    
    # save STT as txt file
with open('atheer_result.txt',mode ='w') as file: 
   file.write("Recognized text:") 
   file.write("\n") 
   file.write(result) 
print("Good Job You Successfully Voice Registered!")