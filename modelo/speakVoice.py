import wx
import speech_recognition as sr
import winsound
from  accessible_output2.outputs.sapi5 import SAPI5


class Speak():
	def __init__(self ,  texto , *args , **qwargs):
		self.texto=texto
		self.sText=[]



	def dictando(self):
		r = sr.Recognizer()		
		freq = 2500 # Set frequency To 2500 Hertz
		dur = 40 # Set duration To 10 ms == 1 second
		winsound.Beep(freq, dur)

		with sr.Microphone() as source:
			audio = r.listen(source)

			try:
				self.sText = r.recognize_google(audio, language='es')
			except:
				mj=wx.MessageBox("su microfono esta desconectado o funciona incorrectamente, verifique antes de seguir intentando usar el dictado por voz  ","advertencia")
				mj.ShowModal()

	def getText(self):

		return self.texto+self.sText


