#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import cv2


# Função copiada de digits.py do profº Luiz Eduardo.
def load_images(path_images):
	archives = os.listdir(path_images)
	images = []
	arq = open('digits/files.txt')
	lines = arq.readlines()
	for line in lines:
		aux = line.split('/')[1]
		image_name = aux.split(' ')[0]
		label = line.split(' ')[1]
		label = label.split('\n')
		
		for archive in archives:
			if archive == image_name:
				image = cv2.imread(path_images +'/'+ archive, 0)
				images.append(image)

	return images

histogramas = []

img = load_images('digits/data')

hog = cv2.HOGDescriptor()
winStride = (64,128)
padding = (64,128)

for x in range(len(img)):
	histogramas.append(hog.compute(img[1],winStride, padding))
