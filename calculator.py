# import
from tkinter import *
from tkinter import ttk
import tkinter as tk
import math
# import>
# valori
a = ""
x1 = ""
x2 = ""
delta = ""
pxd = ""
delturi = ""
# px1 = tk.StringVar()
# px2 = tk.StringVar()
pi = 180

# valoare font
fecr = ("Courier", 20, "bold")
fecr1 = ("Courier", 10, "bold")
log_font = ("Courier", 50, "bold")
# valoare font>
# valori>
# functii


def ad1():
    global a
    a = a + "1"
# ❗change the ect Entry text to a
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def ad2():
    global a
    a = a + "2"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def ad3():
    global a
    a = a + "3"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def ad4():
    global a
    a = a + "4"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def ad5():
    global a
    a = a + "5"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def ad6():
    global a
    a = a + "6"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def ad7():
    global a
    a = a + "7"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def ad8():
    global a
    a = a + "8"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def ad9():
    global a
    a = a + "9"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def ad0():
    global a
    a = a + "0"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def adp():
    global a
    a = a + "+"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def adm():
    global a
    a = a + "-"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def adinm():
    global a
    a = a + "*"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def adimp():
    global a
    a = a + "/"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def adrad():
    global a
    a = str(math.sqrt(int(a)))
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def egal():
    global a
    if a == "":
        a = str(float(eval(ecr.get())))
        ecr.delete(0, tk.END)
        ecr.insert(0, a)
    a = str(eval(a))
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def CLR():
    global a
    a = ""
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def pardes():
    global a
    a = a + "("
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def parimch():
    global a
    a = a + ")"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def modulet():
    global a
    a = a + "%"
    ecr.delete(0, tk.END)
    ecr.insert(0, a)


def ecg2():
    # ❗global is usen when you nead to change an value outside the function
    global afv
    global bfv
    global cfv
    afv = int(af.get())
    bfv = int(bf.get())
    cfv = int(cf.get())
    delta = (bfv * bfv)-(4 * cfv * afv)
    if delta == 0:
        x1 = (-1*(bfv))/(2*afv)
        x2 = x1
    elif delta > 0:
        x1 = ((float(-1 * bfv)) + (float(math.sqrt(delta))))/(float(2*afv))
        x2 = ((float(-1 * bfv)) - (float(math.sqrt(delta))))/(float(2*afv))
    else:
        x1 = "∅"
        x2 = "∅"
    pxd = ("x1=" + str(x1) + "|x2="+str(x2))
    delturi = (str("∆=" + str(delta)))
    delt['text'] = delturi
    xuxd['text'] = pxd
# fin 🧑‍🏫


# ❗here I transformed 42 lines of code in 8 because instead of writing all settings one by one I made a loop to make it for me the loop is at line 224
btn_set = [[1, ad1, "blue"], [2, ad2, "blue"], [3, ad2, "blue"], ["+", adp, "yellow"],
           [4, ad4, "blue"], [5, ad5, "blue"], [
               6, ad6, "blue"], ["-", adm, "yellow"],
           [7, ad7, "blue"], [8, ad8, "blue"], [
               9, ad9, "blue"], ["*", adinm, "yellow"],
           ["%", modulet, "yellow"], [0, ad0, "blue"], [
               "/", adimp, "yellow"], ["√", adrad, "yellow"],
           ["(", pardes, "orange"], [")", parimch, "orange"], ["CLR", CLR, "red"], ["=", egal, "red"]]
v = len(btn_set)

# functii>
# set interfata baza
# ❗normal tkiner window setings
root = tk.Tk()
root.title("Calculator")
root.geometry("1100x300")
# set interfata baza>
# set ecran calc
ecr = tk.Entry(root, background="green", foreground="white",
               borderwidth=1, relief="solid", font=fecr, justify="right")
