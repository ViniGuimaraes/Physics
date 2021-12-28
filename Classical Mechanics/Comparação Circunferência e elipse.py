import math
def velocidade_translacao(a, e, p, T, C):
    b = a*(1-e**2)**1/2
    v = (math.pi*a*(2-e**2/2 + 3*e**4/16))/T
    v1 = (math.pi*(3*(a+b)-((3*a+b)*(a+3*b))**1/2))/T
    v_ = C/T
    print("ELIPSE SÉRIE: %s" %v)
    print("ELIPSE RAMANUJAN: %s" %v1)
    print("CIRCUNFERÊNCIA: %s" %v_)

def main():
    while True:
        aMerc = 5790905e4
        eMerc = 2.0563e-1
        Tmer = 7600521.6
        RMe=5791e7
        CMe=2*math.pi*RMe
        aVen = 10820893e4
        eVen = 6772e-6
        Tven = 19414166.4
        RV=1082e8
        CV=2*math.pi*RV
        aTer = 149598261e3
        eTer = 1.671123e-2
        Tter = 3.154e7
        RT=1496e8
        CT=2*math.pi*RT
        aMar = 2279391e5
        eMar = 9.3315e-2
        Tmar = 59354294.4
        RMa=2279e8
        CMa=2*math.pi*RMa
        aJup = 7785472e5
        eJup = 4.8775e-2
        Tjup = 374247820.8
        RJ=7785e8
        CJ=2*math.pi*RJ
        aSat = 143344937e4
        eSat = 5.5723219e-2
        Tsat = 929596608
        RS=1429e9
        CS=2*math.pi*RS
        aUra = 2876679082e3
        eUra = 4.4405586e-2
        Tura = 2661041808
        RU= 2871e9
        CU=2*math.pi*RU
        aNet = 4503443661e3
        eNet = 1.1214269e-2
        Tnet = 5200418592
        RN=4498e9
        CN=2*math.pi*RN
        aPlu = 5906376272e3
        ePlu = 2.4880766e-1
        Tplu = 7828989552
        RP=591352e9
        CP=2*math.pi*RP

        p = input("Digite o nome do planeta: ")
        if p == "Mercúrio" or p == "Mercurio" or p == "mercurio":
            velocidade_translacao(aMerc, eMerc, p, Tmer, CMe)
        elif p == "Vênus" or p == "Venus" or p == "venus":
            velocidade_translacao(aVen, eVen, p, Tven, CV)
        elif p == "Terra" or p == "terra":
            velocidade_translacao(aTer, eTer, p, Tter, CT)
        elif p == "Marte" or p == "marte":
            velocidade_translacao(aMar, eMar, p, Tmar, CMa)
        elif p == "Júpiter" or p == "Jupiter" or p == "jupiter":
            velocidade_translacao(aJup, eJup, p, Tjup, CJ)
        elif p == "Saturno" or p == "saturno":
            velocidade_translacao(aSat, eSat, p, Tsat, CS)
        elif p == "Urano" or p == "urano":
            velocidade_translacao(aUra, eUra, p, Tura, CU)
        elif p == "Netuno" or p == "netuno":
            velocidade_translacao(aNet, eNet, p, Tnet, CN)
        elif p == "Plutão" or p == "Plutao" or p == "plutao":
            velocidade_translacao(aPlu, ePlu, p, Tplu, CP)
        else:
            return 
main()
