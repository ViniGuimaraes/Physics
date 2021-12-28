while True:
 K=2.975888039e-19
 Me=(K*(5.791e10)**3)**0.5/86400
 Mer=((86400*Me)**2/K)**(1/3)
 V=(K*(1.082e11)**3)**0.5/86400
 Vr=((86400*V)**2/K)**(1/3)
 T=(K*(1.496e11)**3)**0.5/86400
 Tr=((86400*T)**2/K)**(1/3)
 Ma=(K*(2.2794e11)**3)**0.5/86400
 Mar=((86400*Ma)**2/K)**(1/3)
 J=(K*(7.7833e11)**3)**0.5/86400
 Jr=((86400*J)**2/K)**(1/3)
 S=(K*(1.4294e12)**3)**0.5/86400
 Sr=((86400*S)**2/K)**(1/3)
 U=(K*(2.87099e12)**3)**0.5/86400
 Ur=((86400*U)**2/K)**(1/3)
 N=(K*(4.5043e12)**3)**0.5/86400
 Nr=((86400*N)**2/K)**(1/3)
 P=(K*(5.91352e12)**3)**0.5/86400
 Pr=((86400*P)**2/K)**(1/3)
 a='Mercúrio'
 b='Vênus'
 c='Terra'
 d='Marte'
 e='Júpiter'
 f='Saturno'
 g='Urano'
 h='Netuno'
 i='Plutão'
 p=input("digite o nome do planeta: ")
 if p=='Mercúrio':
   print("O período de translação de %s é: %s Dias Terrestre" %(p,Me))
   print("A distância Sol/%s é: %s m " %(p,Mer))
 elif p=='Vênus':
   print("O período de translação de %s é: %s Dias Terrestre" %(p,V))
   print("A distância Sol/%s é: %s m " %(p,Vr))
 elif p=='Terra':
   print("O período de translação de %s é: %s Dias" %(p,T))
   print("A distância Sol/%s é: %s m " %(p,Tr))
 elif p=='Marte':
   print("O período de translação de %s é: %s Dias Terrestre" %(p,Ma))
   print("A distância Sol/%s é: %s m " %(p,Mar))  
 elif p=='Júpiter':
   print("O período de translação de %s é: %s Dias Terrestre" %(p,J))
   print("A distância Sol/%s é: %s m " %(p,Jr))
 elif p=='Saturno':
   print("O período de translação de %s é: %s Dias Terrestre" %(p,S))
   print("A distância Sol/%s é: %s m " %(p,Sr))
 elif p=='Urano':
   print("O período de translação de %s é: %s Dias Terrestre" %(p,U))
   print("A distância Sol/%s é: %s m " %(p,Ur))
 elif p=='Netuno':
   print("O período de translação de %s é: %s Dias Terrestre" %(p,N))
   print("A distância Sol/%s é: %s m " %(p,Nr))
 elif p=='Plutão':
   print("O período de translação de %s é: %s Dias Terrestre" %(p,P))
   print("A distância Sol/%s é: %s m " %(p,Pr))

   
            
            
    
 
    
     


