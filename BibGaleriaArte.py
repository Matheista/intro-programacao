
def consultaPreco(x,y=0):
    if y==0:
        y=input("Qual o Titúlo da Obra?\n")
    print('O preço do "'+y+'" é %.2f R$' % x)

def consultaArtista(x,y=0):
    if y==0:
        y=input("Nome da obra?\n")
    print('A obra" '+y+'" foi feita por',x)

def consultaQuantObras(x,y=0):
    if y==0:
        y=input(str.lower("infore o nome do Artista para saber quantas obras possuí\n"))
    print('O Artista "'+y+'" possui '+str(x)+' obra(s)')
    
def consultaTipo(x,y=0):
    if y==0:
        y=input("Nome da obra?\n")
    if x == "escultura":
        print('A Obra "'+y+'" é uma Escultura')
    else:
        print('A Obra "'+y+'" é um Quadro')
