#Neopixel Handler, zweiter Teil des Bollogggehirn V4.0
#TODO: Everything
#Die genauigkeit von time.monotonic() geht bergab nach einer stunde.

import board,busio,digitalio,time,neopixel,random,math

#SETUP ###############################################

uart = busio.UART(tx=board.GP0,rx = board.GP1,bits = 8,baudrate=57600,stop=1,parity=None,timeout=0.01)
incoming = [0 for i in range(7)]

pin_streifen_1 = board.GP2
pin_streifen_2 = board.GP3
pin_streifen_3 = board.GP4
pin_streifen_4 = board.GP5
pin_streifen_5 = board.GP6
pin_streifen_6 = board.GP7

leds_strip_1 = 70
leds_strip_2 = 70
leds_strip_3 = 70
leds_strip_4 = 70
leds_strip_5 = 70
leds_strip_6 = 70

strip1 = neopixel.NeoPixel(pin_streifen_1, leds_strip_1, brightness = 1.0, auto_write = False)
strip2 = neopixel.NeoPixel(pin_streifen_2, leds_strip_2, brightness = 1.0, auto_write = False)
strip3 = neopixel.NeoPixel(pin_streifen_3, leds_strip_3, brightness = 1.0, auto_write = False)
strip4 = neopixel.NeoPixel(pin_streifen_4, leds_strip_4, brightness = 1.0, auto_write = False)
strip5 = neopixel.NeoPixel(pin_streifen_5, leds_strip_5, brightness = 1.0, auto_write = False)
strip6 = neopixel.NeoPixel(pin_streifen_6, leds_strip_6, brightness = 1.0, auto_write = False)

strip1.fill((0,0,0))
strip2.fill((0,0,0))
strip3.fill((0,0,0))
strip4.fill((0,0,0))
strip5.fill((0,0,0))
strip6.fill((0,0,0))



###################################################################################
master_brightness = 1.0
BPM = 69.0
current_mode = []
current_FX = []
colors = []

def change_BPM(BPM_new,tenth):
    global BPM
    BPM = BPM_new + tenth/10

def change_master_brightness(data):
    global master_brightness
    master_brightness = data/255

def color_new(r,g,b):
    global colors
    colors.append([r,g,b])

def color_change(r,g,b,ID):
    global colors
    colors[ID] = [r,g,b]

def color_del(ID):
    global colors
    colors.pop(ID)
#MODES  ################################
def Mode_solid_color(r,g,b):
    global strip_array1
    global strip_array2
    global strip_array3
    global strip_array4
    global strip_array5
    global strip_array6

    for i in range(70):
        strip_array1.append([r,g,b])
        strip_array2.append([r,g,b])
        strip_array3.append([r,g,b])
        strip_array4.append([r,g,b])
        strip_array5.append([r,g,b])
        strip_array6.append([r,g,b])
    
    return


#EFFECTS ###############################
class elem_star():
    def init(self,size_max,size_min,lifetime,):


def FX_nightsky():
    global strip_array1
    global strip_array2
    global strip_array3
    global strip_array4
    global strip_array5
    global strip_array6
    

   
    return
def new_data():
    #All modes need to be checked in at the new_data lobby, from witch 
    global incoming
    id = incoming[0]
    if(id == 0):
        print("debug")
    if(id == 1):
        current_mode = [id,incoming[1],incoming[2],incoming[3]]
    elif(id == 100):
        current_FX = None
    elif(id == 101):
        current_FX = [id,incoming[1],incoming[2],incoming[3],incoming[4],incoming[5],incoming[6]]
    elif(id == 200):
        color_new(incoming[1],incoming[2],incoming[3])
    elif(id == 201):
        color_change(incoming[1],incoming[2],incoming[3],incoming[4])
    elif(id == 203):
        color_del(incoming[1])
    elif(id == 254):
        change_master_brightness(incoming[1])
    elif(id == 255):
        change_BPM(incoming[1],incoming[2])

def run_modes():
    global current_mode
    id = current_mode[0]
    if(id == 1):
        Mode_solid_color(current_mode[1],current_mode[2],current_mode[3])
        return

def run_effects():
    global current_FX
    id = current_FX[0]
    if(id == 101):
        FX_nightsky(current_FX[1],current_FX[2],current_FX[3],current_FX[4],current_FX[5],current_FX[6])




    
#MAINLOOP     ######################################################################              
refresh_rate  = 30 #ms
time_since_refresh = time.monotonic()

while(True):
    currenttime = time.monotonic()

    #DER FUCKING INPUTHANDLER
    data = uart.read(1)
    if(data != None):
        incoming[0] = int.from_bytes(data,"big")
        incoming[1] = int.from_bytes(uart.read(1),"big")
        incoming[2] = int.from_bytes(uart.read(1),"big")
        incoming[3] = int.from_bytes(uart.read(1),"big")
        incoming[4] = int.from_bytes(uart.read(1),"big")
        incoming[5] = int.from_bytes(uart.read(1),"big")
        incoming[6] = int.from_bytes(uart.read(1),"big")
        print(incoming)
        new_data()
    
    

    if(currenttime - refresh_rate < time_since_refresh):
        
        strip1.show()
        strip2.show()
        strip3.show()
        strip4.show()
        strip5.show()
        strip6.show()
        time_since_refresh = currenttime

        strip_array1 = []
        strip_array2 = []
        strip_array3 = []
        strip_array4 = []
        strip_array5 = []
        strip_array6 = []

#[Strip Array] ->
#   [Colored by Mode] ->
#       [Masked with Effect] ->
#                [Masked by Fade] ->
#                   [Masterbrightness] ->
#                                    [LED-STRIP]
