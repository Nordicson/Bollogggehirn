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
class Mode():
    def __init__(self,id,par_1,par_2,par_3,par_4,par_5,par_6):
        self.id = id
        self.par_1 = par_1
        self.par_2 = par_2
        self.par_3 = par_3
        self.par_4 = par_4
        self.par_5 = par_5
        self.par_6 = par_6
        self.arr = []
    
    def get_params(self):
        return [self.id, self.par_1, self.par_2, self.par_3, self.par_4, self.par_5, self.par_6]

    def frame_step(self):
        return
    
    def get_array(self):
        return self.arr
    
    def new_param(self):
        return
        
class Debug(Mode):
    def __init__(self):
        self.id = 0
        self.par_1 = 0
        self.par_2 = 0
        self.par_3 = 0
        self.par_4 = 0
        self.par_5 = 0
        self.par_6 = 0
        self.arr = []

class Mode_Solid_Color(Mode):
    def get_array(self):
        params = super().get_params(self)
        COLOR_R,COLOR_G,COLOR_B = params[1], params[2], params[3]
        return [[COLOR_R,COLOR_G,COLOR_B] for i in range(70)]

class Mode_Checkerbox(Mode):
    def __init__(self,id, par_1, par_2, par_3, par_4, par_5, par_6):
        super().__init__(id,par_1, par_2, par_3, par_4, par_5, par_6)
        self.move = self.par_6
        self.arr = [[0,0,0] for i in range(70)]
        self.move_count = 0
        i = 0
        while i < 70:
            modulo = (i % (par_4 + par_5))
            if ((modulo >= 0) & (modulo < par_4)):
                self.arr[i] = [par_1, par_2, par_3]
            i = i + 1             

    def get_array(self):
        return self.arr

    def set_array(self, arr):
        self.arr = arr

    def frame_step(self):
        if self.move_count == self.move:
            new_arr = []
            new_arr.append(self.arr[69])
            new_arr.append(self.arr[0:69])
            self.set_array(new_arr)
            self.move_count = 0
        else:
            self.move_count += 1

    def new_param(self):
        i = 0
        while i < 70:
            modulo = (i % (self.par_4 + self.par_5))
            if ((modulo >= 0) & (modulo < self.par_4)):
                self.arr[i] = [self.par_1, self.par_2, self.par_3]
            i = i + 1
        
#EFFECTS ###############################
def FX_nightsky():
    return
    

   
    return
def new_data():
    #All modes need to be checked in at the new_data lobby, from witch 
    global incoming
    global current_mode
    id = incoming[0]

    if(id > 0 & id < 100):
        if(current_mode.id == id):
            current_mode.par_1 = data[1]
            current_mode.par_2 = data[2]
            current_mode.par_3 = data[3]
            current_mode.par_4 = data[4]
            current_mode.par_5 = data[5]
            current_mode.par_6 = data[6]
            current_mode.new_param()
        else:
            current_mode = find_mode(incoming)


    elif(id == 0):
        print("debug")
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

def find_mode(data):
    id = data[0]
    if(id == 1):
        return Mode_Solid_Color(id,data[1],data[2],data[3],data[4],data[5],data[6])
    if(id == 2):
        return Mode_Checkerbox(id,data[1],data[2],data[3],data[4],data[5],data[6])

#MAINLOOP     ######################################################################              
refresh_rate  = 30 #ms
time_since_refresh = time.monotonic()

current_mode = Debug()
current_FX = []

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
        current_mode.set_color(20,233,5)
        current_mode.frame_step()
        
        strip1 = current_mode.get_array()
        strip1.show()
        strip2.show()
        strip3.show()
        strip4.show()
        strip5.show()
        strip6.show()
        time_since_refresh = currenttime


#[Strip Array] ->
#   [Colored by Mode] ->
#       [Masked with Effect] ->
#                [Masked by Fade] ->
#                   [Masterbrightness] ->
#                                    [LED-STRIP]
