import hcsr04
import utime

capteur_hcsr04_1 = hcsr04.HCSR04(18,19)  #trig et echo
while True:
    dist_mm = capteur_hcsr04_1.distance()
    #dist_mm = capteur_hcrs04_1.n_mesures(10)
    print(dist_mm)
    utime.sleep_ms(500)