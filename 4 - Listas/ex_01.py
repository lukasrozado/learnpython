#Dada a lista abaixo
#use indexação para descobrir "olá"
      #1    #2   # 3 DENTRO DE 3 TEM 3 INDEX DENTRO DO SEGUNDO TEM 1 QUE É OLÁ.
lst = [1,2,[3,4],[5,[100,200,["olá"]],23,11],1,7]
print(lst[3][1][2])