import os
def get_colors():
    col_arr = []
    with open("colors.txt","r") as color_text:
        for lines in color_text:
            line_clean = lines.strip("\n")
            splitted = line_clean.split(",")
            col_arr.append(splitted)
    return col_arr

def set_colors(col_arr):
    string = ""
    for i in range(len(col_arr)):
        string += str(col_arr[i][0])
        string += ","
        string += str(col_arr[i][1])
        string += ","
        string += str(col_arr[i][2])
        string += ","
        string += str(col_arr[i][3])
        string += "\n"
    with open("colors.txt","w") as color_text:
        color_text.write(string)
    return
def del_color(ID):
    col_arr = get_colors()
    col_arr.pop(ID)
    set_colors(col_arr)
    return

def new_color(r,g,b,name):
    col_arr = get_colors()
    col_arr.append([r,g,b,name])
    set_colors(col_arr)
    return

def change_color(ID , new_r , new_g , new_b , new_name):
    col_arr = get_colors()
    ID = int(ID)
    if(new_name != None):
        col_arr[ID] = [new_r , new_g , new_b , new_name]
        set_colors(col_arr)
    else:
        col_arr[ID][0] = new_r
        col_arr[ID][1] = new_g
        col_arr[ID][2] = new_b
        set_colors(col_arr)
    return

#PRESETS######################################################


def get_preset_files():
    
    presets = os.listdir("presets")
    return presets

def new_preset_file(filename):
    os.chdir("presets")
    try:
        with open(filename,"x"):
            os.chdir("..")
            return True
    except:
        os.chdir("..")
        print("filename exists already")
        return False
        
def del_preset_file(filename):
    os.chdir("presets")
    try:
        os.remove(filename)
        os.chdir("..")
        return True
    except:
        os.chdir("..")
        print("can not delete", filename)
        return False
    
def get_preset_content(filename):
    os.chdir("presets")
    content = []
    with open(filename,"r") as file:
        for lines in file:
            line_clean = lines.strip("\n")
            line_clean = line_clean.strip("\r")
            splitted = line_clean.split(",")
            content.append(splitted)
    os.chdir("..")
    return content

def set_preset_content(filename,content):
    os.chdir("presets")
    string = ""
    for i in range(len(content)):
        string += str(content[i][0]) #time_from_start
        string += ","
        string += str(content[i][1]) #mode
        string += ","
        string += str(content[i][2]) #0
        string += ","
        string += str(content[i][3]) #1
        string += ","
        string += str(content[i][4]) #2
        string += ","
        string += str(content[i][5]) #3
        string += ","
        string += str(content[i][6]) #4
        string += ","
        string += str(content[i][7]) #5
        string += "\n"
    with open(filename,"w") as file:
        file.write(string)
    os.chdir("..")
        
def add_preset_line(filename,time,mode,par_0,par_1,par_2,par_3,par_4,par_5):
    content = get_preset_content(filename)
    content.append([time,mode,par_0,par_1,par_2,par_3,par_4,par_5])
    set_preset_content(filename,content)
    
def del_preset_line(filename,line_nr):
    content = get_preset_content(filename)
    content.pop(line_nr)
    set_preset_content(filename,content)

def change_preset_line(filename,line_nr,time,mode,par_0,par_1,par_2,par_3,par_4,par_5):
    content = get_preset_content(filename)
    line_nr = int(line_nr)
    content[line_nr] = [time,mode,par_0,par_1,par_2,par_3,par_4,par_5]
    set_preset_content(filename,content)

    
if(__name__ == "__main__"):
    nix = None
#     new_preset_file("new_preset1.txt")
#     change_preset_line("new_preset1.txt",0,3,0,1,1,1,1,1,1)
#     print(get_preset_files())
#     print(get_preset_content("new_preset1.txt"))