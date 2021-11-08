import wx
from gtts.lang import tts_langs

class ConvertirArchivo(wx.Dialog):
	def __init__(self, *args ,**qwargs):
		super().__init__(*args ,**qwargs)
		self.speed=['normal','lento']
		langs = tts_langs()
		self.lang=list(langs.values())
		self.langCode = list(langs.keys())
		self.audio=['mp3','wav']
		self.pathDir=""
		self.SetTitle('convertir a audio')
		
		panel=wx.Panel(self)
		#speed=['rapida','lenta']
		wx.StaticText(panel,-1,label='nombre del archivo')
		self.name = wx.TextCtrl(panel)
		btnCarpeta = wx.Button(panel , -1 , 'examinar..')
		self.lbAudio=wx.ListBox(panel , -1 , choices=self.audio)
		self.lbAudio.SetSelection(0)
		wx.StaticText(panel,-1,label='Velocidad')
		self.lbSpeed=wx.ListBox(panel , -1 , choices=self.speed)
		self.lbSpeed.SetSelection(0)
		wx.StaticText(panel,-1,label='Lenguaje')
		self.lbLang=wx.ListBox(panel , -1 , choices=self.lang)
		self.lbLang.SetSelection(12)
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
		return self.langCode[idL]

	def getAudio(self):
		idA=self.lbAudio.GetSelection()
		return self.audio[idA]

	def folder(self , event):

		dlgFol = wx.DirDialog(self, "seleccione carpeta")
		if dlgFol.ShowModal() == wx.ID_OK:
			self.pathDir= dlgFol.GetPath()
			print(self.pathDir)
		dlgFol.Destroy



	def getPath(self):
		return self.pathDir

