# Escreva um prgrama que identifique se um triangulo é valido ou não. 
# Para um triangulo ser valido a soma de um de seus dois lados tem que ser 
# sempre maior ou igual ao terceiro lado, caso não seja, o triangulo é invalido.
# Considere esses dados para o seu codigo:

a = 3 
b = 6
c = 9

if (a+b) >= c and (b+c) >= a and (a+c) >= b:
    print("Triangulo válido")
else:
    print("Triângulo inválido")

