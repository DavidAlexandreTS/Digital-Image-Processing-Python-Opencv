import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread("ft4.jpg")

b_list = []
g_list = []
r_list = []

for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        #print(imagem[i][j])
        b_list.append(imagem[i][j][0])
        g_list.append(imagem[i][j][1])
        r_list.append(imagem[i][j][2])


#pega os valores unicos da lista
b_list_unique = sorted(set(b_list))
g_list_unique = sorted(set(g_list))
r_list_unique = sorted(set(r_list))

b_count = []
g_count = []
r_count = []

for i in range(0, len(b_list_unique)):
    somatorio = 0
    for j in range(0, len(b_list)):
        if b_list_unique[i] == b_list[j]:
            somatorio += 1

    b_count.append(somatorio)

for i in range(0, len(g_list_unique)):
    somatorio = 0
    for j in range(0, len(g_list)):
        if g_list_unique[i] == g_list[j]:
            somatorio += 1

    g_count.append(somatorio)

for i in range(0, len(r_list_unique)):
    somatorio = 0
    for j in range(0, len(r_list)):
        if r_list_unique[i] == r_list[j]:
            somatorio += 1

    r_count.append(somatorio)

#print(b_count)
plt.plot(b_count, color = 'blue')
plt.plot(g_count, color = 'green')
plt.plot(r_count, color = 'red')
plt.show()