import cv2

imagem = cv2.imread("shelee.jpg")

#pintando os pixels da imagem de branco
imagem[0:20, :] = (255, 255, 255)

#variavel para representar a cor branca
#nota: estamos usando tupla () porque é imutável
waite = (255, 255, 255)

#for para percorrer a matriz que representa a imagem
for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        #pintar o pixel de branco
        #imagem[i][j] = waite

        #checando se um pixel tem 255 de azul em seu canal de cores
        #e em caso positivo, pintando ele de branco
        if imagem[i][j][0] == 255:
            imagem[i][j] = waite

#selecionando uma fonta no OpenCV
fonte = cv2.FONT_HERSHEY_COMPLEX

#colocando na imagem o texto
#parametros: imagem, texto que vai la, posicao do texto, esilo da fonte
#meio que o tamanho, cor, espessura, e por fim um ngc pra deixar mais bonitinho
cv2.putText(imagem, "Caio is homo", (100, 550), fonte, 2, waite, 2, cv2.LINE_AA)

print(imagem.shape)

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)