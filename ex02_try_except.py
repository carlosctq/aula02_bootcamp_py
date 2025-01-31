
    # Exemplo que causa TypeError

# try:
#     resultado = len(3)
#     print(resultado)
# except TypeError as e:
#     print(e)
# else:
#     print("tudo ocorreu bem")
# finally:
#     print("o importante e participar")  

# numero = int(input("Insira um numero :"))
# if isinstance(numero,int ):
#     print("A variável é um inteiro.")
# except ValueError:
#     print("A variável não é um inteiro.")


entrada = input("Insira um número: ")

try:
    numero = int(entrada)
    if isinstance(numero, int):
        print("A variável é um inteiro.")
except ValueError:
    print("A variável não é um inteiro.")

