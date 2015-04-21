
from __future__ import division
import Tkinter
from Tkinter import *
import tkMessageBox

List=[]
list2=[]
V_W=[]
#=======================================================================================================================
#=======================================================================================================================
#---------------------------------------------> Remove one Letter     <-------------------------------------------------
def Remove_1_Letter(word):
    for x in range(0,len(word)):
        s=''
        for xx in range(0,len(word)):
            if xx == x:
                continue
            else:
                s=s+word[xx]
        List.append(s)
#=======================================================================================================================
#=======================================================================================================================
#------------------------------------------> Swap two adjacent Letters   <----------------------------------------------
def split_string(word):
    ww=[]
    for x in range(0,len(word)):
         ww.append(word[x])
    return  ww
#-----------------------------------------------------------------------------------------------------------------------
def join_string(ww):
     ss=''
     for x in range(0,len(ww)):
         ss +=ww[x]
     return ss
#-----------------------------------------------------------------------------------------------------------------------
def swap(www,x):
    temp=''
    temp=www[x+1]
    www[x+1]=www[x]
    www[x]=temp
    return www
#-----------------------------------------------------------------------------------------------------------------------
def swap_2_adjacent(word):
    for x in range(0,len(word)-1):
        www=split_string(word)                                           #*************
        ww=swap(www,x)                                                   #*************
        ss=join_string(ww)                                               #*************
        List.append(ss)
#=======================================================================================================================
#=======================================================================================================================
#-----------------------------------------------> Change one Letter   <-------------------------------------------------
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def change_1_Letter(word):
    for x in range(0,len(word)):
        for xx in range(0,len(alphabet)):
            www=split_string(word)                                           #*************
            www[x]=alphabet[xx]
            ss=join_string(www)                                              #*************
            List.append(ss)
#=======================================================================================================================
#=======================================================================================================================
#--------------------------------------------------> Add one Letter   <-------------------------------------------------
def add_1_Letter(word):
    for x in range(0,len(word)+1):
        for xx in range(0,len(alphabet)):
            www=split_string(word)                                           #*************
            www.insert(x,alphabet[xx])
            ss=join_string(www)                                              #*************
            List.append(ss)
#=======================================================================================================================
#=======================================================================================================================
#-----------------------------------------------> First edit on word  <-------------------------------------------------
def first_edit(word):
    del List[:]
    Remove_1_Letter(word)
    swap_2_adjacent(word)
    change_1_Letter(word)
    add_1_Letter(word)
#/////////////////////////////
#//////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////
#/////////////////////////////
def second_edit():
    for x in range(0,len(List)):
        first_edit(List[x])
#=======================================================================================================================
#=======================================================================================================================
#--------------------------------------------------> Read Dictionary  <-------------------------------------------------
def Read_dictionary():
     file=open("D:\\dictionary.txt","r")
     dictionary=[]
     while True:
         wo=file.readline()
         if wo=="":
             break
         else:
             dictionary.append(wo[0:len(wo)-1].lower())
     file.close()
     return dictionary
d=Read_dictionary()
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#=======================================================================================================================
#=======================================================================================================================
#------------------------------------------> valid words in Dictionary<-------------------------------------------------
'''def valid_words():
    d=Read_dictionary()
    list2=[]
    for w in range(0,len(List)):
        for x in range(0,len(d)):
            if List[w]==d[x]:
                  list2.append(List[w])
                  print(List[w])
    return list2'''
#=======================================================================================================================
#=======================================================================================================================
#------------------------------------------> valid words if unique<-------------------------------------------------
def unique(w):
    for x in list2:
        if w ==x:
            return  False
    return True
#=======================================================================================================================
#=======================================================================================================================
#----------------------------------------------------->  in Dictionary<-------------------------------------------------
def in_Dictionary(w):
    for dd in d:
        if w == dd:
            return True
    return False
#=======================================================================================================================
#=======================================================================================================================
#------------------------------------------> valid words in Dictionary<-------------------------------------------------
def valid_words():
    del list2[:]
    for w in List:
        for dd in d:
            if w == dd:
                if unique(w):
                     list2.append(w)
    return list2
#=======================================================================================================================
#=======================================================================================================================
#---------------------------------------------------> Read big text   <-------------------------------------------------
def Read_big_text():
    file=open("D:\\big text.txt","r")
    return file.read().split()
t=Read_big_text()
#=======================================================================================================================
#=======================================================================================================================
#---------------------------------------> previous word count from big text  <------------------------------------------
def previous_word_count(word):
    count=0
    for x in t:
        if x == word:
            count = count+1
    return count
#=======================================================================================================================
#=======================================================================================================================
#---------------------------------> conditional current word count from big text  <-------------------------------------
def conditional_word_count(w_N_1,w_N):
    count=0
    for x in range(0,len(t)):
        if t[x] == w_N:
            if t[x-1]==w_N_1:
                 count = count+1
    return count
