
import time,math,RGB1602, encoder,machine, array, rp2, gc, toolbox
from machine import Pin, UART
gc.enable()

version = "Bolloggehirn 0.4"

#TODO
#Preset player
#Presetsettings
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
class element():
    def __init__(self,name,parent):
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
                currentfunc.update()
        except:
            print(currentfunc,"can not reach its parent")
    def onpressB(self):
        return
    def onpressC(self):
        return
    def update(self):
        return
    def updateA(self):
        return
    def updateB(self):
        return
    def updateC(self):
        return


    

class menu(element):
    def __init__(self, name, parent):
        super().__init__(name, parent)

    def onpressB(self):
        #select content
        global currentfunc
        currentfunc = self.contents[self.indexA]
        print(currentfunc)
        currentfunc.update()

    def update(self):
        UpdateRow0(self.name)
        UpdateRow1(self.contents[self.indexA].name)

    def updateA(self):
        UpdateRow1(self.contents[self.indexA].name)

class menu_with_preset(menu):
    def __init__(self, name, parent):
        super().__init__(name, parent)

    def update(self):
        UpdateRow0([self.name,">Pre"])
        UpdateRow1(self.contents[self.indexA].name)
    
    def onpressC(self):
        global currentfunc
        currentfunc = preset_add_external("preset_add_external",self,[self.indexA,self.contents[self.indexA].indexA],self.contents[self.indexA].indexB,self.contents[self.indexA].indexC,self.contents[self.indexA].indexD,self.contents[self.indexA].indexE,self.contents[self.indexA].indexF)
        currentfunc.update()


class func(element):
    def __init__(self,ID, name, parent):
        super().__init__(name, parent)
        self.desc = []
        self.ID = ID
        self.indexD = 0
        self.indexE = 0
        self.indexF = 0
        self.limD = 255
        self.limE = 255
        self.limF = 255
        try:
            self.parent.add_child(self)
        except:
            print("something went terribly wrong when ",name,"tried to add itself as a child")
    
    def onpressB(self):
        if(self.shifted == False):
            self.shifted = True
            self.update()
        else:
            self.shifted = False
            self.update()


    def onpressC(self):
        UART_special_delivery(self.ID,self.indexA,self.indexB,self.indexC,self.indexD,self.indexD,self.indexE,self.indexF)

    def update(self):
        if(self.shifted == False):
            UpdateRow0([self.desc[0],self.desc[1],self.desc[2]])
            UpdateRow1([self.indexA,self.indexB,self.indexC])
        else:
            UpdateRow0([self.desc[3],self.desc[4],self.desc[5]])
            UpdateRow1([self.indexD,self.indexE,self.indexF])
    
    def refresh_numbers(self):
        if(self.shifted == False):
            UpdateRow1([self.indexA,self.indexB,self.indexC])
        else:
            UpdateRow1([self.indexD,self.indexE,self.indexF])

    def updateA(self):
        self.refresh_numbers()

    def updateB(self):
        self.refresh_numbers()

    def updateC(self):
        self.refresh_numbers()

class naming_class(element):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        global chars
        self.limB = len(chars)
        self.desc = ["name:","add","done"]
        self.string = ""

    def onpressB(self):
        if(self.indexB == 0 and len(self.string) > 0):
            self.string = self.string[:-1]
            self.updateB()
            return
        self.string += chars[self.indexB]
        self.updateB()
        return
    
    def onpressC(self):
        if self.string == "":
            Popup("needs a Name!","",0.7)
            self.update()
            return
        else:
            self.parent.naming_return = self.string
            self.string = ""
            self.indexB = 0
            self.parent.set_with_naming()
            Popup("done!","",0.4)
            self.onpressA()
            
            
            
    
    def update(self):
        UpdateRow0([self.desc[0],self.desc[1],self.desc[2]])
        UpdateRow1([self.string,chars[self.indexB]])
        return
    
    def updateB(self):
        UpdateRow1([self.string,chars[self.indexB]])
    
class color_wheel_class(element):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.array = []
        self.one_row = True
    
    def onpressA(self):
        global currentfunc
        try:
            currentfunc = self.parent
            print(currentfunc)
            currentfunc.update()
        except:
            print("color_wheel möchte von seinen Eltern aus Smaland abgeholt werden")
    def onpressB(self):
        return
    def onpressC(self):
        return
    
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
        time.sleep(0.2)
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
    
    OneColorNoise = func(3, "3 OneColorNoise",modeselect)
    OneColorNoise.desc.extend(("R","G","B"," "," ","FPS"))

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

