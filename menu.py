
import wx
from divConvert  import DivConvert
from pathlib import Path 
import os
#from os import mkdir
from dlPreference import Preference
#from vtnDivConvert import DivConvert 
from modelo.divText import DivText
from modelo.conversionText import ConversionText
from funciones import guardarConfiguracion, cargarConfiguracion, voices_list
from modelo.speakVoice import Speak

class Menu(wx.Frame):
	def __init__(self , *args , ** qwargs):
		super().__init__( *args , ** qwargs)
		self.config = cargarConfiguracion()
		self.voice = voices_list()
		self.iniciarMenu()
	def iniciarMenu(self):
		menubar= wx.MenuBar()
		fileMenu = wx.Menu()

		abrir = fileMenu.Append(-1, 'abrir\tCtrl+o')
		guardar = fileMenu.Append(-1, 'guardar \tCtrl+g')
		guardarComo = fileMenu.Append(-1, 'guardar como \tCtrl+f12')
		guardarAud = fileMenu.Append(-1, 'guardar archivo de audio \tCtrl+s')
		iniciar = fileMenu.Append(-1, 'Dividir  y Convertir en archivo de audio\tCtrl+f8')
		cerrar = fileMenu.Append(-1, 'cerrar\tCtrl+f4')
		salir = fileMenu.Append(wx.ID_EXIT, 'Salir de la aplicación\tCtrl+Q')
		hablarMenu = wx.Menu()
		leer = hablarMenu.Append(-1, 'Leer\tF6')
		pausa = hablarMenu.Append(-1, 'Pausa\tF7')
		toolsMenu = wx.Menu()
		dictado= toolsMenu.Append(-1, 'Dictado Por Voz  \tF5')
		descarga= toolsMenu.Append(-1, 'Descargas   \tCtrl+d')
		preferencia= toolsMenu.Append(-1, 'Preferencias \tCtrl+p')
		helpMenu=wx.Menu()
		acerca=helpMenu.Append(-1, 'Acerca de ..   \tF1')
		menubar.Append(fileMenu , '&Archivo')
		menubar.Append(hablarMenu , '&Hablar')
		menubar.Append(toolsMenu , '&Herramientas')
		menubar.Append(helpMenu , '&Ayuda')
		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU, self.onquit, salir)
		self.Bind(wx.EVT_MENU, self.openFile,abrir)
		self.Bind(wx.EVT_MENU, self.saveComo,guardarComo)
		self.Bind(wx.EVT_MENU, self.conversion, iniciar)
		self.Bind(wx.EVT_MENU, self.saveAud, guardarAud)
		self.Bind(wx.EVT_MENU, self.saveFile, guardar)
		self.Bind(wx.EVT_MENU, self.closeFile,cerrar)
		self.Bind(wx.EVT_MENU,self.preference ,preferencia)
		self.Bind(wx.EVT_MENU,self.dictado ,dictado)
		self.Bind(wx.EVT_MENU,self.descarga ,descarga)
		self.Bind(wx.EVT_MENU,self.leer ,leer)
		#self.Bind(wx.EVT_MENU,self.pausa ,pausa)
		panel = wx.Panel(self)
		sz_principal =wx.BoxSizer(wx.VERTICAL)
		self.editor= wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=wx.Size(900,300))
		sz_principal.Add(self.editor, 1, wx.EXPAND)
		panel.SetSizer(sz_principal)
		self.Centre
		self.Show()

	def onquit(self, event):
		self.Close()
#abrir archivo
	def openFile(self, event):
		dlg = wx.FileDialog(self, "abrir", "", "", 'archivo de texto (*.txt)|*.txt| documento de word (*.docx)|*.docx| todos los archivos (*.*)|*.*')
		# style=wx.FD_SAVE
		#dlg = wx.DirDialog(self, "seleccione carpeta")
		if dlg.ShowModal() == wx.ID_OK:
			try:
				path= dlg.GetPath()
				f = open(path, "r", encoding="utf-8")
				txt = f.read()
				f.close()
				self.editor.SetValue(txt)
				self.name= dlg.GetPath() 
				self.SetTitle("ISA Text a Voice-"+self.name)
			except:
				wx.MessageBox("archivo no valido", "error")
		dlg.Destroy()

