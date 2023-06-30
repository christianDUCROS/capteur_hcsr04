'''
Sur groove : sig correspond à trig et echo donc
broche_trig = broche_echo = broche_sig
'''
 
from machine import Pin, time_pulse_us
import utime

class HCRS04 () :
    
    def __init__(self,broche_trig,broche_echo):
       self.Pin_trig = broche_trig
       self.Pin_echo = broche_echo

    def distance(self):   
        sig = Pin(self.Pin_trig, Pin.OUT)
        start = time.ticks_ms() # get millisecond counter
        sig.value(0)  
        utime.sleep_us(1)
        sig.value(1) #déclenchement du trigger >10us  mesuré 33us
        #utime.sleep_us(10)
        sig.value(0)
        delta = time.ticks_diff(time.ticks_ms(), start)
        print(delta)
        sig = Pin(self.Pin_echo, Pin.IN)
        t = time_pulse_us(sig, 1, 23000)  # timeout pour 4m  = 2 * 11700
        dist_mm = 340000 * t // 2000000  #en mm 
        utime.sleep_ms(60) #temps mini entre 2 mesures  (60ms)
        return dist_mm
    
    def n_mesures(self, n) :
        somme = 0
        for i in range (n) :
            dist = self.distance()
            somme = somme + dist
        moyenne = somme // n
        return moyenne