""" def fxstruct():
    noFX = func(100,"0 No Effect",effectselect)
    noFX.desc.extend(("Nix","Nix","Nix","Nix","Nix","Nix"))

    FX_mask_stars = func(101,"1 Stars",effectselect)
    FX_mask_stars.desc.extend(("Menge","size","life"," "," "," "))
    FX_mask_stars.limA = 50 #Amount
    FX_mask_stars.indexA = 20
    FX_mask_stars.limB = 20 #Size
    FX_mask_stars.indexB = 2
    FX_mask_stars.limC = 100 #Life in Frames
    FX_mask_stars.indexC = 20

    #END HERE
    effectselect.limA  = len(effectselect.contents) - 1
    return
    """
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


#effectselect = menu("effectselect",mainmenu,"effects"," ",0.4)
modeselect = menu("modeselect",mainmenu)
color_menu = menu("edit colors",mainmenu)
preset_menu = menu("presets",mainmenu)

mainmenu.limA = len(mainmenu.contents) - 1
print(mainmenu.contents)

#COLOR MENUSTUFFS############################################
class color_new_class(func):
    def __init__(self, ID, name, parent):
        super().__init__(ID, name, parent)
        self.desc.extend(("r","g","b","","",""))
        self.naming_return = ""
        self.indexA = None
        self.indexB = None
        self.indexC = None

    def onpressB(self):
        return
    def onpressC(self):
        naming_color = naming_class("color_naming",self)
        currentfunc = naming_color
        currentfunc.update()
    def set_with_naming(self):
        toolbox.new_color(self.indexA,self.indexB,self.indexC,self.naming_return)
        UART_special_delivery(self.ID,self.indexA,self.indexB,self.indexC,0,0,0)

color_new = color_new_class(200,"new color",color_menu)

class color_change_class(func):
    def __init__(self, ID, name, parent):
        super().__init__(ID, name, parent)
        self.desc.extend(("Nr:","Change!"," ","","",""))
        self.colors = []
        self.indexB = None
        self.indexC = None
        self.limA = len(toolbox.get_colors()) - 1
    
    def update(self):
        self.colors = toolbox.get_colors()
        UpdateRow0([self.desc[0],self.desc[1],self.desc[2]])
        UpdateRow1([self.indexA,self.colors[self.indexA][3]])

    def updateA(self):
        UpdateRow1([self.indexA,self.colors[self.indexA][3]])
    
    def onpressB(self):
        global currentfunc
        color_change_to_rgb.set_color(self.indexA,self.colors[self.indexA][0],self.colors[self.indexA][1],self.colors[self.indexA][2],self.colors[self.indexA][3])
        currentfunc = color_change_to_rgb
        currentfunc.update()
        return

    def onpressC(self):
        return

class color_change_to_rgb_class(func):
    def __init__(self, ID, name, parent):
        super().__init__(ID, name, parent)
        self.desc.extend(("r","g","b","","",""))
        self.naming_return = ""
        self.nr = None
    
    def set_color(self,nr,r,g,b,name):
        self.nr = nr
        self.indexA = r
        self.indexB = g
        self.indexC = b
        self.naming_return = name
    def onpressB(self):
        return

    def onpressC(self):
        global currentfunc
        color_change_naming = naming_class("color_change_naming",self)
        color_change_naming.string = self.naming_return
        currentfunc = color_change_naming
        currentfunc.update()

    def set_with_naming(self):
        toolbox.change_color(self.nr,self.indexA,self.indexB,self.indexC,self.naming_return)
        UART_special_delivery(201,self.indexA,self.indexB,self.indexC,self.nr,0,0)
        Popup("done!"," ",0.5)
        self.onpressA()

color_change = color_change_class(201,"change color",color_menu)
color_change_to_rgb = color_change_to_rgb_class(202,"change color rgb",color_change)

