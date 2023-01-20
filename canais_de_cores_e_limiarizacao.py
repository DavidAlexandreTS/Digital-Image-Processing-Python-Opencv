import cv2

#Cores
imagem = cv2.imread("malf.jpg")

(b, g, r) = cv2.split(imagem)

#imagem em tons de cinza porque só tem um canal de cores
cv2.imshow("Imagem Azul", b)
cv2.imshow("Imagem Verde", g)
cv2.imshow("Imagem Vermelha", r)

cv2.imshow("Imagem Original", imagem)
cv2.waitKey(0)

#Limiarização

#percorrendo a imagem e deixando TODOS os seus pixels pretos
for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        imagem[i][j] = (0, 0, 0)

fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem, '255', (15, 65), fonte, 2, (255, 255, 255), 2)
cv2.putText(imagem, '70', (115, 65), fonte, 2, (70, 70, 70), 2)
cv2.putText(imagem, '100', (215, 65), fonte, 2, (100, 100, 100), 2)
cv2.putText(imagem, '1', (315, 65), fonte, 2, (1, 1, 1), 2)

cv2.imshow("Imagem com os coiso escrita", imagem)
cv2.waitKey(0)

#preto pra branco
for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        if imagem[i][j][0] == 0:#poderia ser imagem[i][j][0] != 0: para visualizar todos os numeros, pois o resto da img é preta e tem valor = 0
            imagem[i][j] = (255, 255, 255)

cv2.imshow("Imagem com os coiso branca", imagem)
cv2.waitKey(0)