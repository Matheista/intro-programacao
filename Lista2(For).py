"""Rafaela tem uma loja de antiguidade e decidiu avaliar quanto vale o seu estoque de 1500
peças. Escreva um programa que receba como entrada a descrição, o valor e o ano de cada item presente na loja"""
#A quantidade de items produzidos antes de 1827
#o valor médio dos intens
# a descrição  e o ano do objeto mais valiosos

"""n=int(input("Qual a Quantidade de Peças"))
antesAno=0
valioso=0
valorTotal=0
desValor=0
anoValor=0
for i in range(n):
    des=input("Qual o produto? ")
    valor=float(input("Qual o valor? "))
    ano=int(input("Qual ano? "))


    if ano < 1827:
        antesAno+=1
    
    if valioso < valor:
        valioso=valor
        desValor=des
        anoValor=ano
        
    valorTotal+=valor


media=(valorTotal/n)

print("a média é %.2f R$" %  (media))
print("Quantidade de produtos antes de 1827:",antesAno)
print("O Produto mais caro é" ,desValor,"do ano de ",anoValor)"""

"""2. Uma lavanderia oferece ao cliente duas opções de cobrança: R$ 7,00 por peça de roupa ou R$
5,00 por quilo. Caso a lavagem seja a seco, é acrescentada uma taxa de R$ 3,50. Escreva um
programa que receba como entrada os dados dos últimos 50 pedidos de lavagem e exiba o valor
a ser pago por cada um, o total arrecadado pela lavanderia e a quantidade de lavagens a seco
solicitadas."""

"""pedidos = int(input("Quantos pedidos? "))
peca = 7.00
quilo = 5.00
seco=3.50
Total=0
contSeco=0

for i in range(pedidos):
    FormC=str.lower(input("Qual forma de cobrança ? \n>Peça \n>Peso \n>"))
    if FormC == "peça":
        QntPeca=int(input("Quantidade de Peças? "))
        PrecoPeca=QntPeca*peca
        print("Valor do pedido",PrecoPeca)
        Total+=PrecoPeca
    elif FormC == "peso":
        QntQuilo=int(input("Quantos Quilos? "))
        PrecQuilo=QntQuilo*quilo
        print("Valor do pedido",PrecQuilo)
        Total+=PrecQuilo
    lavaSeco=str.lower(input("Lavagem à Seco ?"))
    if lavaSeco == "sim":
        Total+=seco
        contSeco+=1

print("Total Arrecadado %.2f R$" % Total,"\nQuantidades de lavagens à seco =",contSeco)
"""






"""3. Escreva um programa para receber como entrada dois números e exibir a quantidade de
múltiplos de 4 entre eles (os extremos do intervalo não devem ser considerados)."""

"""n1 = int(input("Digite o primeiro número? "))
n2 = int(input("Digite o segundo número? "))
count=0
for i in range (n1+1,n2):
    if i%4 == 0:
        count+=1

print(count,"Múltiplos")"""


"""4. Uma grande loja de produtos para o lar deseja fazer um levantamento de todas as 7000 vendas
realizadas nos últimos meses para descobrir as preferências de seus clientes. São vendidos
móveis nas cores marfim e branco, e eletrodomésticos das marcas Brastemp e Electrolux, além
de objetos de decoração em geral. Escreva um programa que receba como entrada os dados das
vendas realizadas (os dados variam de acordo com o tipo de produto) e exiba ao final:
 o percentual de móveis de cada cor vendidos (Dica: para saber o percentual, é preciso analisar
a quantidade em relação ao total)
 a marca de eletrodomésticos mais vendida
 o preço médio dos artigos de decoração"""



"""
n = int(input("Qual a quantidade de itens? "))
CountB=0
CountM=0
MarcaB=0
MarcaE=0
PrecoT=0
CountP=0
for i in range(n):
    
    item=str.lower(input("Qual o objeto? "))

    if item == "móvel":
        cor=str.lower(input("Qual cor? \n>Branco \n>Marfim \n>"))
        if cor == "branco":
            CountB+=1            
        elif cor == "marfim":
            CountM+=1   
        
    elif item == "eletrodoméstico":
        marca=str.lower(input("Qual marca? \n>Brastemp  \n>Electrolux \n>"))
        if marca == "brastemp":
            MarcaB+=1
        else:
            MarcaE+=1
            
    else:
        preco=int(input("Qual preço do produto? R$"))
        PrecoT+=preco
        CountP+=1

if CountB + CountM > 0:
    pMarfim = 100*CountM//(CountM+CountB)
    pBranco = 100 - pMarfim
    print("Percentuais =",pMarfim,"%Marfim",pBranco,"%Branco")

else:
    print("Nenhum móvel vendido")


if MarcaB+MarcaE>0:
    if MarcaB > MarcaE:
        print("Marca mais vendida é Brastemp")
    elif MarcaB > MarcaE:
         print("Marca mais vendida é Eletrolux")
    else:
        ("Ambas as marcas foram vendidas igualmente")
else:
    print("Nenhum eletrodoméstico vendido")



if PrecoT == 0:
    print("Nenhum objeto de decoração vendido")
else:
    print("O preço médio de decoração é %.0f R$" %(PrecoT/CountP))


"""



pessoas=int(input("Quantas pessoas? "))
opBom=0
opReRu=0
opCount=0
Pes30=0
MaiorIdade=0
for i in range(pessoas):
    idade=int(input("Qual sua idade? "))
    opniao=str.lower(input("Qual sua opnião? \nRuim \nRegular \nBom \nExcelente \n>"))
    if opniao == "bom":
        opBom+=idade
        opCount+=1
        opMedia=(opBom//opCount)
        
    if opniao == "regular" or opniao=="ruim":
        opReRu+=1
    
    if idade >30 and opniao == "excelente":
        Pes30+=1
        

    if idade>MaiorIdade:
        MaiorIdade=idade    

print("Média de idade Bom =",opMedia,
      "\nQuantidade respostas Ruim/Regular =",opReRu,
      "\nPessoas acima de 30 Excelente =",Pes30,
      "\nMaior idade =",MaiorIdade)
    




























