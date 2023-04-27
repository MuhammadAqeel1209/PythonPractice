from tkinter import *

my_Root = Tk() 

my_Root.geometry("444x234") 
my_Root.title("My GUI") #-->👉Change the title of GUI

#Important attribute of label
"""
text -> add the text
bd   -> backgroud
fg   -> foreground
font -> set the font
    1)font=("comicsansns",12,"bold")
    2)font= "comicsansns ,12, bold"
xpad -> padding in x
ypad -> padding in y
releif -> border style -> SUNKEN,RAISED,RIDGE,GROOVE
"""
title_label = Label(text=""" A group of Germans at Allas Sea Pool, Helsinki, Finland. Traveling abroad together is a strong indicator of friendship.\n
Part of a series on Love \n Red-outline heart icon\n Types of love \n1)AffectionBonding \n2)HeartCompassionate  \n3)loveConjugal 
\nFriendship is a relationship of mutual affection between people.
\nIt is a stronger form of interpersonal bond than an "acquaintance" or an "association", such as a classmate, neighbor, coworker, or colleague.
\nIn some cultures, the concept of friendship is restricted to a small number of very deep relationships; \nin others, such as the U.S. and Canada, a person could have many friends,\n and perhaps a more intense relationship with one or two people, who may be called good friends or best friends. """,
bg="black",fg="Green",padx=23,pady=44,font="Ariel,12,bold",borderwidth=3,relief=SUNKEN)

#Important attribute of pack
"""
anchor = nw -->use for direction(n, ne, e, se, s, sw, w, nw,centre(by Default))
side = (top(by Default),bottom,right,left)
fill = X Y
xpad = padding in x
ypad = padding in y
"""

title_label.pack(side= LEFT,fill=Y,padx=23,pady=33)
my_Root.mainloop()