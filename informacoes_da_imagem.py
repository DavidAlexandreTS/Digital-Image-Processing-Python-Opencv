import cv2

imagem = cv2.imread("mira.png")

#for que percorre cada linha e coluna da imagem e mostra informações
#sobre cada um dos pixels
for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        print(imagem[i][j])

#numero de linhas da matriz que representa a imagem
#ou numero de pixels na vertical
print(imagem.shape[0])

#numero de colunas da matriz que representa a imagem
#ou numero de pixels na horizontal
print(imagem.shape[1])

#numero de canais de cores presentes na imagem
print(imagem.shape[2])