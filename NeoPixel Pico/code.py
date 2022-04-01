#Neopixel Handler, zweiter Teil des Bollogggehirn V4.0
#Die genauigkeit von time.monotonic() geht bergab nach einer stunde.

import board,busio,time,neopixel,random,math, lookup
import ulab.numpy as np

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
        self.arr1 = np.empty((70,3))
        self.arr2 = np.empty((70,3))
        self.arr3 = np.empty((70,3))
        self.arr4 = np.empty((70,3))
        self.arr5 = np.empty((70,3))
        self.arr6 = np.empty((70,3))
    
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

#0
class Debug(Mode):
    def __init__(self):
        self.id = 0
        self.par_1 = 0
        self.par_2 = 0
        self.par_3 = 0
        self.par_4 = 0
        self.par_5 = 0
        self.par_6 = 0
        self.arr1 = np.empty((70,3))
        self.arr2 = np.empty((70,3))
        self.arr3 = np.empty((70,3))
        self.arr4 = np.empty((70,3))
        self.arr5 = np.empty((70,3))
        self.arr6 = np.empty((70,3))
#1
class Mode_Solid_Color(Mode):
    def __init__(self, id, par_1, par_2, par_3, par_4, par_5, par_6):
        super().__init__(id, par_1, par_2, par_3, par_4, par_5, par_6)
        color = np.array([par_1,par_2,par_3]) 
        self.arr1[:] = color
        self.arr2[:] = color
        self.arr3[:] = color
        self.arr4[:] = color
        self.arr5[:] = color
        self.arr6[:] = color

    def new_param(self):
        color = np.array([self.par_1,self.par_2,self.par_3]) 
        self.arr1[:] = color
        self.arr2[:] = color
        self.arr3[:] = color
        self.arr4[:] = color
        self.arr5[:] = color
        self.arr6[:] = color
#2
class Mode_Checkerbox(Mode):
    def __init__(self,id, par_1, par_2, par_3, par_4, par_5, par_6):
        super().__init__(id,par_1, par_2, par_3, par_4, par_5, par_6)

        if par_4 == 0:
            par_4 = 1
        self.move_count = 0
        color = np.array([par_1,par_2,par_3])
        i = 0
        while i < 70:
            modulo = (i % (par_4 + par_5))
            if ((modulo >= 0) & (modulo < par_4)):
                self.arr1[i] = color
                self.arr2[i] = color
                self.arr3[i] = color
                self.arr4[i] = color
                self.arr5[i] = color
                self.arr6[i] = color
            i = i + 1
        
    def frame_step(self): 
  
        if self.move_count == self.par_6:
            
            new_arr1 = np.roll(self.arr1.copy(),1,axis = 0)
            self.arr1 = new_arr1.copy()
            new_arr2 = np.roll(self.arr2.copy(),1,axis = 0)
            self.arr2 = new_arr2.copy()
            new_arr3 = np.roll(self.arr3.copy(),1,axis = 0)
            self.arr3 = new_arr3.copy()
            new_arr4 = np.roll(self.arr4.copy(),1,axis = 0)
            self.arr4 = new_arr4.copy()
            new_arr5 = np.roll(self.arr5.copy(),1,axis = 0)
            self.arr5 = new_arr5.copy()
            new_arr6 = np.roll(self.arr6.copy(),1,axis = 0)
            self.arr6 = new_arr6.copy()

            self.move_count = 0
        else:
            #print(self.move_count)
            if (self.move_count > self.par_6):
                self.move_count = 0
            else:
                self.move_count += 1

    def new_param(self):
        self.arr1 = np.empty((70,3))
        self.arr2 = np.empty((70,3))
        self.arr3 = np.empty((70,3))
        self.arr4 = np.empty((70,3))
        self.arr5 = np.empty((70,3))
        self.arr6 = np.empty((70,3))

        if self.par_4 == 0:
            self.par_4 = 1
        self.move_count = 0
        color = np.array([self.par_1,self.par_2,self.par_3])
        i = 0
        while i < 70:
            modulo = (i % (self.par_4 + self.par_5))
            if ((modulo >= 0) & (modulo < self.par_4)):
                self.arr1[i] = color
                self.arr2[i] = color
                self.arr3[i] = color
                self.arr4[i] = color
                self.arr5[i] = color
                self.arr6[i] = color
            i = i + 1
