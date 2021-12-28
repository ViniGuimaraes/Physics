import math
def main():
    w = 7.2722052166430399038487115353692e-5
    R = 6371000
    g = 9.813646787
    while True:
        L = float(input("Informe a latitude: "))
        L = math.radians(L)
        print(g*(1+((((w**2)*R)/g)**2)*math.cos(L)*math.cos(L)-((2*(w**2)*R)/g)*math.cos(L)*math.cos(L))**(1/2))
main()

