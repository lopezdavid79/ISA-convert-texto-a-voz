from pickle import load, dump
from modelo.configuracion import Config
import pyttsx3

def cargarConfiguracion():
	try:
		f=open("app.cfg", "rb")
	except FileNotFoundError:
		cf = Config('C: ' , 'Microsoft Raul Mobile - Spanish (Mexico)', 'mp3',100 ,50)
		guardarConfiguracion(cf)
	else:
		cf = load(f)
		f.close()
	
	return cf
	
def guardarConfiguracion(config):
	f=open("app.cfg", "wb")
	dump(config, f)
	f.close()
	print("guardando")



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

def speed_n():
	l=[]
	for i in range (150,1,-1):
		l.append('{} '.format(i))
	return l
def volumen_n():
	vol=[]
	for v in range    (100,0,-1):
		vol.append('{} '.format(v))
	return vol 
	