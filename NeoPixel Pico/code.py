#Neopixel Handler, zweiter Teil des Bollogggehirn V4.0
#Die genauigkeit von time.monotonic() geht bergab nach einer stunde.

import board,busio,digitalio,time,neopixel,random,math
import ulab.numpy as numpy

#SETUP ###############################################

uart = busio.UART(tx=board.GP0,rx = board.GP1,bits = 8,baudrate=57600,stop=1,parity=None,timeout=0.00001)
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

strip1 = [0 for i in range(leds_strip_1)]
strip2 = [0 for i in range(leds_strip_2)]
strip3 = [0 for i in range(leds_strip_3)]
strip4 = [0 for i in range(leds_strip_4)]
strip5 = [0 for i in range(leds_strip_5)]
strip6 = [0 for i in range(leds_strip_6)]

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

helper = [0.0 for i in range(70)]
helper2 = numpy.array(helper)
arr1 = numpy.array([helper2,helper2,helper2])
arr2 = numpy.array([helper2,helper2,helper2])
arr3 = numpy.array([helper2,helper2,helper2])
arr4 = numpy.array([helper2,helper2,helper2])
arr5 = numpy.array([helper2,helper2,helper2])
arr6 = numpy.array([helper2,helper2,helper2])

###################################################################################
master_brightness = 1.0
BPM = 69.0
colors = []


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
        self.arr1 = numpy.array([helper2,helper2,helper2])
        self.arr2 = numpy.array([helper2,helper2,helper2])
        self.arr3 = numpy.array([helper2,helper2,helper2])
        self.arr4 = numpy.array([helper2,helper2,helper2])
        self.arr5 = numpy.array([helper2,helper2,helper2])
        self.arr6 = numpy.array([helper2,helper2,helper2])
    
    def get_params(self):
        return [self.id, self.par_1, self.par_2, self.par_3, self.par_4, self.par_5, self.par_6]

    def get_arrays(self):
        return self.arr1,self.arr2,self.arr3,self.arr4,self.arr5,self.arr6

    def frame_step(self):
        return
    
    def new_param(self):
        return

    def bpm_step(self):
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

class Mode_Solid_Color(Mode):
    def __init__(self, id, par_1, par_2, par_3, par_4, par_5, par_6):
        super().__init__(id, par_1, par_2, par_3, par_4, par_5, par_6)
        self.arr1[0,:] = par_1
        self.arr1[1,:] = par_2
        self.arr1[2,:] = par_3
        self.arr2[0,:] = par_1
        self.arr2[1,:] = par_2
        self.arr2[2,:] = par_3
        self.arr3[0,:] = par_1
        self.arr3[1,:] = par_2
        self.arr3[2,:] = par_3
        self.arr4[0,:] = par_1
        self.arr4[1,:] = par_2
        self.arr4[2,:] = par_3
        self.arr5[0,:] = par_1
        self.arr5[1,:] = par_2
        self.arr5[2,:] = par_3
        self.arr6[0,:] = par_1
        self.arr6[1,:] = par_2
        self.arr6[2,:] = par_3

    def new_param(self):
        self.arr1[0,:] = self.par_1
        self.arr1[1,:] = self.par_2
        self.arr1[2,:] = self.par_3
        self.arr2[0,:] = self.par_1
        self.arr2[1,:] = self.par_2
        self.arr2[2,:] = self.par_3
        self.arr3[0,:] = self.par_1
        self.arr3[1,:] = self.par_2
        self.arr3[2,:] = self.par_3
        self.arr4[0,:] = self.par_1
        self.arr4[1,:] = self.par_2
        self.arr4[2,:] = self.par_3
        self.arr5[0,:] = self.par_1
        self.arr5[1,:] = self.par_2
        self.arr5[2,:] = self.par_3
        self.arr6[0,:] = self.par_1
        self.arr6[1,:] = self.par_2
        self.arr6[2,:] = self.par_3

