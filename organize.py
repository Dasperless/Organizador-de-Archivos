#Documentation is avalible on http://www.visionprogrammer.com/2020/05/python-script-for-organizing-files.html

from os import listdir
from os.path import isfile, join
import os
import shutil

def getPath():
	file = open("path.txt", "r")
	strPath = file.read()
	file.close()
	return strPath

def file_organizer(mypath):
	'''
	A function to sort the files in a download folder
	into their respective categories
	'''
	files  =  [f for f in listdir(mypath) if isfile(join(mypath, f))]
	file_type_variation_list  =  []
	filetype_folder_dict = {}

	for file in files:
		filenamebrake = file.split('.')
		filetype = filenamebrake [len(filenamebrake)-1]

		if filetype not in file_type_variation_list:
			file_type_variation_list.append(filetype)
			new_folder_name = mypath + '/' + filetype + '_folder'
			filetype_folder_dict[str(filetype)] = str(new_folder_name)
			
			if os.path.isdir(new_folder_name) == True:  #folder exists
				continue
			else:
				os.mkdir(new_folder_name)

	for file in files:
		src_path = mypath + '/' + file
		filenamebrake = file.split('.')
		filetype = filenamebrake[len(filenamebrake)-1]

		if filetype in filetype_folder_dict.keys():
			dest_path = filetype_folder_dict[str(filetype)]

			#Intenta mover el archivo, si ya existe, continua y no lo mueve.
			try:									
				shutil.move(src_path, dest_path)
			except:
				continue

	print("Organización de archivos completa " + str(mypath))

opcionIncorrecta = True
mypath = ""
while (opcionIncorrecta):
	print ("[1]: Ordenar directorio específico. \n[2]: Ordenar directorio incrustado en el codigo\n")
	opcion = input(">>")

	if opcion == "1":
		mypath = str(input("Ingrese la ruta: "))		#Descomentar esto si desea ordenar un directorio especifico.
		opcionIncorrecta = False

	if opcion == "2":
		mypath = getPath()	#Path de mi computadora.
		opcionIncorrecta = False
	

file_organizer(mypath)
