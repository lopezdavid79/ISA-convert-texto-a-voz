import pyttsx3

class ConversionText():
	def __init__(self, text,name,volume,speed, voice,*args , **qwargs):
		self.text= text
		self.name=name
		self.speed= speed
		self.volume=volume
		self.voice=voice
		


	def  config_tts(self):
		self.engine = pyttsx3.init()
#Cambiando voces 
		voices = self.engine.getProperty('voices')
#selecionar voz
		self.engine.setProperty('voice', voices[self.voice].id)
#velocidad de la voz
		self.engine.setProperty("rate", self.speed)
#volumen del mismo, el cual podremos ajustar dentro de un rango que va desde 0.0 a 1.0:
		self.engine.setProperty("volume", self.volume)
		
	def escucha_previa(self):
		self.engine = pyttsx3.init()
		self.engine.say(self.text)
		self.engine.runAndWait()


	def pausa(self):
		self.engine = pyttsx3.init()
		self.engine.stop()
		self.engine.runAndWait()

	def grabar_tts(self):
		engine = pyttsx3.init()
		audio_file=self.name
		self.engine.save_to_file(self.text, audio_file)
		self.engine.runAndWait()
