import math
def velocidade_translacao (a, b, e, p, T, r):
    h = ((a-b)/(a+b))**2
    p1 = math.pi*(a+b)*(1 + (1/4)*h + (1/64)*h**2 + (1/256)*h**3)
    p2 = math.pi*(a+b)*(1 + 3*h/(10 + math.sqrt(4 - 3*h)))
    p3 = math.pi*a*(2-e**2/2 + 3*e**4/16)
    p4 = 2*math.pi*r
    v_series_h = p1/T
    v_ramanujan = p2/T
    v_series_e = p3/T
    v_circ = p4/T
    print("SÉRIE COM PARÂMETRO h: ", v_series_h, "Km/s")
    print("FÓRMULA DE RAMANUJAN: ", v_ramanujan, "Km/s")
    print("SÉRIE COM EXCENTRICIDADE COMO PARÂMETRO: ", v_series_e, "Km/s")
    print("ÓRBITA CIRCULAR: ", v_circ, "Km/s")
    print("")

def main():
    while True:
        aMerc = 57910000.0
        eMerc = 0.2056
        bMerc = 56672817.25448615
        Tmer = 7600521.6
        RMe= 5791e4
        aVen = 108200000.0
        bVen = 108197571.423745
        eVen = 0.0067
        Tven = 19414166.4
        RV=1082e5
        aTer = 149598261
        bTer = 149579137.57331802
        eTer = 0.0167
        Tter = 3.154e7
        RT=1496e5
        aMar = 2279391e2
        bMar = 226941458.60218646
        eMar = 0.0935
        Tmar = 59354294.4
        RMa=22794e4
        aJup = 7785472e2
        bJup = 777398867.7940343
        eJup = 0.0489
        Tjup = 374247820.8
        RJ=7785e5
        aSat = 143344937e1
        bSat = 1427116675.232544
        eSat = 0.0565
        Tsat = 929596608
        RS=1429e6
        aUra = 2876679082
        bUra = 2867990416.0786167
        eUra = 0.0457
        Tura = 2661041808
        RU=2871e6
        aNet = 4503443661
        bNet = 4504012413.785736
        eNet = 0.0113
        Tnet = 5200418592
        RN=45043e5
        aPlu = 5906376272
        bPlu = 5734189561.588616
        ePlu = 0.2444
        Tplu = 7828989552
        RP=591352e4

        p = input("Digite o nome do planeta: ")
        if p == "Mercúrio" or p == "Mercurio" or p == "mercurio":
            velocidade_translacao(aMerc, bMerc, eMerc, p, Tmer, RMe)
        elif p == "Vênus" or p == "Venus" or p == "venus":
            velocidade_translacao(aVen, bVen, eVen, p, Tven, RV)
        elif p == "Terra" or p == "terra":
            velocidade_translacao(aTer, bTer, eTer, p, Tter, RT)
        elif p == "Marte" or p == "marte":
            velocidade_translacao(aMar, bMar, eMar, p, Tmar, RMa)
        elif p == "Júpiter" or p == "Jupiter" or p == "jupiter":
            velocidade_translacao(aJup, bJup, eJup, p, Tjup, RJ)
        elif p == "Saturno" or p == "saturno":
            velocidade_translacao(aSat, bSat, eSat, p, Tsat, RS)
        elif p == "Urano" or p == "urano":
            velocidade_translacao(aUra, bUra, eUra, p, Tura, RU)
        elif p == "Netuno" or p == "netuno":
            velocidade_translacao(aNet, bNet, eNet, p, Tnet, RN)
        elif p == "Plutão" or p == "Plutao" or p == "plutao":
            velocidade_translacao(aPlu, bPlu, ePlu, p, Tplu, RP)
        else:
            return 
main()

