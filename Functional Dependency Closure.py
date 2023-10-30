from tkinter import *
 
temdic = {}
anss = ""

#29F4B2 --> Mint Green
#2471A3 --> Navy
#1A5276 --> Navy 2
#AF97EA --> Light Purple
 
root = Tk()
# BACKGROUND = "#CCEDFF" # Light Blue
# BACKGROUND = "#29F4B2" # Mint Green
# BACKGROUND = "#2471A3" # Navy
# BACKGROUND = "#1A5276" # Navy 2
# BACKGROUND = "#AF97EA" # Light Purple
BACKGROUND = "#212F3D" # Black
SECONDARY = "#E5E7E9" # Light Gray
TERTIARY = "#D5DBDB" # Shades of Gray

root.configure(bg=BACKGROUND)

def string_comp(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    if len(s1) != len(s2):
        return False
    list1 = set(list1)
    list2 = set(list2)
    return list1 == list2
 
def hoja():
    temans = getvals()
    L["text"] = temans

def khali_hoja():
    temdic.clear()
    text1.delete("1.0","end")
    text2.delete("1.0","end")
    L["text"] = ""
    pass
 
def getvals():
    to_be_found = text2.get("1.0", END).splitlines()
    # print(to_be_found)
    tem_fd = text1.get("1.0", END).splitlines()
    xlist = []
    ylist = []
 
    for s in tem_fd:
        tem = s.split("->")
        xlist.append(tem[0])
        ylist.append(tem[1])
    # print(xlist)
    # print(ylist)

    for x, y in zip(xlist, ylist):
        if x not in temdic.keys(): 
            lst = []
            for let in x:
                lst.append(let)
            temdic[x] = lst
 
        for letter in y:
            if letter not in temdic[x]:
                temdic[x].append(letter)
 
        for key in temdic.keys():
            tem = []
            for let in key:
                tem.append(let)
 
            for vals in temdic[key]:
                if vals in temdic.keys():
                    tem += (temdic[vals])
                else:
                    tem += (temdic[key])
 
            temdic[key] = tem
            temdic[key] = set(temdic[key])
            temdic[key] = list(temdic[key])
 
            n = len(temdic[key])
            #x->abcde
            # 10 = 0b1010

            # x<<y = x*(2^y)
            
            mxlen = len(str(bin(1 << n))) - 2      #2^n
 
            for i in range(1 << n):
                num = bin(i)  #7 0b111
                num = str(num) 
                temkey = num[2:] #7 = 111
                temlen = len(temkey)
                zeros = ""
                for i in range(mxlen - temlen - 1):
                    zeros += '0'
                temkey = zeros + temkey #00111
                newkey = ""
                for (a, b) in zip(temkey, temdic[key]):
                    if a == '1':
                        newkey += b
                keylist = list(temdic.keys())
                for ind in range(len(keylist)):
                    if string_comp(keylist[ind], newkey) == True: #cde in dict and dec in newkey
                        temdic[key] += temdic[keylist[ind]]
                        break

    # print(temdic)

    # print(temdic)
    
    ansdic = {}
    for s in to_be_found:
        curst = []
        for let in s:
            if let in temdic:
                curst.extend(temdic[let])
            else:
                curst.extend(let)
                temdic[let] = set(let)
        tempkey = list(set(curst))
        ansdic[s] = curst
        # print(ansdic[s])
        n=len(tempkey)
        mxlen = len(str(bin(1 << n))) - 2
        for i in range(1 << n):
            num = bin(i)
            num = str(num)
            temkey = num[2:]
            temlen = len(temkey)
            zeros = ""
            for i in range(mxlen - temlen - 1):
                zeros += '0'
            temkey = zeros + temkey
            newkey = ""
            for (a, b) in zip(temkey, tempkey):
                if a == '1':
                    newkey += b
            # print(newkey)
            keylist = list(temdic.keys())
            for ind in range(len(keylist)):
                if string_comp(keylist[ind], newkey) == True:
                    # print(ansdic[s])
                    # print(temdic[keylist[ind]])
                    ansdic[s] += temdic[keylist[ind]]

    for key in ansdic.keys():
        ansdic[key] = set(ansdic[key])

    # print(ansdic)
    anss = str(ansdic)
    
    temanss = ""
    for ind in range(1, len(anss)-1):
        if(ind>0 and anss[ind]==',' and anss[ind-1]=='}'):
            temanss += '\n'
        else: temanss += anss[ind]
 
    return temanss


 
 
root.title("FD Closure")
root.geometry("900x600")
root.resizable(0, 0)
 
#frame1
f1 = Frame(root, height=130, width=900, pady=10, bg=BACKGROUND)
f1.pack(fill=X)
Label(f1, text="ENTER FUNCTIONAL DEPENDENCIES", bg=BACKGROUND, width=0, padx=160, font="Ubuntu 25 bold", foreground=SECONDARY).grid(row=0, column=0)
  
f2 = Frame(root, height=220, width=800, pady=10, bg=BACKGROUND)
#scrollbar
sc_y = Scrollbar(f2, orient=VERTICAL)
sc_y.pack(side=RIGHT, fill = Y)
 
text1 = Text(f2, height=150, width=700, background=TERTIARY, font="Calibiri 15")
text1.pack()
f2.pack_propagate(0)
f2.pack()
sc_y.config()
 
f3 = Frame(root, height=130, width=900, pady=10, padx=20, bg=BACKGROUND)
f3.pack(fill=X)
Label(f3, text="ENTER ATTRIBUTES\t\t         CLOSURE", bg=BACKGROUND, width=0, font="Ubuntu 20 bold", foreground=SECONDARY).pack(side=LEFT)
 
f4 = Frame(root, height=250, width=250, padx=25, bg=BACKGROUND)
sc_y4 = Scrollbar(f4, orient=VERTICAL)
sc_y4.pack(side=RIGHT, fill = Y)
 
text2 = Text(f4, height=150, width=100, background=TERTIARY, font="Calibiri 15")
text2.pack()
f4.pack_propagate(0)
f4.pack(side=LEFT, padx=30)
sc_y4.config()
 
f5 = Frame(root, height=220, width=100)
f5.pack(side=LEFT)
 
f6 = Frame(root, height=250, width=440, padx=10, bg=BACKGROUND) 
 
L = Label(f6, bg=TERTIARY, text=anss, width=500, height=250,padx=25, font="Calibiri 15 bold")
L.pack(fill=X)

f6.pack_propagate(0)
f6.pack(side=LEFT, padx=10)
 
b = Button(f5, text="FIND", font="Times 12 bold", command = hoja, width=10, bg=SECONDARY, foreground=BACKGROUND).pack(side=LEFT)  
b = Button(f5, text="RESET", font="Times 12 bold", command = khali_hoja, width=10, bg=SECONDARY, foreground=BACKGROUND).pack(side=LEFT)  
 
def run():
    root.mainloop()
 
if __name__ == '__main__':
    run()