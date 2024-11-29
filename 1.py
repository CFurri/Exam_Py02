num_alum = int(input("entera numero de alumnos: "))
conta_alum = 0
aprovats  = 0
nota_mes_alt = 0
num_total_notes = 0

while conta_alum < num_alum:
    conta_alum += 1
    num_notes = int(input("entera numero de les notes: "))
    conta_notes = 0
    num_total_notes += num_notes
    suma = 0
    suspens = 0
    minim = 10
    maxim = 0 
    while conta_notes < num_notes:
        conta_notes += 1
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
    
    if suspens > 0:
        print(f"Alumne {conta_alum} : {suspens} suspensos , diferencia {maxim-minim} \n")
    else:
        print(f"Alumne {conta_alum} : Tot aprovat , mitjana {suma/num_notes} \n")

print(f"Nota mes alta = {nota_mes_alt} , aprovats = {aprovats/num_total_notes*100}% ({aprovats} de {num_total_notes})")
    