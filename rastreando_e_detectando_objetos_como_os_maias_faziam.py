import cv2
import numpy as np

azulEscuro = np.array([100, 67, 0], dtype = "uint8")
azulClaro = np.array([255, 128, 50], dtype = "uint8")

camera = cv2.VideoCapture(0)

while True:
    #camera = cv2.VideoCapture(0)
    (sucesso, frame) = camera.read()

    if not sucesso:
        break

    #obj vai ser uma imagem toda preta, mas que vai pintar de branco um objeto que aparecer na tela e que tiver cores
    #no range definido por essas duas variaveis(praticamente qualquer azul)
    obj = cv2.inRange(frame, azulEscuro, azulClaro)

    #pega os contornos
    (cnts, _) = cv2.findContours(obj.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) > 0:
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 255), 2)

    cv2.imshow("Camera do David", frame)
    cv2.imshow("Camera do David azulfobica", obj)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()