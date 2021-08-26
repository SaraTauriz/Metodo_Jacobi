###            x1   x2  x3    c
ecuacion = [[  10,   2, -1,     27], 
            [  -3,  -6,  2,  -61.5],  
            [   1,   1,  5,  -21.5]] 
##varible para el error
error = 5.0
## variable para finalizar el programa
condicion = True
## variable para contar las iteraciones
iteracion = 1
## variables para guardar los resultados de
## la iteracion actual
x1=0
x2=0
x3=0
## variable para guardar los resultados
## de la pasada iteracion
x=[]
##varialbes usadas para guardar el calculo
## de los errores porcentuales
er1=100
er2=100
er3=100

while condicion:

    if iteracion==1:
        x1= ecuacion[0][3]/ecuacion[0][0]
        x2= ecuacion[1][3]/ecuacion[1][1]
        x3= ecuacion[2][3]/ecuacion[2][2]
        x=[x1,x2,x3]

    else:
        ## Calcular las x 
        #### x1 = (c1 - a1x2 - a1x3) / a1x1
        x1 = ( 27 -2*x[1] +x[2] ) / 10
        #### x2 = (c2 - a2x1 - a2x3) / a2x2
        x2 = ( -61.5 + 3*x[0] -2*x[2]) / -6
        #### x1 = (c3 - a3x1 - a3x2) / a3x3
        x3 = ( -21.5 - x[0] -x[1] ) / 5 

        ## comprobar el error porcentual
        er1 = abs(1-(x[0]/x1))*100
        er2 = abs(1-(x[1]/x2))*100
        er3 = abs(1-(x[2]/x3))*100

        #guardar las x para la proxima iteracion
        x=[x1,x2,x3]

    print(f'''Iteracion {iteracion}

            x1 = {x1}
                error relativo porcentual de x1 = {er1}%

            x2 = {x2}
                error relativo porcentual de x2 = {er1}% 

            x3 = {x3}
                error relativo porcentual de x3 = {er3}% 
    ''')
    
    if er1 < error and er2 < error and er3 < error:
        print(f""" Evaluacion:
            er1:{er1}% < {error}% = Si
            er2:{er2}% < {error}% = Si
            er3:{er3}% < {error}% = Si

        La iteracion {iteracion} llego al error definido
         con valores:
            x1 = {x1}
            x2 = {x2}
            x3 = {x3}
        """)
        condicion = False

    #aumenata el numero de iteracion
    iteracion+=1

print("fin del programa")