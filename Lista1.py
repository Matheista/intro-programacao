"""#1
N = int(input("digite numero:" ))

if N > 0:
    print("Positivo")
elif N <0:
    print("Negativo")

else:
    print("Neutro")
#2

N = int(input("Digite numero: "))

if N%2==0:
    print("par")

else:
    print("impar")
#3

N1 = int(input("digite o primeiro numero: "))
N2 = int(input("digite o segundo numero: "))
N3 = int(input("digite o terceiro numero: "))

    
if N1 > N2:

         if N1 > N3:           
             print(N1,"é o maior")
elif N3>N1:
         if N3>N2:
             print(N3,"é o maior")

else:
    print(N2,"é o maior")
#4



N = int(input("digite um numero: "))

if N%2 != 0:
    print("É impar")
else:
        print("Não é impar")

if N%3 == 0:
        print("é multiplo de 3")
else:
        print("Não é multiplo de 3")

if N//102 == 0:
        print("É divisor de 102")

else:
        print("Não é divisor de 102")

ela deseja oferecer um desconto de 10% para os
clientes que gastarem R$ 100 ou mais e pagarem em dinheiro.

Escreva um programa que
receba como entrada o valor do produto comprado e a forma de pagamento escolhida
(dinheiro ou cheque), calcule o desconto devido (caso necessário), e exiba o valor final a
ser pago.
        
#5

Valor = float(input("Digite valor do produto = "))
FormPag = input("Qual forma de pagamento? ")

if FormPag != "dinheiro" and FormPag != "cheque":
     print("Forma de pagamento inválida")

elif Valor >= 100 and FormPag == "dinheiro":
    desc = 100 - (Valor/10)
    print("R$",desc)


else:
    print("R$",Valor)

Passados seis meses, a loja de Natália teve um crescimento surpreendente e agora ela vai
aceitar pagamentos também com cartão. O cliente poderá escolher entre as funções
débito e crédito do cartão, e ainda parcelar sua compra em até 3 vezes na opção crédito.
Modifique o programa anterior para que as novas formas de pagamento sejam
consideradas e, além do valor final a ser pago, seja exibido o valor de cada parcela nas
compras com cartão de crédito.
Dados de entrada para teste Resultad
"""
#6


Valor = float(input("Digite valor do produto = "))
FormPag = input("Qual forma de pagamento? ")

if FormPag != "dinheiro" and FormPag != "cheque" and FormPag != "cartão":
     print("Forma de pagamento inválida")

if FormPag == "cartão":
    cartão=input("débito ou crédito? ")
    if cartão != "debito" and cartão != "crédito":
        print("Tipo de cartão inválido")
    elif cartão == "crédito":
        vezes = int(input("quantas vezes? (MAX=3) "))
        if vezes > 3 or vezes < 1:
                    print("Quantidade de parcelas inválida")

          
        else:
            print("R$", Valor)
            resultado = Valor/vezes
            print(vezes,"Parcelas de %.2f" % resultado)

elif Valor >= 100 and FormPag == "dinheiro":
    desc = 100 - (Valor/10)
    print("R$",desc)


else:
    print("R$",Valor)



    