#guardar como 
	def saveComo(self, event):
		dlg = wx.FileDialog(self, "Guardar", "", "", 'archivo de texto (*.txt)|*.txt| documento de word (*.docx)|*.docx| todos los archivos (*.*)|*.*', style=wx.FD_SAVE)
		tx=self.editor.GetValue()
		if dlg.ShowModal() == wx.ID_OK:
			path= dlg.GetPath()
			f = open(path, "w", encoding="utf-8")
			txt = f.write(tx)
			f.close()
			self.name= dlg.GetPath() 
			self.SetTitle("ISA Text a Voice-"+self.name)
			dlg.Destroy()

#guardar archivo
	def saveFile(self, event):
		if hasattr(self, 'name'):
			f = open(self.name, "w", encoding="utf-8")
			tx=self.editor.GetValue()
			txt = f.write(tx)
			f.close()
			self.SetTitle("ISA Text a Voice   "+ self.name)
		else:
			self.saveComo(None)

#guardar archivo de audio
	def saveAud(self, event):	
		dlg = wx.FileDialog(self, "Guardar", "", "", 'archivo de audio (*.mp3)|*.mp3| archivo de audio wav (*.wav)|*.wav| todos los archivos (*.*)|*.*', style=wx.FD_SAVE)
		txt=self.editor.GetValue()
		if dlg.ShowModal() == wx.ID_OK:
			name= dlg.GetPath()
			speed=self.config.speed
			volum='0.'+self.config.volumen
			voi=self.config.voice
			voice_x=self.voice.index(voi)

			conversionText= ConversionText(txt, name,volum, speed,voice_x)
			conversionText.config_tts()
			conversionText.grabar_tts()

#dividir y convertir
#cerrar archivo
	def closeFile(self , event):
		self.editor.SetValue("")
		self.SetTitle("ISA Text a Voice ")



#configuración de preferencias
	def preference(self , event):
		dlgPref = Preference(self)
		if dlgPref.ShowModal() == wx.ID_OK:
			config= dlgPref.getConfig()
			voice= dlgPref.getVoice()
			sp =dlgPref.getSpeed()
			aud = dlgPref.getAudio()
			pt =dlgPref.getPath()
			vol=dlgPref.getVolumen()
			#actualiza preferencias  
			config.voice= voice
			config.speed= sp
			config.audio= aud
			config.path= pt
			config.volumen=vol

			guardarConfiguracion(config)

#dictado de voz"
	def dictado(self, event):
		texto=self.editor.GetValue()
		speak=Speak(texto)
		speak.dictando()
		sp=speak.getText()
#posicionar el cursor al final del textCtrl
		self.editor.SetValue(sp)
		self.editor.SetInsertionPointEnd() 

#abrir carpeta de descarga determinadas 
	def descarga(self , event):
		RUTA_CARPETA =self.config.path
		os.system(f'start {os.path.realpath(RUTA_CARPETA)}')



	def getText(self):
		return self.text.GetValue()

	def leer(self , event):
		txt=self.editor.GetValue()
		name= ""
		voi=self.config.voice
		voice_x=self.voice.index(voi)
		speed=self.config.speed
		volum=0.7
		conversionText= ConversionText(txt, name,volum, speed,voice_x)
		conversionText.config_tts()
		conversionText.escucha_previa()
		self.audio=conversionText


	def conversion(self, event):
		txt=self.editor.GetValue()
		try:
			archivo=os.path.basename(self.name)
			self.name, extension = os.path.splitext(archivo)
			self.Show(False)
			divConvert =DivConvert(self , txt , self.name)
		except:
			mj=wx.MessageBox("debe seleccionar archivo a dividir y convertir","error")



"""

			speed = speedString=='lento'
			# comparar es el proceso de convertir 2 valores en un valor booleano, si cumple o no la condición descripta.
			# en este caso verificamos si la variable speedString es igual al string 'lento'
			# si es el mismo valorse transforma en True, si no es False.
			conversionText= ConversionText(text, name,speed,lang,audio,path)
			#conversionText.load()
"""