class color_del_class(func):
    def __init__(self, ID, name, parent):
        super().__init__(ID, name, parent)
        self.indexB = None
        self.indexC = None
        self.desc.extend(("Nr:","","Delete","","",""))
        self.colors = []
    
    def update(self):
        self.colors = toolbox.get_colors()
        UpdateRow0([self.desc[0],self.desc[1],self.desc[2]])
        UpdateRow1([self.indexA,self.colors[self.indexA][3]])
    def updateA(self):
        UpdateRow1([self.indexA,self.colors[self.indexA][3]])
    def updateB(self):
        return
    def updateC(self):
        return
    def onpressB(self):
        return
    
    def onpressC(self):
        name = self.colors[self.indexA][3]
        UART_special_delivery(203,self.indexA,0,0,0,0,0)
        toolbox.del_color(self.indexA)
        Popup("done!","tschau %s" %name,0.4)
        self.update()

color_del = color_del_class(203,"delete color",color_menu)

class color_show_all_class(element):
    def __init__(self,name, parent):
        super().__init__(name, parent)
        self.desc.extend(("<-","1row","2rows","","",""))
        self.indexA = None
        self.indexB = None
        self.indexC = None
    def update(self):
        UpdateRow0(self.desc[0],self.desc[1],self.desc[2])
    
    def onpressB(self):
        color_one_row()
    def onpressC(self):
        color_two_rows()


color_show_all = color_show_all_class("color weel",color_menu)
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
#
#
color_menu.limA = len(color_menu.contents) - 1


#PRESET STUFF #################################
class preset_new_class(element):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.desc = []
        self.desc.extend(("<-","name","set"))
        self.naming_return = ""
    
    def update(self):
        UpdateRow0([self.desc[0],self.desc[1],self.desc[2]])
        UpdateRow1(["Name:",self.naming_return])

    def onpressB(self):
        global currentfunc
        preset_naming = naming_class("preset_naming",self)
        currentfunc = preset_naming
        currentfunc.update()
    
    def onpressC(self):
        if self.naming_return != "":
            r = toolbox.new_preset_file(self.naming_return)
            if r == False:
                Popup("Name already taken","Try again",0.7)
        else:
            Popup("Please give the","Preset a Name!", 0.7)
    
    def set_with_naming(self):
        return

preset_new = preset_new_class("new preset",preset_menu)

class preset_del_class(func):
    def __init__(self, ID, name, parent):
        super().__init__(ID, name, parent)
        self.indexB = None
        self.indexC = None
        self.indexA = None
        self.filename = ""

    def update(self):
        UpdateRow0("<-"," ","delete")
        UpdateRow1(self.filename)
    def onpressB(self):
        return
    def onpressC(self):
        r = toolbox.del_preset_file(self.filename)
        if r == False:
            print("something went terribly wrong while deleting a preset file")
        self.onpressA()

class preset_peek_class(menu):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.filename = ""
        self.steps = []
        self.option = 0
        self.naming_return = ""
        self.limB = 3
        self.limC = len(modeselect.contents) - 1
        self.mode = "???"
    
    def update(self):
        self.steps = toolbox.get_preset_content(self.filename)
        self.limA = len(self.steps) - 1
        self.mode = modeselect.contents[self.steps[self.indexA][1]].name
        self.indexC = self.steps[self.indexA][1]

        if len(self.steps == 0):
            UpdateRow0("Preset is empty")
            UpdateRow1("")
        else:
            if(self.option == 0):
                UpdateRow0(["<-","option>","rename"])
                UpdateRow1(self.filename)
            if(self.option == 1):
                UpdateRow0(["<-","option>","delete"])
                UpdateRow1(["Step:",self.indexA])
            if(self.option == 2):
                UpdateRow0(["<-","option>","mode"])
                UpdateRow1(["Step:",self.indexA,self.mode])
            if(self.option == 3):
                UpdateRow0(["<-","option>","data"])
                UpdateRow1(["Step:",self.indexA,self.mode])

    def updateB(self):
        self.option == self.indexB
    
    def updateC(self):
        if self.option == 2:
            self.mode = modeselect.contents[self.indexC].name
            UpdateRow1(["Step:",self.indexA,self.mode])

    def onpressB(self):
        return

    def onpressC(self):
        if self.option == 0:
            global currentfunc
            preset_rename = naming_class(self.filename,self)
            currentfunc = preset_rename
            currentfunc.update()
        elif(self.option == 1):
            try:
                toolbox.del_preset_line(self.filename,self.indexA)
                Popup("done!","",0.5)
                self.update()
            except:
                Popup("Something is wrong","is it empty?",0.7)
                self.update()
        elif(self.option == 2):
            try:
                toolbox.change_preset_line(self.filename,self.indexA,self.steps[self.indexA][0],self.indexC,self.steps[self.indexA][2],self.steps[self.indexA][3],self.steps[self.indexA][4],self.steps[self.indexA][5],self.steps[self.indexA][6],self.steps[self.indexA][7])
                self.update()
            except:
                Popup("Something went wrong","changing line",0.7)
                self.update()
        elif(self.option == 3):
            global currentfunc
            preset_data = preset_data_class(230,self.mode,self,self.filename,self.indexA,self.steps[self.indexA][0],self.indexC)
            preset_data.desc.extend(modeselect.contents[self.indexC].desc)
            preset_data.indexA = self.steps[self.indexA][2]
            preset_data.indexB = self.steps[self.indexA][3]
            preset_data.indexC = self.steps[self.indexA][4]
            preset_data.indexD = self.steps[self.indexA][5]
            preset_data.indexE = self.steps[self.indexA][6]
            preset_data.indexF = self.steps[self.indexA][7]

            currentfunc = preset_data
            currentfunc.update()

            
    def set_with_naming(self):
        r = toolbox.rename_preset_file(self.filename,self.naming_return)
        if r == False:
            Popup("Name is taken","Try again",0.7)
        return

    def onpressB(self):
        if self.shifted == False:
            self.shifted = True
        else:
            self.shifted = False

