
class DivText():
	def __init__(self , texto , marca , *args , **qwargs):
		self.texto=texto
		self.marca = marca
		
		#metodo para obtener lobngitud y división de texto 
	def div_txt(self): 
		ltx= self.texto.split(self.marca)
		long=len(ltx)
		return long,ltx