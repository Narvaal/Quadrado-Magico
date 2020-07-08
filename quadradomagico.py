import random
import turtle

'''
Nome:Alessandro Bezerra Da Silva
'''

#Computação

def matrizperfeita():
    valorer = [2,7,6,9,5,1,4,3,8]
    matriz = [0]*3
    cont = 0

    for i in range(3):
        matriz[i] = [0]*3

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = valorer[cont]
            cont += 1
    return matriz
            
def quadradomagico(matriz):
   
    valores = [0]*(len(matriz)*2 + 2)
    pos,index = 0,0
    
    somaval = 0

    #Soma linhas 
    while pos < len(matriz):
        for i in range(len(matriz)):
            somaval += matriz[pos][i]
            
        valores[index] = somaval
        pos += 1
        index += 1
        somaval = 0
        
    
    pos = 0
    
    #Soma colunas 
    while pos < len(matriz):
        for i in range(len(matriz)):
            somaval += matriz[i][pos]
            
        valores[index] = somaval
        pos += 1
        index += 1
        somaval = 0


    #Diagonal principal 
    for i in range(len(matriz)):      
        somaval += matriz[i][i]
        

    valores[index] = somaval
    index += 1

    aux = 0
    somaval = 0

    
    #Diagonal secundaria 
    for i in range(len(matriz)-1,-1,-1):
        somaval += matriz[i][aux]
        aux += 1

        

    valores[index] = somaval
    index += 1   

    
    cont = 0

    #Teste valores iguias
    for i in range(len(valores)):
        if valores[i] == valores[0]:
            cont += 1
    if cont == len(valores):
        return valores,True
    
    return valores,False
            
        

def gerarmat(largura,altura,var,varn): 
    matriz = [0]*altura
    for i in range(len(matriz)):
        matriz[i] = [0]*largura
        
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = random.randrange(varn,var)
    
    return matriz

