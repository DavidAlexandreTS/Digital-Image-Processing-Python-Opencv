import cv2

imagem = cv2.imread("mira.png")

for i in range(0, imagem.shape[0], 15):
    for j in range(0, imagem.shape[1], 15):
        imagem[i:i + 3, j:j + 3] = (255, 255, 255)

#suavizacao pela media aritmetica, onde os pixels são suavizados de acordo com a media
#aritmetica dos valores de acordo com o tamanho do kernel
suave = cv2.blur(imagem, (13, 13))
cv2.imshow("Mirajane Fairy Tail", imagem)
cv2.imshow("Mirajane Fairy Tail Suavizada", suave)
cv2.waitKey(0)

#aqui, o calculo é pela mediana, o que nesse caso vai resultar numa qualidade melhor na remoção do ruido
#pois estamos pegando valores que ja estao nos pixels da imagem, nao "criando novos" como fazemos com o uso
#da media aritmetica
suave_mediana = cv2.medianBlur(imagem, 5)
suave_mediana2 = cv2.medianBlur(imagem, 11)
cv2.imshow("Original", imagem)
cv2.imshow("Suavizada com tamanho 5", suave_mediana)
cv2.imshow("Suavizada com tamanho 11", suave_mediana2)
cv2.waitKey(0)