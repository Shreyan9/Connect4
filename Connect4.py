from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Connect4")

clicked = True
count = 0

def disable_button():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
def disable_all_buttons():
    for b in col0 : b.config(state = DISABLED)
    for b in col1 : b.config(state = DISABLED)
    for b in col2 : b.config(state = DISABLED)
    for b in col3 : b.config(state = DISABLED)
    for b in col4 : b.config(state = DISABLED)
    for b in col5 : b.config(state = DISABLED)
    for b in col6 : b.config(state = DISABLED)
def checkwin():

    global winner
    winner = False

    #CHECKING HORIZONTAL


    if s1["bg"] == "red" and s2["bg"] == "red" and s3["bg"]=="red"and s4["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s2["bg"] == "red" and s3["bg"] == "red" and s4["bg"]=="red"and s5["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s3["bg"] == "red" and s4["bg"] == "red" and s5["bg"]=="red"and s6["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s4["bg"] == "red" and s5["bg"] == "red" and s6["bg"]=="red"and s7["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")

    if s8["bg"] == "red" and s9["bg"] == "red" and s10["bg"]=="red"and s11["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s9["bg"] == "red" and s10["bg"] == "red" and s11["bg"]=="red"and s12["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s10["bg"] == "red" and s11["bg"] == "red" and s12["bg"]=="red"and s13["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s11["bg"] == "red" and s12["bg"] == "red" and s13["bg"]=="red"and s14["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")

    if s15["bg"] == "red" and s16["bg"] == "red" and s17["bg"]=="red"and s18["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s16["bg"] == "red" and s17["bg"] == "red" and s18["bg"]=="red"and s19["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s17["bg"] == "red" and s18["bg"] == "red" and s19["bg"]=="red"and s20["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s18["bg"] == "red" and s19["bg"] == "red" and s20["bg"]=="red"and s21["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    
    if s22["bg"] == "red" and s23["bg"] == "red" and s24["bg"]=="red"and s25["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s23["bg"] == "red" and s24["bg"] == "red" and s25["bg"]=="red"and s26["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s24["bg"] == "red" and s25["bg"] == "red" and s26["bg"]=="red"and s27["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s25["bg"] == "red" and s26["bg"] == "red" and s27["bg"]=="red"and s28["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")

    if s29["bg"] == "red" and s30["bg"] == "red" and s31["bg"]=="red"and s32["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s30["bg"] == "red" and s31["bg"] == "red" and s32["bg"]=="red"and s33["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s31["bg"] == "red" and s32["bg"] == "red" and s33["bg"]=="red"and s34["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s32["bg"] == "red" and s33["bg"] == "red" and s34["bg"]=="red"and s35["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")

    if s36["bg"] == "red" and s37["bg"] == "red" and s38["bg"]=="red"and s39["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s37["bg"] == "red" and s38["bg"] == "red" and s39["bg"]=="red"and s40["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s38["bg"] == "red" and s39["bg"] == "red" and s40["bg"]=="red"and s41["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s39["bg"] == "red" and s40["bg"] == "red" and s41["bg"]=="red"and s42["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")

    if s1["bg"] == "yellow" and s2["bg"] == "yellow" and s3["bg"]=="yellow"and s4["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s2["bg"] == "yellow" and s3["bg"] == "yellow" and s4["bg"]=="yellow"and s5["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s3["bg"] == "yellow" and s4["bg"] == "yellow" and s5["bg"]=="yellow"and s6["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s4["bg"] == "yellow" and s5["bg"] == "yellow" and s6["bg"]=="yellow"and s7["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
 
    if s8["bg"] == "yellow" and s9["bg"] == "yellow" and s10["bg"]=="yellow"and s11["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s9["bg"] == "yellow" and s10["bg"] == "yellow" and s11["bg"]=="yellow"and s12["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s10["bg"] == "yellow" and s11["bg"] == "yellow" and s12["bg"]=="yellow"and s13["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s11["bg"] == "yellow" and s12["bg"] == "yellow" and s13["bg"]=="yellow"and s14["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
 
    if s15["bg"] == "yellow" and s16["bg"] == "yellow" and s17["bg"]=="yellow"and s18["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s16["bg"] == "yellow" and s17["bg"] == "yellow" and s18["bg"]=="yellow"and s19["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s17["bg"] == "yellow" and s18["bg"] == "yellow" and s19["bg"]=="yellow"and s20["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s18["bg"] == "yellow" and s19["bg"] == "yellow" and s20["bg"]=="yellow"and s21["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    
    if s22["bg"] == "yellow" and s23["bg"] == "yellow" and s24["bg"]=="yellow"and s25["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s23["bg"] == "yellow" and s24["bg"] == "yellow" and s25["bg"]=="yellow"and s26["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s24["bg"] == "yellow" and s25["bg"] == "yellow" and s26["bg"]=="yellow"and s27["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s25["bg"] == "yellow" and s26["bg"] == "yellow" and s27["bg"]=="yellow"and s28["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
 
    if s29["bg"] == "yellow" and s30["bg"] == "yellow" and s31["bg"]=="yellow"and s32["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s30["bg"] == "yellow" and s31["bg"] == "yellow" and s32["bg"]=="yellow"and s33["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s31["bg"] == "yellow" and s32["bg"] == "yellow" and s33["bg"]=="yellow"and s34["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s32["bg"] == "yellow" and s33["bg"] == "yellow" and s34["bg"]=="yellow"and s35["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
 
    if s36["bg"] == "yellow" and s37["bg"] == "yellow" and s38["bg"]=="yellow"and s39["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s37["bg"] == "yellow" and s38["bg"] == "yellow" and s39["bg"]=="yellow"and s40["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s38["bg"] == "yellow" and s39["bg"] == "yellow" and s40["bg"]=="yellow"and s41["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s39["bg"] == "yellow" and s40["bg"] == "yellow" and s41["bg"]=="yellow"and s42["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")



    #CHECKING VERTICAL

    if s1["bg"] == "red" and s8["bg"] == "red" and s15["bg"]=="red"and s22["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s8["bg"] == "red" and s15["bg"] == "red" and s22["bg"]=="red"and s29["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s15["bg"] == "red" and s22["bg"] == "red" and s29["bg"]=="red"and s36["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    
    if s2["bg"] == "red" and s9["bg"] == "red" and s16["bg"]=="red"and s23["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s9["bg"] == "red" and s16["bg"] == "red" and s23["bg"]=="red"and s30["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s16["bg"] == "red" and s23["bg"] == "red" and s30["bg"]=="red"and s37["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")

    if s3["bg"] == "red" and s10["bg"] == "red" and s17["bg"]=="red"and s24["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s10["bg"] == "red" and s17["bg"] == "red" and s24["bg"]=="red"and s31["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s17["bg"] == "red" and s24["bg"] == "red" and s31["bg"]=="red"and s38["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")

    if s4["bg"] == "red" and s11["bg"] == "red" and s18["bg"]=="red"and s25["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s11["bg"] == "red" and s18["bg"] == "red" and s25["bg"]=="red"and s32["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s18["bg"] == "red" and s25["bg"] == "red" and s32["bg"]=="red"and s39["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    
    if s5["bg"] == "red" and s12["bg"] == "red" and s19["bg"]=="red"and s26["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s12["bg"] == "red" and s19["bg"] == "red" and s26["bg"]=="red"and s33["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s19["bg"] == "red" and s26["bg"] == "red" and s33["bg"]=="red"and s40["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    
    if s6["bg"] == "red" and s13["bg"] == "red" and s20["bg"]=="red"and s27["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s13["bg"] == "red" and s20["bg"] == "red" and s27["bg"]=="red"and s34["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s20["bg"] == "red" and s27["bg"] == "red" and s34["bg"]=="red"and s41["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    
    if s7["bg"] == "red" and s14["bg"] == "red" and s21["bg"]=="red"and s28["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s14["bg"] == "red" and s21["bg"] == "red" and s28["bg"]=="red"and s35["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s21["bg"] == "red" and s28["bg"] == "red" and s35["bg"]=="red"and s42["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")

    if s1["bg"] == "yellow" and s8["bg"] == "yellow" and s15["bg"]=="yellow"and s22["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s8["bg"] == "yellow" and s15["bg"] == "yellow" and s22["bg"]=="yellow"and s29["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s15["bg"] == "yellow" and s22["bg"] == "yellow" and s29["bg"]=="yellow"and s36["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    
    if s2["bg"] == "yellow" and s9["bg"] == "yellow" and s16["bg"]=="yellow"and s23["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s9["bg"] == "yellow" and s16["bg"] == "yellow" and s23["bg"]=="yellow"and s30["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s16["bg"] == "yellow" and s23["bg"] == "yellow" and s30["bg"]=="yellow"and s37["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
 
    if s3["bg"] == "yellow" and s10["bg"] == "yellow" and s17["bg"]=="yellow"and s24["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s10["bg"] == "yellow" and s17["bg"] == "yellow" and s24["bg"]=="yellow"and s31["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s17["bg"] == "yellow" and s24["bg"] == "yellow" and s31["bg"]=="yellow"and s38["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
 
    if s4["bg"] == "yellow" and s11["bg"] == "yellow" and s18["bg"]=="yellow"and s25["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s11["bg"] == "yellow" and s18["bg"] == "yellow" and s25["bg"]=="yellow"and s32["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s18["bg"] == "yellow" and s25["bg"] == "yellow" and s32["bg"]=="yellow"and s39["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    
    if s5["bg"] == "yellow" and s12["bg"] == "yellow" and s19["bg"]=="yellow"and s26["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s12["bg"] == "yellow" and s19["bg"] == "yellow" and s26["bg"]=="yellow"and s33["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s19["bg"] == "yellow" and s26["bg"] == "yellow" and s33["bg"]=="yellow"and s40["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    
    if s6["bg"] == "yellow" and s13["bg"] == "yellow" and s20["bg"]=="yellow"and s27["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s13["bg"] == "yellow" and s20["bg"] == "yellow" and s27["bg"]=="yellow"and s34["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s20["bg"] == "yellow" and s27["bg"] == "yellow" and s34["bg"]=="yellow"and s41["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    
    if s7["bg"] == "yellow" and s14["bg"] == "yellow" and s21["bg"]=="yellow"and s28["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s14["bg"] == "yellow" and s21["bg"] == "yellow" and s28["bg"]=="yellow"and s35["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s21["bg"] == "yellow" and s28["bg"] == "yellow" and s35["bg"]=="yellow"and s42["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")



    #Checking Diagonal

    if s1["bg"] == "red" and s9["bg"] == "red" and s17["bg"]=="red"and s25["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s2["bg"] == "red" and s10["bg"] == "red" and s18["bg"]=="red"and s26["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s3["bg"] == "red" and s11["bg"] == "red" and s19["bg"]=="red"and s27["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s4["bg"] == "red" and s12["bg"] == "red" and s20["bg"]=="red"and s28["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s4["bg"] == "red" and s10["bg"] == "red" and s16["bg"]=="red"and s22["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")

    if s5["bg"] == "red" and s11["bg"] == "red" and s17["bg"]=="red"and s23["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s6["bg"] == "red" and s12["bg"] == "red" and s18["bg"]=="red"and s24["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s7["bg"] == "red" and s13["bg"] == "red" and s19["bg"]=="red"and s25["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s8["bg"] == "red" and s16["bg"] == "red" and s24["bg"]=="red"and s32["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s9["bg"] == "red" and s17["bg"] == "red" and s25["bg"]=="red"and s33["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s10["bg"] == "red" and s18["bg"] == "red" and s26["bg"]=="red"and s34["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s11["bg"] == "red" and s19["bg"] == "red" and s27["bg"]=="red"and s35["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s11["bg"] == "red" and s17["bg"] == "red" and s23["bg"]=="red"and s29["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s12["bg"] == "red" and s18["bg"] == "red" and s24["bg"]=="red"and s30["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s13["bg"] == "red" and s19["bg"] == "red" and s25["bg"]=="red"and s31["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s14["bg"] == "red" and s20["bg"] == "red" and s26["bg"]=="red"and s32["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s15["bg"] == "red" and s23["bg"] == "red" and s31["bg"]=="red"and s39["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s16["bg"] == "red" and s24["bg"] == "red" and s32["bg"]=="red"and s40["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s17["bg"] == "red" and s25["bg"] == "red" and s33["bg"]=="red"and s41["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s18["bg"] == "red" and s26["bg"] == "red" and s34["bg"]=="red"and s42["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s19["bg"] == "red" and s25["bg"] == "red" and s31["bg"]=="red"and s37["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s20["bg"] == "red" and s26["bg"] == "red" and s32["bg"]=="red"and s38["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    if s21["bg"] == "red" and s27["bg"] == "red" and s33["bg"]=="red"and s39["bg"]=="red":
        winner = True
        messagebox.showinfo('Connect4', "Red WINS")
    
    if s1["bg"] == "yellow" and s9["bg"] == "yellow" and s17["bg"]=="yellow"and s25["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s2["bg"] == "yellow" and s10["bg"] == "yellow" and s18["bg"]=="yellow"and s26["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s3["bg"] == "yellow" and s11["bg"] == "yellow" and s19["bg"]=="yellow"and s27["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s4["bg"] == "yellow" and s12["bg"] == "yellow" and s20["bg"]=="yellow"and s28["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s4["bg"] == "yellow" and s10["bg"] == "yellow" and s16["bg"]=="yellow"and s22["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
 
    if s5["bg"] == "yellow" and s11["bg"] == "yellow" and s17["bg"]=="yellow"and s23["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s6["bg"] == "yellow" and s12["bg"] == "yellow" and s18["bg"]=="yellow"and s24["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s7["bg"] == "yellow" and s13["bg"] == "yellow" and s19["bg"]=="yellow"and s25["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s8["bg"] == "yellow" and s16["bg"] == "yellow" and s24["bg"]=="yellow"and s32["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s9["bg"] == "yellow" and s17["bg"] == "yellow" and s25["bg"]=="yellow"and s33["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s10["bg"] == "yellow" and s18["bg"] == "yellow" and s26["bg"]=="yellow"and s34["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s11["bg"] == "yellow" and s19["bg"] == "yellow" and s27["bg"]=="yellow"and s35["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s11["bg"] == "yellow" and s17["bg"] == "yellow" and s23["bg"]=="yellow"and s29["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s12["bg"] == "yellow" and s18["bg"] == "yellow" and s24["bg"]=="yellow"and s30["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s13["bg"] == "yellow" and s19["bg"] == "yellow" and s25["bg"]=="yellow"and s31["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s14["bg"] == "yellow" and s20["bg"] == "yellow" and s26["bg"]=="yellow"and s32["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s15["bg"] == "yellow" and s23["bg"] == "yellow" and s31["bg"]=="yellow"and s39["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s16["bg"] == "yellow" and s24["bg"] == "yellow" and s32["bg"]=="yellow"and s40["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s17["bg"] == "yellow" and s25["bg"] == "yellow" and s33["bg"]=="yellow"and s41["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s18["bg"] == "yellow" and s26["bg"] == "yellow" and s34["bg"]=="yellow"and s42["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s19["bg"] == "yellow" and s25["bg"] == "yellow" and s31["bg"]=="yellow"and s37["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s20["bg"] == "yellow" and s26["bg"] == "yellow" and s32["bg"]=="yellow"and s38["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")
    if s21["bg"] == "yellow" and s27["bg"] == "yellow" and s33["bg"]=="yellow"and s39["bg"]=="yellow":
        winner = True
        messagebox.showinfo('Connect4', "Yellow WINS")

    if winner:
        disable_button()

    if count >= 42 :
         messagebox.showinfo("Connect4","It is a tie!")
def b_click(b, currentCol):
    global clicked, count
    c=5
    endTurn = False
    if clicked == True:
        while c >=0 and endTurn == False:
            if currentCol[c]["bg"] == "lavender":
                currentCol[c]["bg"] = "red"
                endTurn = True
                count+=1
                clicked = False
            else:
                c = c-1    
        
        
    elif clicked == False:
        while c >=0 and endTurn == False:
            if currentCol[c]["bg"] == "lavender":
                currentCol[c]["bg"] = "yellow"
                endTurn = True
                count+=1
                clicked = True
            else:
                c = c-1
        
    checkwin()
def reset():
    global b1, b2, b3, b4, b5, b6, b7, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40, s41, s42, col0, col1, col2, col3, col4, col5, col6, count, clicked

    count = 0
    clicked = True

    b1 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda : b_click(b1, col0)); b1.grid(row = 0, column = 0)
    b2 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda : b_click(b2, col1)); b2.grid(row = 0, column = 1)
    b3 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda : b_click(b3, col2)); b3.grid(row = 0, column = 2)
    b4 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda : b_click(b4, col3)); b4.grid(row = 0, column = 3)
    b5 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda : b_click(b5, col4)); b5.grid(row = 0, column = 4)
    b6 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda : b_click(b6, col5)); b6.grid(row = 0, column = 5)
    b7 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda : b_click(b7, col6)); b7.grid(row = 0, column = 6)

    s1 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s1.grid(row = 1, column = 0)
    s2 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s2.grid(row = 1, column = 1)
    s3 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s3.grid(row = 1, column = 2)
    s4 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s4.grid(row = 1, column = 3)
    s5 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s5.grid(row = 1, column = 4)
    s6 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s6.grid(row = 1, column = 5)
    s7 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s7.grid(row = 1, column = 6)

    s8 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s8.grid(row = 2, column = 0)
    s9 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s9.grid(row = 2, column = 1)
    s10 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s10.grid(row = 2, column = 2)
    s11= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s11.grid(row = 2, column = 3)
    s12= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s12.grid(row = 2, column = 4)
    s13= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s13.grid(row = 2, column = 5)
    s14= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s14.grid(row = 2, column = 6)

    s15= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s15.grid(row = 3, column = 0)
    s16= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s16.grid(row = 3, column = 1)
    s17= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s17.grid(row = 3, column = 2)
    s18= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s18.grid(row = 3, column = 3)
    s19= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s19.grid(row = 3, column = 4)
    s20= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s20.grid(row = 3, column = 5)

    s21 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s21.grid(row = 3, column = 6)
    s22= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s22.grid(row = 4, column = 0)
    s23= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s23.grid(row = 4, column = 1)
    s24= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s24.grid(row = 4, column = 2)
    s25= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s25.grid(row = 4, column = 3)
    s26= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s26.grid(row = 4, column = 4)
    s27= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s27.grid(row = 4, column = 5)
    s28= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s28.grid(row = 4, column = 6)

    s29 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s29.grid(row = 5, column = 0)
    s30= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s30.grid(row = 5, column = 1)
    s31= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s31.grid(row = 5, column = 2)
    s32= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s32.grid(row = 5, column = 3)
    s33= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s33.grid(row = 5, column = 4)
    s34= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s34.grid(row = 5, column = 5)
    s35= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s35.grid(row = 5, column = 6)

    s36 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s36.grid(row = 6, column = 0)
    s37 = Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s37.grid(row = 6, column = 1)
    s38= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s38.grid(row = 6, column = 2)
    s39= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s39.grid(row = 6, column = 3)
    s40= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s40.grid(row = 6, column = 4)
    s41= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender"); s41.grid(row = 6, column = 5)
    s42= Button(root, text="", font = ("Helvetica", 20), height = 3, width = 6, bg = "lavender") ; s42.grid(row = 6, column = 6)

    col0 = [s1,s8,s15,s22,s29,s36]; col1 = [s2,s9,s16,s23,s30,s37]; col2 = [s3,s10,s17,s24,s31,s38]; col3 = [s4,s11,s18,s25,s32,s39]; col4 = [s5,s12,s19,s26,s33,s40]; col5 = [s6,s13,s20,s27,s34,s41]; col6 = [s7,s14,s21,s28,s35,s42]  

    disable_all_buttons()

my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

root.mainloop()