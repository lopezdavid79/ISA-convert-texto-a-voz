import wx
from gtts.lang import tts_langs
from funciones import cargarConfiguracion,voices_list, speed_n, volumen_n 


class  Preference(wx.Dialog):
	def __init__(self, *args ,**qwargs):
		super().__init__(*args ,**qwargs)
		self.speed=speed_n()
		self.volumen=volumen_n()
		self.audio=['mp3','wav']
		self.voice=voices_list()
		self.config = cargarConfiguracion()
#carga  los valores de preferencia
		self.pathDir=self.config.path
		voiceKey= self.config.voice
		speed= self.config.speed
		audio = self.config.audio
		volumen = self.config.volumen


		self.SetTitle('Preferencias')
		
		panel=wx.Panel(self)

		wx.StaticText(panel,-1,label='Ubicación:')
		
		self.name = wx.TextCtrl(panel)
		self.name.SetValue(self.pathDir)
		btnCarpeta = wx.Button(panel , -1 , 'examinar..')
		idAud =self.audio.index(audio)
		self.lbAudio=wx.ListBox(panel , -1 , choices=self.audio)
		self.lbAudio.SetSelection(idAud)
		wx.StaticText(panel,-1,label='Voces:')
		idVoi=self.voice.index(voiceKey)
		self.lbVoice=wx.ListBox(panel , -1 , choices=self.voice)
		self.lbVoice.SetSelection(idVoi)
		
		wx.StaticText(panel,-1,label='Velocidad')
		idSpeed= self.speed.index(speed)
		self.lbSpeed=wx.ListBox(panel , -1 , choices=self.speed)
		self.lbSpeed.SetSelection(idSpeed)


		wx.StaticText(panel,-1,label='Volumen')
		idVolumen= self.volumen.index(volumen)
		self.lbVolumen=wx.ListBox(panel , -1 , choices=self.volumen)
		self.lbVolumen.SetSelection(idVolumen)


		btnOk= wx.Button(panel, wx.ID_OK,'aceptar')
		btnCancel= wx.Button(panel, wx.ID_CANCEL,'Cancelar')
		btnCarpeta.Bind(wx.EVT_BUTTON,self.folder)
	def getFilename(self):
		return self.name.GetValue()
	def getSpeed(self):
		id=self.lbSpeed.GetSelection()
		return self.speed[id]

	def getLang(self):
		idL=self.lbLang.GetSelection()
		return self.lang[idL]

	def getAudio(self):
		idA=self.lbAudio.GetSelection()
		return self.audio[idA]

	def folder(self , event):
		dlgFol = wx.DirDialog(self, "seleccione carpeta")
		if dlgFol.ShowModal() == wx.ID_OK:
			self.pathDir= dlgFol.GetPath()
			self.name.SetValue(self.pathDir)
		dlgFol.Destroy



	def getPath(self):
		return self.pathDir
#objeto configuracion cargado por defecto
	def getConfig(self):
		return self.config

	def getVoice(self):
		idV=self.lbVoice.GetSelection()
		return self.voice[idV]
	def getVolumen(self):
		idVol=self.lbVolumen.GetSelection()
		return self.volumen[idVol]
