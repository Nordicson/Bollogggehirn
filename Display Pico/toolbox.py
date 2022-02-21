import random

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
    
def fill_up(n):
    ffunny_names = ["amber","amethyst","bronze","chartreuse","burgundy"]
    for i in range(n):
        new_color(random.randint(0,255),random.randint(0,255),random.randint(0,255),ffunny_names[random.randint(0,len(ffunny_names))])

if(__name__ == "__main__"):
    running = True
    while(running == True):
        a = input("-new -change quit")
        if(a == "-new"):
            r = input("r:")
            g = input("g:")
            b = input("b:")
            name = input("name:")
            new_color(r,g,b,name)
        elif(a == "-change"):
            ID = input("ID:")
            r = input("r:")
            g = input("g:")
            b = input("b:")
            name = input("name:")
            change_color(ID,r,g,b,name)
        elif(a == "quit"):
            running = False
            break