import numpy as np  
import cv2


def showImage(img):

    from matplotlib import pyplot as plt #modulo 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #TROCANDO AS CORES
    plt.imshow(img) #constroe a janela gráfica
    plt.show() #mostra a janela gráfica
# RGB as cores são vermelho, verde e azul #opnecv é uma matriz 3D que representa toda imagem BGR (AZUL,VERDE, VERM) matiplot entendi 
def getColor(img, x, y):
    return img.item(y, x, 0), img.item( y, x, 1), img.item(y, x, 2)

def setColor(img, x, y, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)

    return img
    

def main():
    obj_img = cv2.imread("img/golden.jpg") # irá fazer a leitura da imagem
    altura, largura, canais_de_cor = obj_img.shape 
    print("Dimensões da Imagem: " + str(largura) + "x" + str(altura))
    print("Canais de Cor: ", canais_de_cor) #mostra as dimensoes da imagem
    
    for y in range(0, altura):
        for x in range(0, largura):
             #print("["+ str(x) + "," + str(y) +"] = "+ str(obj_img[y][x]))
            #input()
    

            azul, verde, vermelho = getColor (obj_img, x, y)
            obj_img = setColor(obj_img, x, y, verde, vermelho, vermelho)

    #cv2.imwrite("golden_modificado.png", obj_img)
    #showImage(obj_img)

main()




