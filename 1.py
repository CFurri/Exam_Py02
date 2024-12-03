num_alum = int(input("entera numero de alumnos: "))
aprovats  = 0
nota_mes_alt = 0
num_total_notes = 0

for na in range(num_alum):
    num_notes = int(input("entera numero de les notes: "))
    num_total_notes += num_notes
    suma = 0
    suspens = 0
    minim = 10
    maxim = 0 
    for nn in range(num_notes):
        la_nota = int(input("entera la nota: "))
        suma += la_nota
        
        if la_nota < 5 : 
            suspens += 1
        else:
            aprovats += 1

        if la_nota >= nota_mes_alt:
            nota_mes_alt = la_nota
        
        if la_nota >= maxim:
            maxim = la_nota
        
        if la_nota <= minim:
            minim = la_nota
    
    if num_notes != 0:
        if suspens != 0:
            print(f"Alumne {na+1} : {suspens} suspensos , diferencia {maxim-minim} \n")
        else:
            print(f"Alumne {na+1} : Tot aprovat , mitjana {suma/num_notes} \n")

print(f"Nota mes alta = {nota_mes_alt} , aprovats = {100*aprovats/num_total_notes}% ({aprovats} de {num_total_notes})")
    