
import pyttsx3
def   voices_list():
#Cambiando voces 
	string_voces=[]
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	for i,voice in enumerate  (voices):
		engine.setProperty('voice', voice.id)
		string_voces.append(voices[i].name)

	# engine.runAndWait()
	return string_voces 