ecr.insert(0, a)
ecr.config(state="normal")
ecr.pack(fill="both", expand=True, side="top")
ecr.place(height=50, width=300)
# set ecran calc>
# butoane
cordx = 0
cordy = 50
for n in range(v):
    element = tk.Button(root, text=btn_set[n][0], background=btn_set[n][2], borderwidth=1,
                        relief="solid", font=fecr, justify="right", command=btn_set[n][1])
    if cordx > 225:
        cordy += 50
        cordx = 0
    element.place(x=cordx, y=cordy, height=50, width=75)
    cordx += 75
btn_set.clear()
# butoane>
# functii grad 2
af = tk.Entry(root, background="white", borderwidth=1,
              relief="solid", font=fecr, justify="right")
af.place(x=375, y=0, height=50, width=75)
bf = tk.Entry(root, background="white", borderwidth=1,
              relief="solid", font=fecr, justify="right")
bf.place(x=375, y=50, height=50, width=75)
cf = tk.Entry(root, background="white", borderwidth=1,
              relief="solid", font=fecr, justify="right")
cf.place(x=375, y=100, height=50, width=75)
av = tk.Label(root, text="a=", background="white", borderwidth=1,
              relief="solid", font=fecr, justify="right")
av.place(x=300, y=0, height=50, width=75)
bv = tk.Label(root, text="b=", background="white", borderwidth=1,
              relief="solid", font=fecr, justify="right")
bv.place(x=300, y=50, height=50, width=75)
cv = tk.Label(root, text="c=", background="white", borderwidth=1,
              relief="solid", font=fecr, justify="right")
cv.place(x=300, y=100, height=50, width=75)
but_anal = Button(root, text="=>", background="blue", borderwidth=1,
                  relief="solid", font=fecr, justify="right", command=ecg2)
but_anal.place(x=300, y=150, width=150, height=50)
delt = tk.Label(root, text="", background="white", borderwidth=1,
                relief="solid", font=fecr, justify="right")
delt.place(x=300, y=200, width=150, height=50)
xuxd = tk.Label(root, text="", background="white", borderwidth=1,
                relief="solid", font=fecr1, justify="right")
xuxd.place(x=300, y=250, width=150, height=50)
# functii grad 2>
# log
m = ""


def calc():
    global m
    m = math.log(int(inp_caplog.get()), int(inp_bazalog.get()))
    m = int(m)
    log_rez.delete(0, tk.END)
    log_rez.insert(0, m)


border = tk.Label(root, background="grey", relief="solid")
border.place(x=450, y=0, height=75, width=400)
log_inf = tk.Label(root, text="log", font=log_font,
                   justify="right", background="grey")
log_inf.place(x=450, y=0)
inp_bazalog = tk.Entry(root, background="white",
                       relief="solid", font=fecr, justify="right")
inp_bazalog.place(x=580, y=40, height=30, width=50)
inp_caplog = tk.Entry(root, background="white", borderwidth=1,
                      relief="solid", font=fecr, justify="right")
inp_caplog.place(x=600, y=10, height=30, width=50)
result = tk.Button(root, text="=", font=log_font,
                   justify="right", command=calc, background="grey")
result.place(x=650, y=15, height=50, width=50)
log_rez = tk.Entry(root, text=m, background="grey", relief="flat", font=fecr)
log_rez.place(x=700, y=0, height=60, width=100)
# fin log
# progresii


def calc_prog_ar():
    a1, a2, n = int(inip_prog_aritm_a1.get()), int(
        inip_prog_aritm_a2.get()), int(inip_prog_aritm_an.get())
    ratiaa = a2-a1
    an = a1 + (n-1)*ratiaa
    rezultat = ((a1 + an)*n)/2
    raspuns_prog_aritm.delete(0, tk.END)
    raspuns_prog_aritm.insert(0, rezultat)


border_prog = tk.Frame(root, relief="solid", borderwidth=1, bg="lightblue")
border_prog.place(x=450, y=75, width=400, height=225)
inip_prog_aritm_a1 = tk.Entry(
    root, background="white", relief="solid", font=fecr, justify="right")
