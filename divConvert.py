import wx
from modelo.conversionText import ConversionText
import os
from pathlib import Path 
from modelo.divText import DivText
from funciones import cargarConfiguracion
from voces import voices_list
from os import mkdir

class  DivConvert(wx.Frame):
	def __init__(self,parent,  texto ,name , *args ,**qwargs):
		super().__init__(parent , *args ,**qwargs)
		self.parent=parent
		self.texto=texto
		self.name = name
		self.voice = voices_list()

		self.audio=['mp3','wav']
		self.config = cargarConfiguracion()
		audio = self.config.audio

		path = self.config.path
		self.SetTitle('Divide el texto  y lo convierte en audio  ')


		panel=wx.Panel(self)		
		wx.StaticText(panel,-1,label='Carpeta de archivo de salida:')
		self.path = wx.TextCtrl(panel)
		self.path.SetValue(path)
		btnCarpeta = wx.Button(panel , -1 , 'examinar..')
		wx.StaticText(panel,-1,label='Formato de archivo de audio:')
		idAud =self.audio.index(audio)
		self.lbAudio=wx.ListBox(panel, -1, choices=self.audio)
		self.lbAudio.SetSelection(idAud)
		self.cb1= wx.CheckBox(panel ,-1 , label='crear sub carpeta ')
		#self.cb1.SetValue(True)
		wx.StaticText(panel,-1,label='nombre de archivo de salida:')
		self.name_salida= wx.TextCtrl(panel) 
		self.name_salida.SetValue(self.name)
		wx.StaticText(panel,-1,label='Dividir por :')
		self.marca = wx.TextCtrl(panel)
		btnProbar = wx.Button(panel , -1 , 'Probar..')
		btnOk= wx.Button(panel, wx.ID_OK,'Dividir y Convertir')
		btnCancel= wx.Button(panel, wx.ID_CANCEL,'Cancelar')
		self.Centre
		self.Show()
		btnCarpeta.Bind(wx.EVT_BUTTON,self.folder)
		btnProbar.Bind(wx.EVT_BUTTON, self.probar)
		btnOk.Bind(wx.EVT_BUTTON, self.aceptar)
		self.Bind(wx.EVT_BUTTON, self.cancelar)

#seleccionar carpeta de descarga
	def folder(self , event):
		dlg = wx.DirDialog(self, "seleccione carpeta")
		if dlg.ShowModal() == wx.ID_OK:
			pathDir= dlg.GetPath()
			self.path.SetValue(pathDir)
		dlg.Destroy
#cantidad de partes que se divide el texto
	def probar(self, event):
		marca=self.marca.GetValue()

		divText = DivText(self.texto , marca)
		long,ltx=divText.div_txt()
		divText.div_txt()
		dialogo = wx.MessageDialog(self, 'cantidad aproximada  de archivos {}'.format(long),'mensaje ')
		dialogo.ShowModal()


	def getPathCompleto(self):
		idA=self.lbAudio.GetSelection()
		extension=self.audio[idA]
		ruta=self.path.GetValue()
		nombre_archivo=self.name.GetValue()
		archivo=nombre_archivo+"."+extension
		return ruta,archivo 

	def cancelar(self , event):
		self.parent.Show(True)
		self.Close()

	def aceptar(self , event):
	#generar ruta , archivo y extension.
		idA=self.lbAudio.GetSelection()
		ext=self.audio[idA]
		ruta=self.path.GetValue()
		name_file = self.name_salida.GetValue()
		cb_sc= self.cb1.GetValue()#valor del check box
		#si el checkboxes true , se crea la carpeta 
		if cb_sc:
			name_sc=self.name_salida.GetValue()
			dir=self.path.GetValue()
			dir=self.path.GetValue()
			ruta = Path(dir,name_sc)
			mkdir(ruta)

		#divide el texto
		marca=self.marca.GetValue()
		divText = DivText(self.texto , marca)
		long,ltx=divText.div_txt()
		divText.div_txt()
		#conversion del texto 
		speed=self.config.speed
		volum='0.'+self.config.volumen
		#volum=0.7
		voi=self.config.voice
		voice_x=self.voice.index(voi)
		for x , texto in enumerate (ltx):
			n_pista = name_file+str(x)+"."+ext
			name= Path(ruta,n_pista)
			conversionText= ConversionText(texto, str(name),volum, speed,voice_x)
			conversionText.config_tts()
			conversionText.grabar_tts()


		self.parent.Show(True)
		self.Close()