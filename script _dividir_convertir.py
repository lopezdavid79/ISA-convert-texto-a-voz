from pathlib import Path 
from modelo.conversionText import ConversionText
from modelo.divText import DivText


def convertir(texto,marca):
#divide el texto
	divText = DivText(texto , marca)
	long,ltx=divText.div_txt()
	divText.div_txt()
		#conversion del texto 
	speed=140
		#volum='0.'+self.config.volumen
	volum=0.7
	voice_x=0
	name_file='davidPrueba'
	ruta='F:\simple'
	ext='mp3'

	for x , texto in enumerate (ltx):
		n_pista = name_file+str(x)+"."+ext
		name= Path(ruta,n_pista)
		print(type(str(name)))
		conversionText= ConversionText(texto, str(name),volum, speed,voice_x)
		conversionText.config_tts()
		conversionText.grabar_tts()

print('dividir y convertir  texto ')
texto='hola <m chau'
marca='<m'
convertir(texto, marca)
print('	proceso terminado')