inip_prog_aritm_a1.place(x=470, y=90, width=50, height=50)
simbol_1 = tk.Label(root, background="lightblue", text="+",
                    relief="flat", font=fecr, justify="right")
simbol_1.place(x=520, y=90, width=50, height=50)
inip_prog_aritm_a2 = tk.Entry(
    root, background="white", relief="solid", font=fecr, justify="right")
inip_prog_aritm_a2.place(x=570, y=90, width=50, height=50)
simbol_2 = tk.Label(root, background="lightblue", text="+.+",
                    relief="flat", font=fecr, justify="right")
simbol_2.place(x=620, y=90, width=50, height=50)
inip_prog_aritm_an = tk.Entry(
    root, background="white", relief="solid", font=fecr, justify="right")
inip_prog_aritm_an.place(x=670, y=90, width=50, height=50)
simbol_3 = tk.Button(root, background="lightblue", text="=",
                     font=fecr, justify="right", command=calc_prog_ar)
simbol_3.place(x=720, y=90, width=50, height=50)
raspuns_prog_aritm = tk.Entry(
    root, background="lightblue", text=a, font=fecr, justify="right")
raspuns_prog_aritm.place(x=770, y=90, width=75, height=50)
# geometrice


def calc_prog_ge():
    b1, b2, n = int(entry_a4.get()), int(entry_a5.get()), int(entry_an.get())
    q = int(b2/b1)
    initial_value = (b1 * ((q**n) - 1)) / (q - 1)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, initial_value)


entry_a4 = tk.Entry(root, background="white",
                    relief="solid", font=fecr, justify="right")
entry_a4.place(x=470, y=150, width=50, height=50)
symbol_multiply_1 = tk.Label(
    root, background="lightblue", text="*", relief="flat", font=fecr, justify="right")
symbol_multiply_1.place(x=520, y=150, width=50, height=50)
entry_a5 = tk.Entry(root, background="white",
                    relief="solid", font=fecr, justify="right")
entry_a5.place(x=570, y=150, width=50, height=50)
symbol_multiply_2 = tk.Label(root, background="lightblue",
                             text="*.*", relief="flat", font=fecr, justify="right")
symbol_multiply_2.place(x=620, y=150, width=50, height=50)
entry_an = tk.Entry(root, background="white",
                    relief="solid", font=fecr, justify="right")
entry_an.place(x=670, y=150, width=50, height=50)
symbol_equal = tk.Button(root, background="lightblue",
                         text="=", font=fecr, justify="right", command=calc_prog_ge)
symbol_equal.place(x=720, y=150, width=50, height=50)
entry_result = tk.Entry(root, background="lightblue",
                        font=fecr, justify="right")
entry_result.place(x=770, y=150, width=75, height=50)
# fin progresii
# medii
med_ar_val = []
rez = 0


def ad_med_ar():
    global med_ar_val, rez
    cra = inp_med_ar.get()
    if cra == "stop":
        cine = len(med_ar_val)
        for x in range(cine):
            rez = rez + med_ar_val[x]
        rez = rez/len(med_ar_val)
        rez_med_ar.delete(0, tk.END)
        rez_med_ar.insert(0, rez)
        med_ar_val.clear()
    else:
        cra = float(cra)
    if isinstance(cra, float):
        med_ar_val.append(cra)
        print(med_ar_val)


inp_med_ar = tk.Entry(root, background="white",
                      relief="solid", font=fecr, justify="right")
inp_med_ar.place(x=470, y=210, width=50, height=50)
but_med_ar = tk.Button(root, background="lightblue", relief="solid",
                       font=fecr, text="+=", justify="right", command=ad_med_ar)
but_med_ar.place(x=520, y=210, width=50, height=50)
rez_med_ar = tk.Entry(root, background="white",
                      relief="solid", font=fecr, justify="right")
