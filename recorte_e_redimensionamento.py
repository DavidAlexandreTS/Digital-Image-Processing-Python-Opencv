import cv2

imagem = cv2.imread("ft4.jpg")

#criando uma imagem com os pixels só dos intervalos selecionados
imagemRecortada = imagem[100:400, 50:400]

#cv2.imshow("Undead WoW", imagem)
#cv2.imshow("Undead Recortada", imagemRecortada)
#cv2.waitKey(0)

#pegando largura e altura
largura = imagem.shape[1]
altura = imagem.shape[0]

#calculando a proporção para redimensionar da forma correta
proporcao = float(altura/largura)

larguraNova = 400
alturaNova = int(larguraNova*proporcao)

#diminuindo a imagem e mantendo a sua forma
imagem = cv2.resize(imagem, (larguraNova, alturaNova))

#cv2.imshow("Undead Redimensionada", imagem)
#cv2.waitKey(0)

#para rotacionar a imagem =D
#da pra rodar em torno dos 2 eixos aqui ta no x, mas pode rodar nos 2
#imagemRotacionada = imagem[:, ::-1]
#cv2.imshow("Imagem", imagem)
cv2.imwrite(r'C:\Users\David\Desktop\Digital-Image-Processing\imt4.jpg',imagem)
#cv2.imshow("Undead rodada", imagemRotacionada)
cv2.waitKey(0)