Letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Poema = input("entra el poema (les frases separades per / ): ").split("/")
rimas = []
resultado = []
rima_map=[]

for frase in Poema:
    frase = frase.split()
    rimas.append(frase[-1][-2:])

print(rimas)
for rima in rimas:
    if not(rima in rima_map):
        rima_map.append(rima)
        rima_map.append(Letras[0])
        resultado.append(Letras.pop(0))
    else:
        indice = rima_map.index(rima)
        resultado.append(rima_map[indice+1])

print(rima_map)
res = " ".join(resultado)
print(res)


#Del mal que pas no puc guarir/si no em mirau/amb los ulls tals, que puga dir/que ja no us plau/que jo per vós haja morir/
#
#Si muir per vós llavors creureu/l'amor que us port/i no es pot fer que no ploreu/la trista mort/d'aquell que ara no voleu/
#
#que el mal que pas no em pot jaquir/si no girau/los vostres ulls, que em vullen dir/que ja no us plau/que jo per vós haja morir/