rez_med_ar.place(x=570, y=210, width=70, height=50)
# fin med aritmetica
# media geometrica
med_ar_val = []
rez = 0


def ad_med_ar():
    global med_ar_val, rez
    cra = inp_med_ar.get()
    if cra == "stop":
        cine = len(med_ar_val)
        for x in range(cine):
            rez = rez + med_ar_val[x]
        rez = rez/len(med_ar_val)
        rez_med_ar.delete(0, tk.END)
        rez_med_ar.insert(0, rez)
        med_ar_val.clear()
    else:
        cra = float(cra)
    if isinstance(cra, float):
        med_ar_val.append(cra)
        print(med_ar_val)


med_ge_val = []
rez = 1


def ad_med_ge():
    global med_ge_val, rez
    cra = inp_med_ge.get()
    if cra == "stop":
        cine = len(med_ge_val)
        for x in range(cine):
            rez = rez * med_ge_val[x]
        rez = float(rez ** (1/cine))
        rez_med_ge.delete(0, tk.END)
        rez_med_ge.insert(0, rez)
        med_ge_val.clear()
    else:
        cra = float(cra)
    if isinstance(cra, float):
        med_ge_val.append(cra)
        print(med_ge_val)


inp_med_ge = tk.Entry(root, background="white",
                      relief="solid", font=fecr, justify="right")
inp_med_ge.place(x=670, y=210, width=50, height=50)
but_med_ge = tk.Button(root, background="lightblue", relief="solid",
                       font=fecr, text="*=", justify="right", command=ad_med_ge)
but_med_ge.place(x=720, y=210, width=50, height=50)
rez_med_ge = tk.Entry(root, background="white",
                      relief="solid", font=fecr, justify="right")
rez_med_ge.place(x=770, y=210, width=70, height=50)
# finmedii
# fin medii
# bin


def calc_bin():
    bin_response = bin(int(inp_nr_bin.get()))
    bin_response = bin_response[2:]
    ext_nr_bin.delete(0, tk.END)
    ext_nr_bin.insert(0, bin_response)


inp_nr_bin = tk.Entry(root, background="white",
                      relief="solid", font=fecr, justify="right")
inp_nr_bin.place(x=450, y=270, width=100, height=25)
binary = tk.Button(root, background="lightblue", text="->",
                   relief="solid", font=fecr, justify="right", command=calc_bin)
binary.place(x=550, y=270, height=25, width=25)
ext_nr_bin = tk.Entry(root, background="white",
                      relief="solid", font=fecr, justify="right")
ext_nr_bin.place(x=575, y=270, width=100, height=25)
semn_bin = tk.Label(root, background="lightblue",
                    relief="flat", font=fecr, justify="right", text="bin")
semn_bin.place(x=676, y=270, width=50, height=23)
# fin bin


def calc_tringo():
    calcul, mod = trigo_entry.get(), sin_cos_tg_cotg.get()
    calcul = calcul.replace("pi", "180")
    calcul = int(eval(calcul))
    if mod == "sin":
        rezultat_trigo = math.sin(calcul)
    elif mod == "cos":
        rezultat_trigo = math.cos(calcul)
    elif mod == "tg":
        rezultat_trigo = (math.sin(calcul))/(math.cos(calcul))
    elif mod == "ctg":
        rezultat_trigo = (math.cos(calcul))/(math.sin(calcul))
    trigo_rez.delete(0, tk.END)
    trigo_rez.insert(0, rezultat_trigo)


border_trigo = tk.Label(root, background="red", relief="solid")
border_trigo.place(x=850, y=0, width=250, height=100)
sin_cos_tg_cotg = tk.Entry(root, relief="solid", background="red", font=fecr)
sin_cos_tg_cotg.place(x=850, y=0, width=50, height=30)
trigo_entry = tk.Entry(root, relief="solid", background="red", font=fecr)
trigo_entry.place(x=900, y=0, width=150, height=30)
trigo_btn = tk.Button(root, relief="solid", background="red",
                      font=fecr, text="=>", command=calc_tringo)
