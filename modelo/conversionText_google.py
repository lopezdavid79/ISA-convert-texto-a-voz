from gtts import gTTS

class ConversionText():
	def __init__(self, text,name,lang,speed, *args , **qwargs):
		self.text= text
		self.name=name
		self.speed= speed
		self.lang=lang
		


	def google_tts_load(self ):
		print (self.lang)
		voz = gTTS(self.text, lang=self.lang, slow=self.speed)
		voz.save(self.name) 
