seq = input("Entra la seqüència separada per * : ").split("*")
A = seq[0].count("A")
B = seq[0].count("B")
cont = 0
for i in range(1,len(seq)):
    if seq[i].count("A") == A and seq[i].count("B") == B:
        cont += 1
print(cont)

#Exm: ABBCR*CDASBR*TBYBSA*AABSDAAB
#Res:2
