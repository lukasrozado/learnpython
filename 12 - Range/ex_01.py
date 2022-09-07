#Escreva um programa que imprima os numeros inteiros de 1 a 50. 
# Para multiplos de três imprima "Fizz" na frente do numero, e paraos 
# multiplos de cinco imprima "Buzz". Para numeros que são multiplos de 3 e 5 
# imprima "FizzBuzz"

for num in range(1,51):
    if num %3 == 0:
        print(num,"- Fizz")
    elif num %5 == 0:
        print(num,"- Buzz")
    if num %5 == 0 and num %3 == 0:
        print(num,"- FizzBuzz")