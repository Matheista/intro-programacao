"""#a
rendaAnual = float (input())

if (rendaAnual <= 12000):
 imposto = 0
elif (rendaAnual > 60000):
 imposto = rendaAnual*0.07
else:                         fazia uma verificação por causa de dois if's
 imposto = rendaAnual*0.03
print(imposto)"""

"""#b
altura = float (input())
if (altura <= 1.40):
 print("Estatura Baixa")
else:
 if (altura < 1.65):
                                       Faltou a indentação 
     print("Estatura Mediana")
 else:
     print("Estatura Alta")
"""
"""#c
a = int (input())
b = int (input())                           faltou o else no final 
c = int (input())
if (a > b) and (a > c):
 print(a)

elif (b > a) and (b > c):
 print(b)
else:
 print(c)"""
"""PrecoGasol = 2.53
PrecoEtan = 2.09
PrecoDies = 1.92


Combustivel = str.lower(input("qual tipo de combustível? "))
Valor = float(input("Qual valor em dinheiro? "))


          

if Combustivel == "etanol": 
    Total = Valor/PrecoEtan
    if Total > 30:
        print("ganhou uma troca de %.2f" % Total)
    else:
         print(" Não ganhou uma troca de %.2f" % Total)
        
                
elif Combustivel == "gasolina":
    Total = Valor/PrecoGasol
    print("Não ganhou uma troca de %.2f" % Total)
else:
    Total = Valor/PrecoDies
    print("Não ganhou uma troca de %.2f" % Total)"""

"""3. A viação Rapidinho cobra R$ 350 pelo aluguel de ônibus (capacidade: 42 pessoas) e R$
200 por van (capacidade 20 pessoas). Escreva um programa que receba como entrada a
quantidade de pessoas de uma excursão e exiba a quantidade de ônibus e vans que
deverão ser alugados e o valor a ser pago por cada pessoa da excursão, sabendo que:
 A escolha entre alugar ônibus e vans dependerá da quantidade de pessoas, mas a
preferência é que sejam preenchidos primeiro os ônibus, e depois as vans
necessárias.
 A despesa geral será dividida igualmente por todos os participantes, não
importando quem irá de ônibus ou de van."""

"""
QntPessoas = int(input("Quantas Pessoas? "))

Bus = 350
Van = 200

CpBus=42
CpVan=20

NBus=0
NVan=0

NBus=QntPessoas // CpBus
Sobra=QntPessoas % CpBus

NVan=Sobra // CpVan
SobraVan=Sobra % CpVan

if SobraVan > 0:
    NVan+=1

Custo = (NVan*Van +NBus*Bus)/QntPessoas
if NVan >=1:
    print(NVan,"van(s)")
if NBus >=1:
     print(NBus,"Onibus")
print( "%.2f" % Custo,"Por Pessoa")
"""

"""4. Luzia é fã do Cirque du Soleil e desde que soube que haverá apresentações no Brasil, tem
mobilizado amigos e familiares para ir. Ela já pesquisou informações sobre transporte e
ingressos, e agora precisa organizar o orçamento da viagem.
Há três tipos de ingresso, dependendo do setor escolhido: platéia VIP (R$ 350), cadeira
(R$ 200) e arquibancada (R$ 100). Estudantes têm direito a 50% de desconto (meiaentrada)
em todos os setores, exceto na platéia VIP. Também é cobrada uma taxa de
conveniência correspondente a 5% do valor do ingresso. Escreva um programa que
receba como entrada o setor escolhido e o tipo de ingresso (inteira ou meia) e exiba o
valor total a ser pago."""



vip=350
cad=200
arq=100

Setor=str.lower(input("Qual Setor deseja?""\n>Vip""\n>Cadeira""\n>Arquibancada""\n>>"))
TipoIngresso=str.lower(input("Meia ou Inteira: "))

if Setor == "vip":
    valor=vip + (vip * (5/100))
    print("R$ %.2f" % valor)


elif TipoIngresso=="meia":
    if  Setor == "cadeira" :
        Setor=cad
        Valor=(float(Setor)/2)
        print(Valor+(Valor*(5/100)))

    elif TipoIngresso=="meia"and Setor == "arquibancada" :
        Setor=arq
        Valor=(float(Setor)/2)
        print(Valor+(Valor*(5/100)))

    else:
        Valor=float(Setor)
        print(Valor+(Valor*(5/100)))
        
    
else:
    print("Tipo de ingresso inválido")

