class preset_data_class(func):
    def __init__(self, ID, name, parent,filename,linenr,time,mode):
        super().__init__(ID, name, parent)
        self.filename = filename
        self.linenr = linenr
        self.time = time
        self.mode = mode
        self.limA = modeselect.contents[mode].limA
        self.limB = modeselect.contents[mode].limB
        self.limC = modeselect.contents[mode].limC
        self.limD = modeselect.contents[mode].limD
        self.limE = modeselect.contents[mode].limE
        self.limF = modeselect.contents[mode].limF

    def onpressC(self):
        try:
            toolbox.change_preset_line(self.filename,self.linenr,self.time,self.mode,self.indexA,self.indexB,self.indexC,self.indexD,self.indexE,self.indexF)
        except: 
            Popup("Something went wrong","changing data",0.7)
        self.onpressA()
    

class preset_browse_class(menu):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.preset_arr = []
        self.indexB = None
        self.indexC = None

    def update(self):
        self.preset_arr = toolbox.get_preset_files()
        self.limA = len(self.preset_arr) - 1
        if(len(self.preset_arr) == 0):
            UpdateRow0("No presets")
            UpdateRow1("___~* ___~*___Y___")
        else:
            UpdateRow0(["<-","peek","del"])
            UpdateRow1([self.indexA,self.preset_arr[self.indexA]])
    
    def updateA(self):
        if(len(self.preset_arr) == 0):
            UpdateRow0("No presets")
            UpdateRow1("____~~* __~~*_Y___")
        else:
            UpdateRow1([self.indexA,self.preset_arr[self.indexA]])
    
    def onpressB(self):
        global currentfunc
        preset_peek = preset_peek_class("preset_peek",self)
        preset_peek.filename = self.preset_arr[self.indexA]
        currentfunc = preset_peek
        currentfunc.update()
        return
    
    def onpressC(self):
        global currentfunc
        preset_del = preset_del_class(221,"preset_del",self)
        preset_del.filename = self.preset_arr[self.indexA]
        currentfunc = preset_del
        currentfunc.update()

preset_browse = preset_browse_class("preset_browse",preset_menu)

class preset_add_external(menu):
    def __init__(self, name, parent,data):
        super().__init__(name, parent)
        self.data = data
        self.presets  = []
        
    
    def update(self):
        self.presets = toolbox.get_preset_files()
        self.limA = len(self.presets) - 1
        if self.limA == 0:
            global currentfunc
            Popup("No Presets","Go make 1",1)
            currentfunc = preset_new
            currentfunc.update()
        else:
            UpdateRow0("Time:",self.indexB,">Done")
            UpdateRow1(["Add to:",self.presets[self.indexA]])
    
    def updateA(self):
        UpdateRow1(self.presets[self.indexA])
    
    def onpressC(self):
        try:
            toolbox.add_preset_line(self.presets[self.indexA],self.indexB,self.data[0],self.data[1],self.data[2],self.data[3],self.data[4],self.data[5],self.data[6])
        except:
            Popup("Something went wrong","adding to preset",0.7)
        self.onpressA()
#MAIN LOOP ###################################################

modestruct()
#fxstruct()
colorstruct()

currentfunc = mainmenu
currentfunc.update()

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