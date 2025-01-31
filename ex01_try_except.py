try:
    primeiro_numero = int(input('Digite um numero inteiro: '))
    segundo_numero = int(input('Digite outro  numero inteiro: '))
    resultado = primeiro_numero // segundo_numero
    print(resultado)
except ZeroDivisionError:
    print('Você dividiu zero por zero')
except:
    print("Você cometeu um erro")

