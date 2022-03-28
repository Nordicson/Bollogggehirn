
import time,math,RGB1602, encoder,machine, array, rp2, gc, toolbox
from machine import Pin, UART
gc.enable()

version = "Bolloggehirn 0.4"

#TODO
#Colorsettings  <-done
#Presetsettings
#Cleaning UART (Weird Bug yay)
#FX_stars
#Documenting a bit <-done
# 

######UART########################################################################
uart = machine.UART(0,baudrate=57600,bits=8,parity=None,stop=1,rx=Pin(13),tx=Pin(12))
uart_buff = bytearray(7)

def timer():
    timer = time.ticks_ms()
    return timer

chars = ["del","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
######LCD DISPLAY##################################################################
lcd = RGB1602.RGB1602(16,2)
lcdR,lcdG,lcdB = 40,255,20
lcd.clear()
lcd.setRGB(lcdR,lcdG,lcdB)
lcd.printout("    Hello :)"  )
lcd.setCursor(0,1)
lcd.printout(version)
time.sleep(0.7)
def UpdateRow0(elements):
    #print("printing0", elements)
    lcd.setCursor(0,0)
    lcd.printout("                ")
    lcd.setCursor(0,0)
    if(type(elements) == list):
        countelem = len(elements)
        p = int(16/countelem)
        for i in range(countelem):
            lcd.setCursor(p*i,0)
            lcd.printout(elements[i])
    else:
        lcd.printout(str(elements))
    return

def UpdateRow1(elements):
    #print("printing1", elements)
    lcd.setCursor(0,1)
    lcd.printout("                ")
    lcd.setCursor(0,1)
    if(type(elements) == list):
        countelem = len(elements)
        p = int(16/countelem)
        for i in range(countelem):
            if(elements[i] != None):
                lcd.setCursor(i*p,1)
                lcd.printout(elements[i])
            
    else:
        lcd.printout(elements)
    return

def Popup(row0,row1,seconds):
    if(row0 != None):
        lcd.setCursor(0,0)
        lcd.printout("                ")
        lcd.setCursor(0,0)
        lcd.printout(row0)
    if(row1 != None):
        lcd.setCursor(0,1)
        lcd.printout("                ")
        lcd.setCursor(0,1)
        lcd.printout(row1)
    time.sleep(seconds)


#ROTARY#########################################################################
def Rot_A_Changed(change):
    global currentfunc
    if change == RotA.ROT_CCW:
        try:
            if(currentfunc.shifted == False):
                if(currentfunc.indexA < currentfunc.limA):
                    currentfunc.indexA += 1
                    currentfunc.updateA()
            elif(currentfunc.indexD < currentfunc.limD):
                currentfunc.indexD += 1
                currentfunc.updateA()
        except:
            print(currentfunc,"does not have an indexA/D that can be changed")
    elif change == RotA.ROT_CW:
        try:
            if(currentfunc.shifted == False):
                if(currentfunc.indexA > 0):
                    currentfunc.indexA -= 1
                    currentfunc.updateA()
            elif(currentfunc.indexD > 0):
                currentfunc.indexD -= 1
                currentfunc.updateA()
        except:
            print(currentfunc,"does not have an indexA/D that can be changed")
    elif change == RotA.SW_RELEASE:
        print('PRESS')
        currentfunc.onpressA()
    elif change == RotA.SW_PRESS:
        print('RELEASE')


def Rot_B_Changed(change):
    global currentfunc
    if change == RotB.ROT_CCW:
        try:
            if(currentfunc.shifted == False):
                if(currentfunc.indexB < currentfunc.limB):
                    currentfunc.indexB += 1
                    currentfunc.updateB()
            elif(currentfunc.indexE < currentfunc.limE):
                currentfunc.indexE += 1
                currentfunc.updateB()
        except:
            print(currentfunc,"does not have an indexB/E that can be changed")
    elif change == RotB.ROT_CW:
        try:
            if(currentfunc.shifted == False):
                if(currentfunc.indexB > 0):
                    currentfunc.indexB -= 1
                    currentfunc.updateB()
            elif(currentfunc.indexE > 0):
                currentfunc.indexE -= 1
                currentfunc.updateB()
        except:
            print(currentfunc,"does not have an indexB/E that can be changed")
    elif change == RotB.SW_RELEASE:
        print('PRESS')
        currentfunc.onpressB()
    elif change == RotB.SW_PRESS:
        print('RELEASE')

def Rot_C_Changed(change):
    global currentfunc
    if change == RotC.ROT_CCW:
        try:
            if(currentfunc.shifted == False):
                if(currentfunc.indexC < currentfunc.limC):
                    currentfunc.indexC += 1
                    currentfunc.updateC()
            elif(currentfunc.indexF < currentfunc.limF):
                currentfunc.indexF += 1
                currentfunc.updateC()
        except:
            print(currentfunc,"does not have an indexC/F that can be changed")
    elif change == RotC.ROT_CW:
        Rot_Changed = "C"
        try:
            if(currentfunc.shifted == False):
                if(currentfunc.indexC > 0):
                    currentfunc.indexC -= 1
                    currentfunc.updateC()
            elif(currentfunc.indexF > 0):
                currentfunc.indexF -= 1
                currentfunc.updateC()
        except:
            print(currentfunc,"does not have an indexC/F that can be changed")
    elif change == RotC.SW_RELEASE:
        print('PRESS')
        currentfunc.onpressC()
    elif change == RotC.SW_PRESS:
        print('RELEASE')

def onpressA():
    try:
        currentfunc.onpressA()
        time.sleep(0.1)
    except:
        print(currentfunc,"has not got a onpressA Function")
def onpressB():
    try:

        currentfunc.onpressB()
        time.sleep(0.1)
    except:
        print(currentfunc,"has not got a onpressB Function")
def onpressC():
    try:
        currentfunc.onpressC()
        time.sleep(0.1)
    except:
        print(currentfunc,"has not got a onpressC Function")

RotA = encoder.Rotary(2,4,3)
RotB= encoder.Rotary(5,7,6)
RotC = encoder.Rotary(8,10,9)

RotA.add_handler(Rot_A_Changed)
RotB.add_handler(Rot_B_Changed)
RotC.add_handler(Rot_C_Changed)


#MENUSTUFFS#################################################################
currentfunc = None

class menu():
    def __init__(self,name,parent,message0,message1,message_time):
        self.name = name
        self.parent = parent
        self.contents = []
        self.shifted = False
        self.indexA = 0
        self.indexB = 0
        self.indexC = 0
        self.limA = 255
        self.limB = 255
        self.limC = 255
        self.message0 = message0
        self.message1 = message1
        self.message_time = message_time

        if(parent != None):
            self.parent.add_child(self)
    def add_child(self,child):
        try:
            self.contents.append(child)
            print(self.name, "konnte", child, "als child eintragen")
        except:
            print(self.name, "konnte", child, "nicht als child eintragen")
    def onpressA(self):
        #return to parent
        global currentfunc
        try:
            if(self.parent != None):
                currentfunc = self.parent
                print(currentfunc)
                update()
        except:
            print(currentfunc,"can not reach its parent")
    def onpressB(self):
        #select content
        global currentfunc
       # try:
        currentfunc = self.contents[self.indexA]
        print(currentfunc)
        update()
       # except:
        #print(self.contents[self.indexA],"can not be selected")
        return

    def onpressC(self):
        #Maybe safe to Preset?
        return

    def update(self):
        UpdateRow0(self.name)
        UpdateRow1(self.contents[self.indexA].name)

    def updateA(self):
        UpdateRow1(self.contents[self.indexA].name)
        return

    def updateB(self):
        return
    def updateC(self):
        return


class func():
    def __init__(self,ID,name,parent):
        self.ID = ID
        self.parent = parent
        self.name = name
        self.shifted = False
        self.desc = []
        self.indexA = 0
        self.indexB = 0
        self.indexC = 0
        self.indexD = 0
        self.indexE = 0
        self.indexF = 0
        self.limA = 255
        self.limB = 255
        self.limC = 255
        self.limD = 255
        self.limE = 255
        self.limF = 255
        self.message0 = None
        self.message1 = None
        self.message_time = 0
        try:
            self.parent.add_child(self)
        except:
            print("x")
        self.special_B = None
        self.special_C = None

    def onpressA(self):
        global currentfunc
        try:
            currentfunc = self.parent
            print(currentfunc)
            update()
        except:
            print(self.name,"möchte von seinen Eltern aus Smaland abgeholt werden")
    def onpressB(self):
        if(self.special_B == None):
            if(self.shifted == False):
                self.shifted = True
                update()
            else:
                self.shifted = False
                update()
        else:
            self.special_B()
        return

    def onpressC(self):
        global uart_buff
        if self.special_C == None:
            try:
                uart_buff[0] = int(self.ID)
                uart_buff[1] = int(self.indexA)
                uart_buff[2] = int(self.indexB)
                uart_buff[3] = int(self.indexC)
                uart_buff[4] = int(self.indexD)
                uart_buff[5] = int(self.indexE)
                uart_buff[6] = int(self.indexF)
                uart.write(uart_buff)
                print("Sending: ",uart_buff)
            except:
                print(self.name,"can not execute the sending Function")
        else:
            print(self.special_C,"got triggered")
            self.special_C()

    def update(self):
        if(self.shifted == False):
            UpdateRow0([self.desc[0],self.desc[1],self.desc[2]])
            UpdateRow1([self.indexA,self.indexB,self.indexC])
        else:
            UpdateRow0([self.desc[3],self.desc[4],self.desc[5]])
            UpdateRow1([self.indexD,self.indexE,self.indexF])
        return
    def updateA(self):
        if(self.shifted == False):
            UpdateRow1([self.indexA,self.indexB,self.indexC])
        else:
            UpdateRow1([self.indexD,self.indexE,self.indexF])
        return
    def updateB(self):
        if(self.shifted == False):
            UpdateRow1([self.indexA,self.indexB,self.indexC])
        else:
            UpdateRow1([self.indexD,self.indexE,self.indexF])
        return
    def updateC(self):
        if(self.shifted == False):
            UpdateRow1([self.indexA,self.indexB,self.indexC])
        else:
            UpdateRow1([self.indexD,self.indexE,self.indexF])


def update():
    global currentfunc
    Popup(currentfunc.message0,currentfunc.message1,currentfunc.message_time)
    currentfunc.update()
    
    return

class naming_class():
    def __init__(self,parent):
        global chars
        self.parent = parent
        self.indexB = 0
        self.limB = len(chars)
        self.shifted = False
        self.desc = ["name:","add","done"]
        self.string = ""
    
    def onpressA(self):
        global currentfunc
        try:
            currentfunc = self.parent
            print(currentfunc)
            update()
        except:
            print("naming_class möchte von seinen Eltern aus Smaland abgeholt werden")
        
    def onpressB(self):
        if(self.indexB == 0 and len(self.string) > 0):
            self.string = self.string[:-1]
            self.updateB()
            return
        self.string += chars[self.indexB]
        self.updateB()
        return
    
    def onpressC(self):
        if self.parent == color_new:
            if self.string == "":
                Popup("needs a Name!","",0.7)
                self.update()
                return
            else:
                toolbox.new_color(self.parent.indexA,self.parent.indexB,self.parent.indexC,self.string)
                UART_special_delivery(200,self.parent.indexA,self.parent.indexB,self.parent.indexC,0,0,0)
                Popup("done!","",0.4)
                self.onpressA()
                self.string = ""
                self.indexB = 0
        elif self.parent == color_change_rgb:
            if self.string == "":
                Popup("needs a Name!","",0.7)
                self.update()
                return
            else:
                toolbox.change_color(color_change.indexA,self.parent.indexA,self.parent.indexB,self.parent.indexC,self.string)
                UART_special_delivery(201,self.parent.indexA,self.parent.indexB,self.parent.indexC,color_change.indexA,0,0)
                Popup("done!","",0.4)
                self.onpressA()
                self.string = ""
                self.indexB = 0
        return
    
    def update(self):
        UpdateRow0([self.desc[0],self.desc[1],self.desc[2]])
        UpdateRow1([self.string,chars[self.indexB]])
        return
    
    def updateA(self):
        return
    
    def updateB(self):
        UpdateRow1([self.string,chars[self.indexB]])
        
    def updateC(self):
        return
    
class color_wheel_class():
    def __init__(self,parent):
        self.parent = parent
        self.array = []
        self.indexA = 0
        self.limA = 255
        self.one_row = True
        self.shifted = False
    
    def onpressA(self):
        global currentfunc
        try:
            currentfunc = self.parent
            print(currentfunc)
            update()
        except:
            print("naming_class möchte von seinen Eltern aus Smaland abgeholt werden")
    
    def update(self):
        if self.one_row == True:
            UpdateRow0(["Nr.",self.indexA,self.array[self.indexA][3],""])
            UpdateRow1([self.array[self.indexA][0],self.array[self.indexA][1],self.array[self.indexA][2]])
        else:
            if(self.indexA != 0):
                UpdateRow0([self.indexA,self.array[self.indexA - 1][3],""])
                UpdateRow1([self.indexA,self.array[self.indexA][3],""])
            
    def updateA(self):
            if self.one_row == True:
                UpdateRow0(["Nr.",self.indexA,self.array[self.indexA][3],""])
                UpdateRow1([self.array[self.indexA][0],self.array[self.indexA][1],self.array[self.indexA][2]])
            else:
               if(self.indexA != 0 and self.indexA < len(self.array)):
                    UpdateRow0([self.indexA - 1,self.array[self.indexA - 1][3],""])
                    UpdateRow1([self.indexA,self.array[self.indexA][3],""])
        
def UART_special_delivery(mode_byte,byte_1,byte_2,byte_3,byte_4,byte_5,byte_6):
    try:
        uart_buff[0] = int(mode_byte)
        uart_buff[1] = int(byte_1)
        uart_buff[2] = int(byte_2)
        uart_buff[3] = int(byte_3)
        uart_buff[4] = int(byte_4)
        uart_buff[5] = int(byte_5)
        uart_buff[6] = int(byte_6)
        uart.write(uart_buff)
        print("Sending: ",uart_buff)
    except:
        print("no pizza today")
        
        

#MODES###########################################################
#Modes are inserted into menus by this func by means of
#making a function with:
#                               [] = func(ID,"Screen-name",parent)
#with ID beeing the number that will be send to the other Pico via UART.
#
#Edit the description with:     [].desc.extend((1,2,3,4,5,6))
#Set Limits A-F of index with:  [].limA = Limit
#Set Index A-F with.            [].indexA = Value

def modestruct():
    solidcolor = func(1,"1 SolidColor",modeselect)
    solidcolor.desc.extend(("R","G","B"," "," "," "))

    MultiColor = func(2,"2 Checkerbox",modeselect)
    MultiColor.desc.extend(("R","G","B","ON","OFF","FPS"))

    print(modeselect.contents)
    
    modeselect.limA = len(modeselect.contents) - 1
    return
#EFFECTS###########################################################
#Effects are inserted into menus with the "fxstruct" func by means of
#making a function with:
#                               [] = func(ID,"Screen-name",parent)
#with ID beeing the number that will be send to the other Pico via UART.
#
#Edit the description with:     [].desc.extend((1,2,3,4,5,6))
#Set Limits A-F of index with:  [].limA = Limit
#Set Index A-F with:            [].indexA = Value

def fxstruct():
    noFX = func(100,"0 No Effect",effectselect)
    noFX.desc.extend(("Nix","Nix","Nix","Nix","Nix","Nix"))

    FX_stars = func(101,"1 Star Sky",effectselect)
    FX_stars.desc.extend(("menge","size","life","pulse","moveL","moveR"))
    FX_stars.limA = 50 #Menge
    FX_stars.indexA = 20
    FX_stars.limB = 20 #Größe
    FX_stars.indexB = 2
    FX_stars.limC = 20 #Wert in sekunden?
    FX_stars.indexC = 5
    FX_stars.limD = 10 #Puls : Skala von 1 bis 10 (relativ zur größe maybe x1.1 - x2 ) 0 is off.
    FX_stars.limE = 20 #Bewegung nach Links     LEDs pro Sek/10
    FX_stars.limF = 20 #Bewegung nach Rechts, wenn beides existiert, bewegt sich der Anteil mit der Geschwindigkeit.
    #END HERE
    effectselect.limA  = len(effectselect.contents) - 1
    return
def colorstruct():
    colors = toolbox.get_colors()
    for element in colors:
        UART_special_delivery(200,element[0],element[1],element[2],0,0,0)

#Menüdefinitionen:################################################
mainmenu = menu("home menu",None,'home'," ",0.4)
AnzFarben =  35

MasterBrightness = func(255,"MasterBrightness",mainmenu)
MasterBrightness.desc.extend(("Brightness","","","","",""))
MasterBrightness.indexA = 255

BPM = func(254,"BPM",mainmenu)
BPM.desc.extend(("BPM","+BPM/10","","","",""))
BPM.indexA = 69


effectselect = menu("effectselect",mainmenu,"effects"," ",0.4)
modeselect = menu("modeselect",mainmenu,"modes"," ",0.4)
color_menu = menu("edit colors",mainmenu,"edit colors","",0.4)
preset_menu = menu("presets",mainmenu,"presets","",0.4)

mainmenu.limA = len(mainmenu.contents) - 1
print(mainmenu.contents)

#COLOR MENUSTUFFS############################################

color_new = func(200,"new color",color_menu)
color_naming = naming_class(color_new)

def color_name():
    global currentfunc
    naming_class.parent = color_new
    currentfunc = color_naming
    currentfunc.update()
    time.sleep(0.2)
    
color_new.desc.extend(("r","g","b","","",""))
color_new.special_C = color_name
#
color_change = func(201,"change color",color_menu)
color_change.desc.extend(("Nr:","Change!","","","",""))
color_change.indexB = None
color_change.indexC = None
color_change.limA = len(toolbox.get_colors()) - 1

color_change_rgb = func(202,"change_col_rgb",color_change)
color_change_rgb.desc.extend(("r","g","b","","",""))

def color_change_to_rgb():
    global currentfunc
    colors = toolbox.get_colors()
    color_change_rgb.indexA = int(colors[color_change.indexA][0])
    color_change_rgb.indexB = int(colors[color_change.indexA][1])
    color_change_rgb.indexC = int(colors[color_change.indexA][2])
    
    currentfunc = color_change_rgb
    currentfunc.update()
    print(currentfunc,"changed")
    time.sleep(0.2)
    
def color_changer():
    global currentfunc
    colors = toolbox.get_colors()
    color_naming.parent = color_change_rgb
    color_naming.string = colors[color_change.indexA][3]
    currentfunc = color_naming
    currentfunc.update()
    time.sleep(0.2)

color_change.special_C = color_change_to_rgb
color_change_rgb.special_C = color_changer

#
color_del = func(203,"delete color",color_menu)
color_del.desc.extend(("Nr:","","Delete","","",""))
color_del.indexB = None
color_del.indexC = None

def color_delete():
    colors = toolbox.get_colors()
    ID = color_del.indexA
    name = colors[ID][3]
    toolbox.del_color(ID)
    UART_special_delivery(203,ID,0,0,0,0,0)
    Popup("done!","tschau %s" %name,0.4)
    update()

color_del.special_C = color_delete
#
color_show_all = func(210,"color weel",color_menu)
color_wheel = color_wheel_class(color_show_all)

def color_one_row():
    global currentfunc
    color_wheel.one_row = True
    color_wheel.array = toolbox.get_colors()
    color_wheel.limA =len(color_wheel.array)
    currentfunc = color_wheel
    currentfunc.update()
    time.sleep(0.2)

def color_two_rows():
    global currentfunc
    color_wheel.one_row = False
    color_wheel.array = toolbox.get_colors()
    color_wheel.limA =len(color_wheel.array)
    currentfunc = color_wheel
    currentfunc.update()
    time.sleep(0.2)
    

color_show_all.desc.extend(("back","1row","2rows","","",""))
color_show_all.indexA = None
color_show_all.indexB = None
color_show_all.indexC = None
color_show_all.special_B = color_one_row
color_show_all.special_C = color_two_rows

#
#
color_menu.limA = len(color_menu.contents) - 1


#PRESET STUFF #################################
preset_new = func(220,"new preset",preset_menu)
preset_new.desc.extend(("back","name","set","","",""))
preset_new.indexA = None
preset_new.indexB = None
preset_new.indexC = None

#MAIN LOOP ###################################################

modestruct()
fxstruct()
colorstruct()

currentfunc = mainmenu
update()

breath = 0
breath_out = 0
print("Allocated:",gc.mem_alloc(),"Bytes, Free:",gc.mem_free(),"Bytes")


while(True):

    if(timer() % 100 == 0 and breath < 30):
        lcdR += 3
        lcdG -= 3
        lcd.setRGB(lcdR,lcdG,lcdB)
        #print("Setting RGB")
        breath += 1
        if(breath == 30 - 1):
            breath_out  =  30
            
    if(timer() % 100 == 0 and breath_out > 0):
        lcdR -= 3
        lcdG += 3
        lcd.setRGB(lcdR,lcdG,lcdB)
        breath_out -=1
        if(breath_out == 1):
            breath = 0