#Escreva uma função que calcula o volume de uma esfera dado seu raio 
# A formula é V = 4/3nr³
# Obs sinta a vontade para usar pi como 3,1416. Porém se vocês mais precisão, importe a biblioteca math e use pi como math.pi

import math

def calculo(rad):
    return (rad**3) * (4/3) * math.pi

print(calculo(2))