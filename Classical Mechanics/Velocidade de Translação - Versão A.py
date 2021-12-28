import math
def velocidade_translacao(a, e, p, T):
    b = a*(1-e**2)**1/2
    v = (math.pi*a*(2-e**2/2 + 3*e**4/16))/T
    v1 = (math.pi*(3*(a+b)-((3*a+b)*(a+3*b))**1/2))/T
    print("A velocidade de translação para o planeta %s é %s m/s(COMPRIMENTO DA ELIPSE COM SÉRIES INFINITAS)" %(p, v))
    print("A velocidade de translação para o planeta %s é %s m/s(COMPRIMENTO DA ELIPSE COM A APROXIMAÇÃO DE RAMANUJAN)" %(p, v))
    print("\n")

def main():
    while True:
        aMerc = 5790905e4
        eMerc = 2.0563e-1
        Tmer = 7600521.6
        aVen = 10820893e4
        eVen = 6772e-6
        Tven = 19414166.4
        aTer = 149598261e3
        eTer = 1.671123e-2
        Tter = 3.154e7
        aMar = 2279391e5
        eMar = 9.3315e-2
        Tmar = 59354294.4
        aJup = 7785472e5
        eJup = 4.8775e-2
        Tjup = 374247820.8
        aSat = 143344937e4
        eSat = 5.5723219e-2
        Tsat = 929596608
        aUra = 2876679082e3
        eUra = 4.4405586e-2
        Tura = 2661041808
        aNet = 4503443661e3
        eNet = 1.1214269e-2
        Tnet = 5200418592
        aPlu = 5906376272e3
        ePlu = 2.4880766e-1
        Tplu = 7828989552

        p = input("Digite o nome do planeta: ")
        if p == "Mercúrio" or p == "Mercurio" or p == "mercurio":
            velocidade_translacao(aMerc, eMerc, p, Tmer)
        elif p == "Vênus" or p == "Venus" or p == "venus":
            velocidade_translacao(aVen, eVen, p, Tven)
        elif p == "Terra" or p == "terra":
            velocidade_translacao(aTer, eTer, p, Tter)
        elif p == "Marte" or p == "marte":
            velocidade_translacao(aMar, eMar, p, Tmar)
        elif p == "Júpiter" or p == "Jupiter" or p == "jupiter":
            velocidade_translacao(aJup, eJup, p, Tjup)
        elif p == "Saturno" or p == "saturno":
            velocidade_translacao(aSat, eSat, p, Tsat)
        elif p == "Urano" or p == "urano":
            velocidade_translacao(aUra, eUra, p, Tura)
        elif p == "Netuno" or p == "netuno":
            velocidade_translacao(aNet, eNet, p, Tnet)
        elif p == "Plutão" or p == "Plutao" or p == "plutao":
            velocidade_translacao(aPlu, ePlu, p, Tplu)
        else:
            return 
main()
