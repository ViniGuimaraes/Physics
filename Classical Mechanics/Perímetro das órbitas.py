import math
def PERÍMETRO (a, b, e, p, r):
    h = ((a-b)/(a+b))**2
    p1 = math.pi*(a+b)*(1 + (1/4)*h + (1/64)*h**2 + (1/256)*h**3)
    p2 = math.pi*(a+b)*(1 + 3*h/(10 + math.sqrt(4 - 3*h)))
    p3 = math.pi*a*(2-e**2/2 + 3*e**4/16)
    p4 = 2*math.pi*r
    v_series_h = p1
    v_ramanujan = p2
    v_series_e = p3
    v_circ = p4
    print("PERÍMETRO DA ELIPSE POR SÉRIE COM PARÂMETRO h: ", v_series_h, "Km")
    print("PERÍMETRO DA ELIPSE PELA FÓRMULA DE RAMANUJAN: ", v_ramanujan, "Km")
    print("PERÍMETRO DA ELIPSE POR SÉRIE COM PARÂMETRO e: ", v_series_e, "Km")
    print("PERÍMETRO  POR ÓRBITA CIRCULAR: ", v_circ, "Km")
    print("")

def main():
    while True:
        aMerc = 57910000.0
        eMerc = 0.2056
        bMerc = 56672817.25448615
        RMe= 5791e4
        aVen = 108200000.0
        bVen = 108197571.423745
        eVen = 0.0067
        RV=1082e5
        aTer = 149598261
        bTer = 149579137.57331802
        eTer = 0.0167
        RT=1496e5
        aMar = 2279391e2
        bMar = 226941458.60218646
        eMar = 0.0935
        RMa=22794e4
        aJup = 7785472e2
        bJup = 777398867.7940343
        eJup = 0.0489
        RJ=7785e5
        aSat = 143344937e1
        bSat = 1427116675.232544
        eSat = 0.0565
        RS=1429e6
        aUra = 2876679082
        bUra = 2867990416.0786167
        eUra = 0.0457
        RU=2871e6
        aNet = 4503443661
        bNet = 4504012413.785736
        eNet = 0.0113
        RN=45043e5
        aPlu = 5906376272
        bPlu = 5734189561.588616
        ePlu = 0.2444
        RP=591352e4

        p = input("Digite o nome do planeta: ")
        if p == "Mercúrio" or p == "Mercurio" or p == "mercurio":
            PERÍMETRO(aMerc, bMerc, eMerc, p, RMe)
        elif p == "Vênus" or p == "Venus" or p == "venus":
            PERÍMETRO(aVen, bVen, eVen, p, RV)
        elif p == "Terra" or p == "terra":
            PERÍMETRO(aTer, bTer, eTer, p, RT)
        elif p == "Marte" or p == "marte":
            PERÍMETRO(aMar, bMar, eMar, p, RMa)
        elif p == "Júpiter" or p == "Jupiter" or p == "jupiter":
            PERÍMETRO(aJup, bJup, eJup, p, RJ)
        elif p == "Saturno" or p == "saturno":
            PERÍMETRO(aSat, bSat, eSat, p, RS)
        elif p == "Urano" or p == "urano":
            PERÍMETRO(aUra, bUra, eUra, p, RU)
        elif p == "Netuno" or p == "netuno":
            PERÍMETRO(aNet, bNet, eNet, p, RN)
        elif p == "Plutão" or p == "Plutao" or p == "plutao":
            PERÍMETRO(aPlu, bPlu, ePlu, p, RP)
        else:
            return 
main()

