hora1 = int(input("Digite a hora da primeira entrada: "))
min1 = int(input("Digite os minutos da primeira entrada: "))
hora2 = int(input("Digite a hora da segunda entrada: "))
min2 = int(input("Digite os minutos da segunda entrada: "))
soma1 = int((hora1 + hora2))
soma2 = int((min1 + min2))

if hora1 > 12 and hora2 > 12 and soma2 >= 60:
    somat = soma2 - 60
    somah = soma1 + 1
    horat = somah - 24
    print("{}:{}".format(horat, somat))
    if hora1 < 12 and hora2 < 12 and soma2 >= 60:
        somat2 = soma2 - 60
        somah = soma1 + 1
        horat2 = somah - 12
        print("{}:{}".format(horat2, somat2))
else:
    horato = soma1 - 12
    print("{}:{}".format(horato, soma2))

#if soma2 >= 60:
   # somat = soma2 - 60
   # somah = soma1 + 1
   # horat = somah - 12
   # print("{}:{}".format(horat, somat))
#minSTR = ""
# if somat >= 0 or somat < 10:
#        minSTR = "0"+str(somat)
 #   else:
#        minSTR = str(somat)
 #   print("{}:{}".format(horat, minSTR))