import cv2 as cv
import numpy as np
import os
from imutils import paths

#Caminho da pasta onde estão as imagens
folder = r'C:\Users\Vinícius\Pictures\Memes'

#Cria uma lista com o diretório de cada imagem
images = list(paths.list_images(folder))
qtd_imgs = len(images)

#Cria uma lista com o diretório das imagens repetidas
repeated_img = []

#Definindo as variáveis de iteração
i = 0 
j = 0 
# i --> imagem que será usada para comparar com as demais
# j --> imagens que serão usadas para comparação
# A imagem "i" será comparada com todas as imagens da pasta que serão representadas por "j"

#O range é "qtd_imgs - 1" para que não ocorra um List Index Out of Range, pois o id na lista começa no zero.
for i in range(qtd_imgs-1): 

	print(f'i = {i}')

	path_img_base = images[i]

	#Lê a imagem usando imcode para conseguir ler diretórios que possuem caracteres com codificação utf-8
	img_base = cv.imdecode(np.fromfile(path_img_base, dtype=np.uint8), cv.IMREAD_UNCHANGED)

	#Recebe o id da próxima imagem
	prox = i + 1
	
	#O número de imagens que faltam ser comparadas diminui a medida que o "i" avança, então serão necessárias menos iterações
	for j in range(qtd_imgs-(i+1)):
	 
		print(f'prox = {prox}')
		
		path_prox_img = images[prox]

		#Lê a próxima imagem usando imcode para conseguir ler diretórios que possuem caracteres com codificação utf-8
		prox_img = cv.imdecode(np.fromfile(path_prox_img, dtype=np.uint8), cv.IMREAD_UNCHANGED)

		#Compara os arrays da img_base e da prox_img, se as imagens forem iguais a prox_img é adicionada na lista de imagens repetidas
		if np.array_equal(img_base, prox_img):
			
			repeated_img.append(path_prox_img)
			

		j+=1
		prox+=1

	print('-------------------')

	i+=1

#Remove diretórios repetidos na lista
repeated_img = sorted(set(repeated_img))

#Apaga as imagens repetidas na pasta
for img in repeated_img:

	print(img)
	try:
		os.remove(img)
	except FileNotFoundError as e:
		print(f'{img} já foi removida. Erro: {e}')

