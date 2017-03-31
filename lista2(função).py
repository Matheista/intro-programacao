import BibGaleriaArte
#1. Escreva um programa que exiba um menu para o usuário e permita que ele escolha que tipo de
#consulta deseja fazer. O programa deverá também solicitar ao usuário os dados necessários para
#fazer a pesquisa escolhida.

"""print("Menu\n QualTipo de Consulta deseja?\n>Consulta por Preço\n>Consulta por Artista\n>Consulta por Quantidade de Obras\n>Consulta por Tipo de Obra")
consulta=str.lower(input())


if consulta == "consulta por preço":
    consulta=BibGaleriaArte.consultaPreco(500)
    
elif consulta == "consulta por artista":
    consulta=BibGaleriaArte.consultaArtista("Leonardo")
    
elif consulta == "consulta por quantidade de obras":
    consulta=BibGaleriaArte.consultaQuantObras(40)

elif consulta == "consulta por tipo de obra":
    consulta=BibGaleriaArte.consultaTipo("escultura")

"""

#2. Escreva um programa que receba como entrada os nomes de 60 obras da galeria e exiba o valor
#total das obras do artista Leonardo Resende.

"""
countR=0
for i in range(59):
    obra=(input("Nome da obra\n"))
    resende=str.lower(input("essa obra é de Leonardo Resende?\nSim \nNão \n"))
    if resende =="sim":
        countR+=1             
    else:
        BibGaleriaArte.consultaArtista(input("Qual o nome do Artista?"),obra)  

BibGaleriaArte.consultaQuantObras(countR,"Leonardo Resende")"""

#3. Escreva um programa que receba como entrada os nomes de 50 obras da galeria e exiba uma
#mensagem informando se ela dispõe de uma quantidade maior de quadros ou de esculturas."""

"""

contQE=0
contE=0
contQ=0
for i in range (9):
    if contQE%2==0:
        x="escultura"
        contE+=1        
    else:
        x="quadro"
        contQ+=1
    z=BibGaleriaArte.consultaTipo(x)
    contQE+=1
   
if contE>contQ:
    print("A galeria dispõe de uma quantidade maior de %.0f esculturas" % contE)
elif contQ>contE:
    print("A galeria dispõe de uma quantidade maior de %.0f de quadros" % contQE)
        
else:
    print("A galeria dispõe de uma mesma  quantidade de números de  %.0f esculturas e quadros" % contE)

"""
#4. Escreva um programa que receba como entrada os nomes de 30 obras e exiba quantas esculturas
#de Adélia Machado existem na galeria."""

"""AdeliaCont=0
obraE=0
AdeliaT=0
for i in range(29):
    if obraE%2==0:
        obra=str.lower(input("Qual obra\n"))
        x="escultura"
        BibGaleriaArte.consultaTipo(x,obra)
    Artista=str.lower(input("Qual artista?\n"))
    if Artista=="adélia machado"or Artista=="adelia machado" and x =="escultura":
        AdeliaCont=+1
        AdeliaT+=AdeliaCont
z=BibGaleriaArte.consultaQuantObras(AdeliaCont,"Adélia Machado")"""

#5. Escreva um programa que receba como entrada os nomes de 80 obras e exiba o valor médio dos
#quadros da galeria.
"""preco=0
obraQ=0
precoT=0
for i in range(3):
    if obraQ%2==0:
        x="quadro"
        preco+=11
    obra=str.lower(input("Qual obra\n"))
    BibGaleriaArte.consultaPreco(preco,obra)
    if x=="quadro":
        preco+=10
        precoT+=preco
        obraQ+=1
print("A galeria possuí o valor da média %.2f e o total de" % (preco/obraQ), precoT)"""