def imprimirmat(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    print()



#Layout
WIDTH = 1000
HEIGHT = 800


'tela'
tela = turtle.Screen()
tela.title("Quadrado Mágico")
tela.bgcolor("Black")
tela.setup(width = WIDTH,height = HEIGHT)
tela.tracer(0)

'quadrado'
quadrado = turtle.Turtle()
quadrado.speed(0)
quadrado.shape("square")
quadrado.color("green")
quadrado.shapesize(stretch_wid = WIDTH/20, stretch_len = HEIGHT/20)
quadrado.penup()
quadrado.zindex = 0
quadrado.goto(0,0)

'quadrado2'
quadrado2 = turtle.Turtle()
quadrado2.speed(0)
quadrado2.shape("square")
quadrado2.color("black")
quadrado2.shapesize(stretch_wid = HEIGHT/20, stretch_len = WIDTH/20)
quadrado2.penup()
quadrado2.zindex = 5
quadrado2.goto(0,0)


'caneta'

caneta =  turtle.Turtle()
caneta.speed(0)
caneta.color("White")
caneta.penup()
caneta.hideturtle()
caneta.goto(0,0)
caneta.clear()
quadrado.zindex = 10


'caneta2'

caneta2 =  turtle.Turtle()
caneta2.speed(0)
caneta2.color("Blue")
caneta2.penup()
caneta2.hideturtle()
caneta2.goto(0,0)
caneta2.clear()
quadrado.zindex = 10



'Main Loop'

x = 0

while True:

    
    
    input("Aperte ENTER para continuar!")
    
    tela.update()
    
       
    
    
    

    """
    #matriz = matrizperfeita()
    
    # teste
    matriz = gerarmat(2,2,9,0)
    tamanho = len(matriz)
    valarray,aux = quadradomagico(matriz)
    # teste
    """
    
    if x != True:
        'Entrada de valores'
        tamanho = int(tela.numinput("Escreva o tamanho da matriz","Apenas um valor"))
        numeros = tela.textinput("Escreva os valores da matriz","Escreva os {} valores em sequencia".format(tamanho**2))

        matriz = [0]*tamanho
        cont = 0

        for i in range(tamanho):
            matriz[i] = [0]*tamanho
       
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                matriz[i][j] = int(numeros[cont])
                cont += 1
        
        valarray,bol = quadradomagico(matriz)

    
    
    'matriz'
    

    tamanhofont = int(440/tamanho)
    tamanhofont2 = int(200/tamanho)
    x = tamanhofont * -len(matriz)//2 + tamanhofont//2
    y =  tamanhofont * +len(matriz)//2 - tamanhofont
    
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            caneta.goto(x,y)       
            caneta.write("{}".format(matriz[i][j]),align = "center",font =("Courier",tamanhofont))
            x += tamanhofont 
            
        y -= tamanhofont 
    
        x = tamanhofont * -len(matriz)//2 + tamanhofont//2

    
    'linha'
 

    x = tamanhofont * +len(matriz)//2 - tamanhofont2/2 + tamanhofont//2
    y = tamanhofont * +len(matriz)//2 - tamanhofont2

    for i in range(len(matriz)):            
        caneta2.goto(x,y)
        caneta2.write("{}".format(valarray[i]),align = "left",font = ("Courier",tamanhofont2))
        y -= tamanhofont   
         

        
     
    
    'diagonal pri'

    x = tamanhofont * -len(matriz)//2 - tamanhofont2 - tamanhofont/2 + tamanhofont//2
    y = tamanhofont * -len(matriz)//2 - tamanhofont2 
    
   
    
    
    posfin = len(matriz)* 2

    caneta2.goto(x,y)
    caneta2.color("Red")
    caneta2.write("{}".format(valarray[posfin]),align = "Center",font =("Courier",tamanhofont2))

    'diagonal sec'
    x = tamanhofont * -len(matriz)//2 + tamanhofont*len(matriz) + tamanhofont//2
    y = tamanhofont * -len(matriz)//2 - tamanhofont2

    caneta2.goto(x,y)
    
    caneta2.write("{}".format(valarray[posfin + 1]),align = "Center",font =("Courier",tamanhofont2))
    

    
    'coluna'
    caneta2.color("Blue")
    aux = tamanhofont2//3
    x = tamanhofont * -len(matriz)//2 + tamanhofont//2
    y = tamanhofont * -len(matriz)//2 - tamanhofont/2

    for i in range(len(matriz)):            
        caneta2.goto(x,y)
        caneta2.write("{}".format(valarray[i]),align = "Center",font = ("Courier",tamanhofont2))
        x += tamanhofont 

    
    input("Aperte ENTER para continuar!")
    
    if bol == True:
        tela.clear()
        
        quadrado3 = turtle.Turtle()
        quadrado3.speed(0)
        quadrado3.shape("square")
        quadrado3.color("Green")
        quadrado3.shapesize(stretch_wid = HEIGHT/20, stretch_len = WIDTH/20)
        quadrado3.penup()
        quadrado3.zindex = 11
        quadrado3.goto(0,0)

        caneta.goto(0,-30)
        caneta.write("A matriz é um \nquadrado magico",align = "Center",font =("Courier",60))
        
        
        
    else:
        tela.clear()
        quadrado3 = turtle.Turtle()
        quadrado3.speed(0)
        quadrado3.shape("square")
        quadrado3.color("Red")
        quadrado3.shapesize(stretch_wid = HEIGHT/20, stretch_len = WIDTH/20)
        quadrado3.penup()
        quadrado3.zindex = 11
        quadrado3.goto(0,0)

        caneta.goto(0,-30)
        caneta.write("A matriz não é \nquadrado magico",align = "Center",font =("Courier",60))

    
    

    
        
    
    
        

    
        
    
    
    
        
        
    
        
        

    
        
        


    

    
    
    
    
    
        
        
    

    









