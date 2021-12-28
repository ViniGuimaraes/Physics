def discrepancia(K, Razao, Planeta):
    if K > Razao:
            dif = K-Razao
            print("O valor de K é maior que a razão T^2/R^3 para %s, a discrepância é de %s\n" %(Planeta,dif))
    elif Razao > K:
        dif = Razao - K
        print("O valor de K é menor que a razão T^2/R^3 para %s, a discrepância é de %s\n" %(Planeta,dif))
    else:
        print("Não há discrepância\n")
            
def main():
    while True:
        dif = 0
        Rmer = 5791e7
        Tmer = 7600521.6
        Razao_Mer = Tmer**2/Rmer**3
        Rven = 1082e8
        Tven = 19414166.4
        Razao_Ven = Tven**2/Rven**3
        Rter = 1496e8
        Tter = 3.154e7
        Razao_Ter = Tter**2/Rter**3
        Rmar = 2279e8
        Tmar = 59354294.4
        Razao_Mar = Tmar**2/Rmar**3
        Rjup = 7785e8  
        Tjup = 374247820.8
        Razao_Jup = Tjup**2/Rjup**3
        Rsat = 1429e9
        Tsat = 929596608
        Razao_Sat = Tsat**2/Rsat**3
        Rura = 2871e9
        Tura = 2661041808
        Razao_Ura = Tura**2/Rura**3
        Tnet = 5200418592
        Rnet = 4498e9
        Razao_Net = Tnet**2/Rnet**3
        Tplu = 7828989552
        Rplu = 591352e7
        Razao_Plu = Tplu**2/Rplu**3
        K = 2.975888039e-19
        p = input("Digite o nome do planeta: ")
        if p == "Mercúrio" or p == "Mercurio" or p == "mercurio":
            Planeta = "Mercúrio"
            discrepancia(K, Razao_Mer, Planeta)
        elif p == "Vênus" or p == "Venus" or p == "venus":
            Planeta = "Vênus"
            discrepancia(K, Razao_Ven, Planeta)
        elif p == "Terra" or p == "terra":
            Planeta = "Terra"
            discrepancia(K, Razao_Ter, Planeta)
        elif p == "Marte" or p == "marte":
            Planeta = "Marte"
            discrepancia(K, Razao_Mar, Planeta)
        elif p == "Júpiter" or p == "Jupiter" or p == "jupiter":
            Planeta = "Mercúrio"
            discrepancia(K, Razao_Jup, Planeta)
        elif p == "Saturno" or p == "saturno":
            Planeta = "Saturn"
            discrepancia(K, Razao_Sat, Planeta)
        elif p == "Urano" or p == "urano":
            Planeta = "Urano"
            discrepancia(K, Razao_Ura, Planeta)
        elif p == "Netuno" or p == "netuno":
            Planeta = "Netuno"
            discrepancia(K, Razao_Net, Planeta)
        elif p == "Plutão" or p == "Plutao" or p == "plutao":
            Planeta = "Plutão"
            discrepancia(K, Razao_Plu, Planeta)
        else:
            return 
main()

