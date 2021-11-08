import wx
import os
from modelo.divText import DivText
from funciones import cargarConfiguracion
from voces import voices_list

class  DivConvert(wx.Dialog):
	def __init__(self, *args ,**qwargs):
		super().__init__( *args ,**qwargs)
		self.config = cargarConfiguracion()
		self.audio=['mp3','wav']
		path = self.config.path
		self.SetTitle('Divide el texto  y lo convierte en audio  ')
		
		panel=wx.Panel(self)
		
		wx.StaticText(panel,-1,label='Carpeta de archivo de salida:')
		self.path = wx.TextCtrl(panel)
		self.path.SetValue(path)
		btnCarpeta = wx.Button(panel , -1 , 'examinar..')
		wx.StaticText(panel,-1,label='Formato de archivo de audio:')
		self.lbAudio=wx.ListBox(panel, -1, choices=self.audio)
		self.cb1= wx.CheckBox(panel ,-1 , label='crear sub carpeta ')
		#self.cb1.SetValue(True)
		wx.StaticText(panel,-1,label='nombre de archivo de salida:')
		self.name= wx.TextCtrl(panel) 
		wx.StaticText(panel,-1,label='Dividir por :')
		self.marca = wx.TextCtrl(panel)
		btnProbar = wx.Button(panel , -1 , 'Probar..')
		btnOk= wx.Button(panel, wx.ID_OK,'Dividir y Convertir')
		btnCancel= wx.Button(panel, wx.ID_CANCEL,'Cancelar')
		btnCarpeta.Bind(wx.EVT_BUTTON,self.folder)
		btnProbar.Bind(wx.EVT_BUTTON, self.probar)
	def getFilename(self):
		return self.name.GetValue()
	def getSpeed(self):
		id=self.lbSpeed.GetSelection()
		return self.speed[id]


#seleccionar carpeta de descarga
	def folder(self , event):
		dlg = wx.DirDialog(self, "seleccione carpeta")
		if dlg.ShowModal() == wx.ID_OK:
			pathDir= dlg.GetPath()
			self.path.SetValue(pathDir)
		dlg.Destroy
#cantidad de partes que se divide el texto
	def probar(self, event):
		divText = DivText(text, marca)
		divText.div_txt()


	def cargar_nombre(self,name):
		archivo=os.path.basename(name)
		nombre, extension = os.path.splitext(archivo)
		self.name.SetValue(nombre)


	def getMarca(self):
		return self.marca.GetValue()
	def getCb1(self):
		return self.cb1.GetValue()

	def getPath(self):
		return self.path.GetValue()
	def getPathCompleto(self):
		idA=self.lbAudio.GetSelection()
		extension=self.audio[idA]
		ruta=self.path.GetValue()
		nombre_archivo=self.name.GetValue()
		archivo=nombre_archivo+"."+extension
		return ruta,archivo 