#=======================================================================================================================
#=======================================================================================================================
#------------------------------------------------->      word probability     <-----------------------------------------
def word_probability(w_N_1,w_N):
    if (previous_word_count(w_N_1)==0): pass
    else:
        return float(conditional_word_count(w_N_1,w_N)/previous_word_count(w_N_1))
#=======================================================================================================================
#=======================================================================================================================
#--------------------------------------------->  probability of all words   <-------------------------------------------
def probability_of_all_words_given(w_N_1):
    list=[]
    for w_N in V_W:
        list.append(word_probability(w_N_1,w_N))
    return list
#=======================================================================================================================
#=======================================================================================================================
#---------------------------------------------------->  sort probability    <-------------------------------------------
def max_3_probability(w_N_1):
    index=[]
    pp=[]
    p=probability_of_all_words_given(w_N_1)
    for x in p:
        pp.append(x)

    for x in range(0,len(p)):
        big=x
        for xx in range(x+1,len(p)):
             if p[xx] > p[big]:
                big=xx
        temp=p[x]
        p[x]=p[big]
        p[big]=temp
        num=len(pp)
        if(len(pp)>3):
            num=3
        else:
            num=len(pp)

    for x in range(0,num):
        for xx in range(0,len(pp)):
            if pp[xx]==p[x]:
                index.append(xx)
    return index
#=======================================================================================================================
#=======================================================================================================================
#------------------------------------------------->       MAIN      <---------------------------------------------------
'''
#string=raw_input("enter text==> ")
first_edit('muh')                          #                        (ok)        Deal with one letter error
#second_edit()                            #      XXXXXXXXXXXXXXXXX (so big)    Deal with two letters error
print("================================================================================================================")
print("----------------->   all valid words")
V_W=valid_words()
#-----------------------------------------------------------------------------------------------------------------------
print("----------------->   Suggest words")
print("Please Wait...")
s=max_3_probability('very')
for x in range(0,3):
    print(V_W[s[x]])
'''
#=======================================================================================================================
#=======================================================================================================================
#------------------------------------------------->       GUI      <----------------------------------------------------
main_frame=Tkinter.Tk()
f1=Frame(main_frame,background='#565454')

#=======================================================================================================================
def ok():

    text=e1.get().split()
    for x in range(0,len(text)):
        if in_Dictionary(text[x]):
            txt.insert(END ,text[x]+" :-  This IS Correct \n")
            #tkMessageBox.showinfo(text[x],"Is Correct")
        else:
            #tkMessageBox.showinfo(text[x],"Not Correct ")
            txt.insert(END ,text[x]+" :- This IS Not Correct \n")
            first_edit(text[x])
            global V_W
            V_W = valid_words()

            #tkMessageBox.showinfo("---------->  ",V_W)
            txt.insert(END , "\n all valid words :- ")
            txt.insert(END ,V_W)
            txt.insert(END , " \n")
            print(V_W)
    #================
            s=max_3_probability(text[x-1])
            num2=len(s)
            if (num2>3):
                num2=3
            else:
                num2=len(s)

            for x in range(0,num2):
                #tkMessageBox.showinfo("---------->   Suggest words",V_W[s[x]])
                txt.insert(END , "\n Suggest words :-")
                txt.insert(END ,V_W[s[x]] )
                txt.insert(END , " \n")






#=======================================================================================================================

l00=Label(f1,text="",width="15",background='#565454')
l0=Label(f1,text="                Spell Checker                ",width="15",background='#565454', foreground='#14222c')
l000=Label(f1,text="",width="15",background='#565454')
ll=Label(text="",width="80",background='#565454')

l1=Label(f1,text="Enter Text",width="15",background='#565454', foreground='#14222c')
e1=Entry(f1,width="50", foreground='#14222c')
b1=Button(f1,text="Check",background="gray",width="20",command=ok, foreground='#14222c')
la=Label(main_frame,text="output",width="80",background='#565454', foreground='#14222c')
txt=Text(main_frame, height=15, width=70,background='#565454',foreground='#bbbbbb')
# txt.tag_configure('bold_italics', font=('Arial', 16, 'bold', 'italic'))
# txt.tag_configure('big', font=('Verdana', 20, 'bold'))
# txt.tag_configure('color', foreground='#476042', font=('Tempus Sans ITC', 16, 'bold'))


f1.pack()
l00.pack()
l0.pack()
l000.pack()
l1.pack(side="left")
e1.pack(side="left")
b1.pack(side="left")
ll.pack()

la.pack()
txt.pack()


def NewFile():
    tkMessageBox.showinfo(" New File"," This is Open New File")
# def OpenFile():
#     name = askopenfilename()
#     tkMessageBox.showinfo(" This is Path of The File" , name)
def About():
    tkMessageBox.showinfo("about us", " We are Student at the Faculty of Computing and Information Menoufia University \n Department of Computer Science")


menu = Menu(main_frame)
main_frame.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
# filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=main_frame.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)



main_frame.mainloop()

#=======================================================================================================================
#=======================================================================================================================



