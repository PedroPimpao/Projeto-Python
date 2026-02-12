numero=int(input("Digite um número inteiro: "))
cont=0
for i in range(1,numero+1):
    if numero%i==0:
       print("{}".format(i),end=' ') 
       cont=cont+1
if cont<3:
    print("\nNUMERO PRIMO")
else:
    print("\nNÃO É PRIMO")
  
    


