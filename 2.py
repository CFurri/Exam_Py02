seq = input("enter la sequencia separat per  * : ").split("*")
distancies = []
print(seq,"\n")

for nums in seq:
    nums = nums.split()
    nums = list(map(int,nums))
    suma = 0
    print(nums)
    
    for num in nums :
        suma+=num
    
    mitjana = suma/len(nums)
    print("mitjana : ",mitjana)
    
    minim_dis = False
    for num in nums:
        dis = abs(mitjana-num)
        if minim_dis:
            if dis <= minim_dis:
                minim_dis=dis
        else:
            minim_dis=dis
    
    print("minim distancia amb mitjana",minim_dis,"\n")
    distancies.append(minim_dis)


i_maxim = 0
maxim_dis = 0
for i in range(0,len(distancies)):
    if distancies[i] >= maxim_dis:
        maxim_dis = distancies[i]
        i_maxim = i

print("sequencia que te mes distancia amb mitjana : ",i_maxim + 1)

#exmp :7 4 17 25 36*47 14 27 39*34 9 16 7*25 13 6 14 37