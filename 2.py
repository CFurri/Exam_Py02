#exmp :7 4 17 25 36*47 14 27 39*34 9 16 7*25 13 6 14 37

seq = input("enter la sequencia separat per  * : ").split("*") #crear una seq de numeros separados por * :["7 4 17 25 36" ,"47 14 27 39","34 9 16 7"]
distancies = []
print(seq,"\n")

for nums in seq: #recorrer cada subsequencia de sequencia separado por *
    nums = nums.split() #crear un list de cada num separado por " " : nums = ["7","4","17","25","36"]
    nums = list(map(int,nums)) #convertir cada element en dicho list a int (a defecto es string) => tambien puedes poner int() dentro de primer for
    suma = 0                        #nums => [7,4,17,25,36]
    print(nums)
    
    for num in nums : #recorer  cada num de subsequencia(nums) para calcular la suma
        suma+=num       #suma = 7+4+17+25+36
    
    mitjana = suma/len(nums) #calcular la mitjana suma / cantidad de numeros en la lista de nums ->len()
    print("mitjana : ",mitjana)
                            
    #minim_dis = False# 
                      #para calcular el minim de una lista en un bucle siempre tenemos que poner un primer valor mas mayor posible+1 para que si o si
                      #con primer if cambia el valor de minim por ejemplo si el rango de numeros es 1 a 10 ponemos 11 y con primer recorida el valor
                      #de minim si o si cambia y asi si tengamos una lista [10,10,10,10] el valor de minim es 10 o [10,9] valor de minim = 9
                      #en caso de enconterar maxim debriamos poner el valor mas menor por defecto ...
                      #pero aqui no sabemos cual es el maximum valor posible aqui vienen 2 sulociones poner el valor +infinto o lo que
                      #yo he hecho poner lo en False y anadir otro bloc de if que digo si es False el valor de minim no hay ningun comparcion 
                      #solo pon el minim_dis egual que numero recorrido que es primer numero 
                      #tambien pueded soponer que mayor numero posible es 100 poner minim_dis = 100 y borrar bloce de primer if y else

                      #ahora lo estoy pensando no borro mi explicacion de arriba pero es muy dificil dejalo(te sirve seguro leer lo para otros)
                      #ya que tenemos nuestro lista basicamente podemos poner un valor de la lista a defecto minim = mitjana-nums[0] porque ya
                      #tenemos la lista y la mitjana ponemos el primer valor por defecto calculando manual la distancia. si hay distancia menor 
                      #que este pues cambia el valor sino pues nada es el minim no borro codigo de antes para que veas
    minim_dis = abs(mitjana-nums[0])                  
    
    for num in nums: #ahora que tenemos mitjana de la lista(nums) recoremos la lista para calcular distancias y sacar el minimo
        dis = abs(mitjana-num) #abs() para tener el valor absoluto el nagativo no sirve en calcular distancia
        #if minim_dis != False:
        if dis <= minim_dis: #el famoso if para mirar si hay un distancia menor que el primero
                minim_dis=dis #para que cambia el valor de minim
        #else:
        #    minim_dis=dis
    
    print("minim distancia amb mitjana",minim_dis,"\n")
    distancies.append(minim_dis) #ahora que tenemos distancia minima lo anadiremos a una lista por cada sub sequencia

#el final de este for tenemos la lista de minim distancias de cada subseq[minim_distancia_subseq(1),minim_distancia_subseq(2),minim_distancia_subseq(3), ...]

#este troso de codi basicamente trata de enconterar el mayor numero en la lista de distancias
i_maxim = 0 # porque nececitamos el numero de subseq este for trata de enconterar el indice de valor maximo por eso es un for i in range... 
maxim_dis = 0
for i in range(0,len(distancies)): #recore los (indices) de cada distancia en lista de distancias 
    if distancies[i] >= maxim_dis: #el if para mirar si el valor recorrido es mayor que anterior
        maxim_dis = distancies[i]  #cambiar el valor de maxim
        i_maxim = i                #si el valor recorido es mayor que anterior pues asi guardamos su indice con cambiar el valor de i_maxim


#ya que tenemos el indice maximo solo el unico punto es que el indice siempre epiece de 0 pero la pregunta quiere numero de subseq (empice de 1)

print("sequencia que te mes distancia amb mitjana : ",i_maxim + 1) # aqui un +1 y es acabo eres gilipollas si no lo lees entero -->R / Homeeee no m'insultis ho he llegit tot

#gracias por vuestro atencion