class Mode_Checkerbox(Mode):
    def __init__(self,id, par_1, par_2, par_3, par_4, par_5, par_6):
        super().__init__(id,par_1, par_2, par_3, par_4, par_5, par_6)

        if par_4 == 0:
            par_4 = 1
        self.move_count = 0

        i = 0
        while i < 70:
            modulo = (i % (par_4 + par_5))
            if ((modulo >= 0) & (modulo < par_4)):
                arr1[0,i] = par_1
                arr1[1,i] = par_2
                arr1[2,i] = par_3
                arr2[0,i] = par_1
                arr2[1,i] = par_2
                arr2[2,i] = par_3
                arr3[0,i] = par_1
                arr3[1,i] = par_2
                arr3[2,i] = par_3
                arr4[0,i] = par_1
                arr4[1,i] = par_2
                arr4[2,i] = par_3
                arr5[0,i] = par_1
                arr5[1,i] = par_2
                arr5[2,i] = par_3
                arr6[0,i] = par_1
                arr6[1,i] = par_2
                arr6[2,i] = par_3
            i = i + 1
        
    def frame_step(self): 
  
        if self.move_count == self.par_6:
            
            new_arr = numpy.roll(self.arr1.copy(),1)
            self.arr1 = new_arr.copy()
            new_arr = numpy.roll(self.arr2.copy(),1)
            self.arr2 = new_arr.copy()
            new_arr = numpy.roll(self.arr3.copy(),1)
            self.arr3 = new_arr.copy()
            new_arr = numpy.roll(self.arr4.copy(),1)
            self.arr4 = new_arr.copy()
            new_arr = numpy.roll(self.arr5.copy(),1)
            self.arr5 = new_arr.copy()
            new_arr = numpy.roll(self.arr6.copy(),1)
            self.arr6 = new_arr.copy()

            self.move_count = 0
        else:
            #print(self.move_count)
            if (self.move_count > self.par_6):
                self.move_count = 0
            else:
                self.move_count += 1

    def new_param(self):
        if par_4 == 0:
            par_4 = 1
        self.move_count = 0

        i = 0
        while i < 70:
            modulo = (i % (par_4 + self.par_5))
            if ((modulo >= 0) & (modulo < par_4)):
                self.arr1[0,i] = self.par_1
                self.arr1[1,i] = self.par_2
                self.arr1[2,i] = self.par_3
                self.arr2[0,i] = self.par_1
                self.arr2[1,i] = self.par_2
                self.arr2[2,i] = self.par_3
                self.arr3[0,i] = self.par_1
                self.arr3[1,i] = self.par_2
                self.arr3[2,i] = self.par_3
                self.arr4[0,i] = self.par_1
                self.arr4[1,i] = self.par_2
                self.arr4[2,i] = self.par_3
                self.arr5[0,i] = self.par_1
                self.arr5[1,i] = self.par_2
                self.arr5[2,i] = self.par_3
                self.arr6[0,i] = self.par_1
                self.arr6[1,i] = self.par_2
                self.arr6[2,i] = self.par_3
            i = i + 1
        

#NEW DATA ##############################
def new_data():
    #All modes need to be checked in at the new_data lobby, from witch 
    global incoming
    global current_mode
    id = incoming[0]

    if(id > 0 & id < 100):
        #Modes are seperated here
        if(current_mode.id == id):
            #in case the mode stays the same
            current_mode.par_1 = incoming[1]
            current_mode.par_2 = incoming[2]
            current_mode.par_3 = incoming[3]
            current_mode.par_4 = incoming[4]
            current_mode.par_5 = incoming[5]
            current_mode.par_6 = incoming[6]
            current_mode.new_param()
            #else the currentmode will be searched for
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
    #finds the corrisponding mode and initialises its class as current_mode
    id = data[0]
    if(id == 1):
        return Mode_Solid_Color(id,data[1],data[2],data[3],data[4],data[5],data[6])
    if(id == 2):
        return Mode_Checkerbox(id,data[1],data[2],data[3],data[4],data[5],data[6])

# TOOLS ################################

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

def finish():
    arr1,arr2,arr3,arr4,arr5,arr6 = current_mode.get_arrays()
    arr1 * master_brightness
    arr2 * master_brightness
    arr3 * master_brightness
    arr4 * master_brightness
    arr5 * master_brightness
    arr6 * master_brightness

    for i in range(70):
        strip1[i] = [ int(arr1[0][i]) , int(arr1[1][i]) , int(arr1[2][i]) ]
    for i in range(70):
        strip2[i] = [ int(arr2[0][i]) , int(arr2[1][i]) , int(arr2[2][i]) ]
    for i in range(70):
        strip3[i] = [ int(arr3[0][i]) , int(arr3[1][i]) , int(arr3[2][i]) ]
    for i in range(70):
        strip4[i] = [ int(arr4[0][i]) , int(arr4[1][i]) , int(arr4[2][i]) ]
    for i in range(70):
        strip5[i] = [ int(arr5[0][i]) , int(arr5[1][i]) , int(arr5[2][i]) ]
    for i in range(70):
        strip6[i] = [ int(arr6[0][i]) , int(arr6[1][i]) , int(arr6[2][i]) ]

#MAINLOOP     ######################################################################              
refresh_rate  = 1 #ms
time_since_refresh = time.monotonic()

current_mode = Debug()
current_FX = Debug()

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
    
    

    if((currenttime - refresh_rate) > time_since_refresh):
        current_mode.frame_step()
        #current_mode.bpm_step()

        finish()
        
        strip1.show()
        strip2.show()
        strip3.show()
        strip4.show()
        strip5.show()
        strip6.show()
        time_since_refresh = currenttime