#3
class Mode_Noise_One_Color(Mode):
    global colors
    def __init__(self, id, par_1, par_2, par_3, par_4, par_5, par_6):
        super().__init__(id, par_1, par_2, par_3, par_4, par_5, par_6)
        self.move_count = 0
        self.fade = np.array([1.0,1.0,1.0,1.0,1.0,1.0])
        self.fade_count = 0
        
        color = np.array([par_1,par_2,par_3])
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr1[i] = color * noise[i]
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr2[i] = color * noise[i]
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr3[i] = color * noise[i]
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr4[i] = color * noise[i]
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr5[i] = color * noise[i]
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr6[i] = color * noise[i]
    
    def new_param(self):
        color = np.array([self.par_1,self.par_2,self.par_3])
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr1[i] = color * noise[i]
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr2[i] = color * noise[i]
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr3[i] = color * noise[i]
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr4[i] = color * noise[i]
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr5[i] = color * noise[i]
        noise = lookup.get_70x_noise(random.randint(0,4))
        for i in range(70):
            self.arr6[i] = color * noise[i]
    
    def frame_step(self): 
        for i in range(6):
            if(self.fade[i] != 1.0):
                if(self.fade[i] <= 0):
                    self.fade[i] = 1.0
                else:
                    self.fade[i] -= 1/self.par_5
                    
        if self.move_count == self.par_6:
            
            new_arr1 = np.roll(self.arr1.copy(),1,axis = 0)
            self.arr1 = new_arr1.copy()
            new_arr2 = np.roll(self.arr2.copy(),1,axis = 0)
            self.arr2 = new_arr2.copy()
            new_arr3 = np.roll(self.arr3.copy(),1,axis = 0)
            self.arr3 = new_arr3.copy()
            new_arr4 = np.roll(self.arr4.copy(),1,axis = 0)
            self.arr4 = new_arr4.copy()
            new_arr5 = np.roll(self.arr5.copy(),1,axis = 0)
            self.arr5 = new_arr5.copy()
            new_arr6 = np.roll(self.arr6.copy(),1,axis = 0)
            self.arr6 = new_arr6.copy()

            self.move_count = 0
        else:
            #print(self.move_count)
            if (self.move_count > self.par_6):
                self.move_count = 0
            else:
                self.move_count += 1
    def get_arrays(self):
        new_arr1 = self.arr1 * self.fade[0]
        new_arr2 = self.arr2 * self.fade[1]
        new_arr3 = self.arr3 * self.fade[2]
        new_arr4 = self.arr4 * self.fade[3]
        new_arr5 = self.arr5 * self.fade[4]
        new_arr6 = self.arr6 * self.fade[5]
        
        
        return new_arr1,new_arr2,new_arr3,new_arr4,new_arr5,new_arr6
    def bpm_step(self):
        if(self.par_5 == 0):
            return
        if(self.fade_count == 6):
            self.fade_count = 0
        
        self.fade[self.fade_count] -= 1/self.par_5
        self.fade_count += 1
        

#NEW DATA ##############################
def new_data():
    #All modes need to be checked in at the new_data lobby, from witch 
    global incoming
    global current_mode
    id = incoming[0]
    
    if(id == 0):
        print("debug")
    elif(id == 200):
        color_new(incoming[1],incoming[2],incoming[3])
    elif(id == 201):
        color_change(incoming[1],incoming[2],incoming[3],incoming[4])
    elif(id == 203):
        color_del(incoming[1])
    elif(id == 254):
        change_BPM(incoming[1],incoming[2])
    elif(id == 255):
        change_master_brightness(incoming[1])
        
    
    elif(id > 0 & id < 100):
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
    
    

def find_mode(data):
    #finds the corrisponding mode and initialises its class as current_mode
    id = data[0]
    if(id == 1):
        return Mode_Solid_Color(id,data[1],data[2],data[3],data[4],data[5],data[6])
    if(id == 2):
        return Mode_Checkerbox(id,data[1],data[2],data[3],data[4],data[5],data[6])
    if(id == 3):
        return Mode_Noise_One_Color(id,data[1],data[2],data[3],data[4],data[5],data[6])

# TOOLS ################################

def change_BPM(BPM_new,tenth):
    global BPM
    BPM = BPM_new + tenth/10
    print(BPM)

def change_master_brightness(data):
    global master_brightness
    master_brightness = data/255
    print(master_brightness)

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
    global master_brightness
    arr1,arr2,arr3,arr4,arr5,arr6 = current_mode.get_arrays()
    new1 = arr1 * master_brightness
    new2 = arr2 * master_brightness
    new3 = arr3 * master_brightness
    new4 = arr4 * master_brightness
    new5 = arr5 * master_brightness
    new6 = arr6 * master_brightness 
    
    for i in range(70):
        test = new1[i].tolist()
        strip1[i] = test
        test = new2[i].tolist()
        strip2[i] = test
        test = new3[i].tolist()
        strip3[i] = test
        test = new4[i].tolist()
        strip4[i] = test
        test = new5[i].tolist()
        strip5[i] = test
        test = new6[i].tolist()
        strip6[i] = test

        

#MAINLOOP     ######################################################################              
refresh_rate  = 0 #s
time_since_refresh = time.monotonic()
time_since_bpm = time.monotonic()
current_mode = Debug()
current_FX = Debug()

while(True):
    currenttime = time.monotonic()

    #DER FUCKING INPUTHANDLER
    data = uart.read(1)
    if(data != None):
        incoming = [0 for i in range(7)]
        incoming[0] = int.from_bytes(data,"big")
        incoming[1] = int.from_bytes(uart.read(1),"big")
        incoming[2] = int.from_bytes(uart.read(1),"big")
        incoming[3] = int.from_bytes(uart.read(1),"big")
        incoming[4] = int.from_bytes(uart.read(1),"big")
        incoming[5] = int.from_bytes(uart.read(1),"big")
        incoming[6] = int.from_bytes(uart.read(1),"big")
        print(incoming)
        new_data()
    
    

    if((time_since_refresh + refresh_rate) < currenttime):
        
        current_mode.frame_step()
        
        if((time_since_bpm + (60/BPM) < currenttime)):
            current_mode.bpm_step()
            print("Beat")
            time_since_bpm = currenttime
        
        #starttime = time.monotonic()
        finish()
        #endtime = time.monotonic()
        #print(endtime - starttime)
        strip1.show()
        strip2.show()
        strip3.show()
        strip4.show()
        strip5.show()
        strip6.show()
        time_since_refresh = currenttime
