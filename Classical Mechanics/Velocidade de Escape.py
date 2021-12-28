while True:
 G=6.67e-11
 j=input("digite o nome do planeta: ")
 M=float(input("digite a massa de %s (Kg) : " %(j)))
 R=float(input("digite o raio de %s (m) : " %(j)))
 x= 1e-3*(2*M*G/R)**0.5
 print("A velocidade de escape da superfície de %s é: %s Km/s" %(j,x))
    

 print("")
 
 
         


            

