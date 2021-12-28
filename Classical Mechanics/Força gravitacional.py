while True:
 G=6.67e-11
 M=1.98892e30
 x=G*M
 j=input("digite o nome do planeta: ")
 mp=float(input("digite a massa de %s (Kg) : " %(j)))
 sp=float(input("digite a distância sol-%s (m): " %(j)))
 y=(x*mp/sp**2)
 print("A Força Gravitacional sol-%s é:  %s N " %(j,y))

 print("")
