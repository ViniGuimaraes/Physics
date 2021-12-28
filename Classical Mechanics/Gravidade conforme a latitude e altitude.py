import math
def main():
    while True:
        beta = 5.3*10**(-3)
        g0 = 9.7803
        R = 6.371*10**6
        latitude = int(input("Digite a latitude: "))
        altitude = float(input("Digite a altitude: "))
        
        deltagz = (-(2*g0*(1+beta*(math.sin(latitude))**(2))*altitude))/R
        glat = g0*(1+beta*(math.sin(latitude))**(2))

        g = glat+deltagz

        print("A gravidade a uma latitude de ", latitude, "graus e a uma altitude de ", altitude,  "metros é ", g, "m/s^2\n")   
main()