trigo_btn.place(x=1050, y=0, width=50, height=30)
trigo_rez = tk.Entry(root, font=fecr, background="white", relief="solid")
trigo_rez.place(x=850, y=30, width=250, height=30)
semn_trigo = tk.Label(text="trigo", font=fecr, relief="flat", background="red")
semn_trigo.place(x=855, y=72, width=100, height=25)
# trigonometrie
# rezistori


def start_resistor_calc():
    b1, b2, b3, b4, b5 = band_1.get(), band_2.get(
    ), band_3.get(), band_4.get(), band_5.get()
    match b1:
        case "black":
            b1 = 0
        case "brown":
            b1 = 1
        case "red":
            b1 = 2
        case "orange":
            b1 = 3
        case "yellow":
            b1 = 4
        case "green":
            b1 = 5
        case "blue":
            b1 = 6
        case "violet":
            b1 = 7
        case "grey":
            b1 = 8
        case "white":
            b1 = 9
    match b2:
        case "black":
            b2 = 0
        case "brown":
            b2 = 1
        case "red":
            b2 = 2
        case "orange":
            b2 = 3
        case "yellow":
            b2 = 4
        case "green":
            b2 = 5
        case "blue":
            b2 = 6
        case "violet":
            b2 = 7
        case "grey":
            b2 = 8
        case "white":
            b2 = 9
    match b3:
        case "black":
            b3 = 0
        case "brown":
            b3 = 1
        case "red":
            b3 = 2
        case "orange":
            b3 = 3
        case "yellow":
            b3 = 4
        case "green":
            b3 = 5
        case "blue":
            b3 = 6
        case "violet":
            b3 = 7
        case "grey":
            b3 = 8
        case "white":
            b3 = 9
    match b4:
        case "black":
            b4 = ""
        case "brown":
            b4 = "*10"
        case "red":
            b4 = "*100"
        case "orange":
            b4 = "*1000"
        case "yellow":
            b4 = "*10000"
        case "green":
            b4 = "*100000"
        case "blue":
            b4 = "*1000000"
        case "violet":
            b4 = "*10000000"
        case "grey":
            b4 = "*100000000"
        case "white":
            b4 = "*1000000000"
        case "gold":
            b4 = "/10"
        case "silver":
            b4 = "/100"
    match b5:
        case "black":
            b5 = ""
        case "brown":
            b5 = "±1%"
        case "red":
            b5 = "±2%"
        case "green":
            b5 = "±0.5%"
        case "blue":
            b5 = "±0.25%"
        case "violet":
            b5 = "±0.1%"
        case "grey":
            b5 = "±0.05%"
        case "gold":
            b5 = "±5%"
        case "silver":
            b5 = "±10%"
    calcul = str(eval(str(b1)+str(b2)+str(b3)+b4))+b5
    band_resp.delete(0, tk.END)
    band_resp.insert(0, calcul)


band_1 = tk.Entry(root, background="white", relief="solid")
band_1.place(x=850, y=100, width=50, height=30)
band_2 = tk.Entry(root, background="white", relief="solid")
band_2.place(x=900, y=100, width=50, height=30)
band_3 = tk.Entry(root, background="white", relief="solid")
band_3.place(x=950, y=100, width=50, height=30)
band_4 = tk.Entry(root, background="white", relief="solid")
band_4.place(x=1000, y=100, width=50, height=30)
band_5 = tk.Entry(root, background="white", relief="solid")
band_5.place(x=1050, y=100, width=50, height=30)
band_resp = tk.Entry(root, background="white", relief="solid")
band_resp.place(x=850, y=130, width=200, height=30)
band_button = tk.Button(root, text="=>", background="blue",
                        command=start_resistor_calc, relief="solid")
band_button.place(x=1050, y=130, width=50, height=30)
# fin_rezistori
# fin_trigonometrie


root.mainloop()
