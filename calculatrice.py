try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk


#Précédent calcul fait
def resultatRead(fichier):
    with open(fichier, "r") as fileRead:
        lines = fileRead.readlines()
        linesEntrerResultat = {}
        for elt in lines:
            linesEntrerResultat[elt.split("\t\t=====>\t\t")[0]] = elt.split("\t\t=====>\t\t")[1].replace("\n", "")
        fileRead.close()
    return linesEntrerResultat

print("\t\t\tPrécedent calcul")
for key, val in resultatRead("fichier.txt").items():
    print("{}\t\t=====>\t\t{}\n".format(key, val))
print("\t\t\tcalcul actuel")
fenetre = tk.Tk() #Ouverture de la fenetre

""" Configuration de la fenetre """
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
fenetre.geometry("%dx%d+%d+%d" %(350,400,(fenetre.winfo_screenwidth()-750)/2,(fenetre.winfo_screenheight()-580)/2))
fenetre.minsize(350,400)
fenetre.maxsize(350,400)
fenetre.config(bg="white")
fenetre.title("Calculatrice")
fenetre.tk.call('wm', 'iconphoto', fenetre._w, tk.PhotoImage(file='cal.png'))


""" Fin de la Configuration de la fenetre """


""" configuration de la fenetre de la calculatrice"""
''' libelle = ttk.Label(fenetre, text = 'label', font = ("arial", 10, "bold"))
libelle.place(x = 0, y = 0) '''

touche = '0'


def onKey(event):
    global touche
    touche=event.char
def valider():
    global touche
    if touche in "0123456789/x-+%.":
        return True
    else: return False


varDansEcran = tk.StringVar()

ecranAffichage = ttk.Entry(fenetre,font = ("arial", 20, "bold"), textvariable=varDansEcran)
ecranAffichage.configure(validate="key",validatecommand=valider)
ecranAffichage.bind("<Key>",onKey)
ecranAffichage.insert(0, 0)
ecranAffichage.place(x=15,y=15)


def recupererVarEcran():
    print(varDansEcran.get())

#Fonction d'affichage
def affiche(nombre: str):
    global ecranAffichage, varDansEcran, touche
    touche = nombre
    
    if "Error" in varDansEcran.get():
        varDansEcran.set("")
        ecranAffichage.insert(0, nombre)
    elif len(varDansEcran.get()) == 1 :
        if not varDansEcran.get().isdigit():
            if varDansEcran.get() in "+-":
                ecranAffichage.insert(len(varDansEcran.get()), nombre)
            else:
                varDansEcran.set("")
                ecranAffichage.insert(0, nombre)
        elif varDansEcran.get() == "0" and nombre in "0123456789-+":
            varDansEcran.set("")
            ecranAffichage.insert(0, nombre)
        else:
            ecranAffichage.insert(len(varDansEcran.get()), nombre)
    else:
        ecranAffichage.insert(len(varDansEcran.get()), nombre)

def equal():
    global varDansEcran

    saisi = varDansEcran.get()
    
    if "%" in saisi :
        saisi = saisi.replace('%', '/100')
    if "x" in saisi :
        saisi = saisi.replace('x', '*')
    
    try:
        total = eval(saisi)
    except SyntaxError as e:
        total = "Error Syntax"
    except ZeroDivisionError as e:
        total = "Zero Division Error"
    except NameError as e:
        total = "Error Number"
    except Exception as e:
        total = "Error"

    varDansEcran.set("")
    ecranAffichage.insert(0, total)
    
    print("{}\t\t=====>\t\t{}\n".format(saisi, total))
    with open("fichier.txt", "a+") as file:
        file.write("{}\t\t=====>\t\t{}\n".format(saisi, total))
        file.close()

def supprimerTout():
    global varDansEcran
    varDansEcran.set("0")

def supprimerDernierElement():
    global varDansEcran
    saisiEnList = list(varDansEcran.get())
    if len(saisiEnList) > 1 :
        saisiEnList.pop(-1)
        varDansEcran.set("")
        ecranAffichage.insert(0, ''.join(saisiEnList))
    else:
        varDansEcran.set("")
        ecranAffichage.insert(0, "0")
    
    
    
   

#ttk.Button(fenetre, text="Affiche", padding = 5, command=recupererVarEcran).place(x=20, y=80)


on = ttk.Button(fenetre, text="ON", padding = 5, command=supprimerTout)
on.place(x=5, y=150)

mc = ttk.Button(fenetre, text="MC", padding = 5)
mc.place(x=90, y=150)

mPlus = ttk.Button(fenetre, text="Sup", padding = 5, command=supprimerDernierElement)
mPlus.place(x=175, y=150)

pourcentage = ttk.Button(fenetre, text="%", padding = 5, command=lambda:affiche("%"))
pourcentage.place(x=260, y=150)


sept = ttk.Button(fenetre, text="7", padding = 5, command=lambda:affiche("7"))
sept.place(x=5, y=200)

huit = ttk.Button(fenetre, text="8", padding = 5, command=lambda:affiche("8"))
huit.place(x=90, y=200)

neuf = ttk.Button(fenetre, text="9", padding = 5, command=lambda:affiche("9"))
neuf.place(x=175, y=200)

plus = ttk.Button(fenetre, text="+", padding = 5, command=lambda:affiche("+"))
plus.place(x=260, y=200)


quatre = ttk.Button(fenetre, text="4", padding = 5, command=lambda:affiche("4"))
quatre.place(x=5, y=250)

cinq = ttk.Button(fenetre, text="5", padding = 5, command=lambda:affiche("5"))
cinq.place(x=90, y=250)

six = ttk.Button(fenetre, text="6", padding = 5, command=lambda:affiche("6"))
six.place(x=175, y=250)

moins = ttk.Button(fenetre, text="-", padding = 5, command=lambda:affiche("-"))
moins.place(x=260, y=250)


un = ttk.Button(fenetre, text="1", padding = 5, command=lambda:affiche("1"))
un.place(x=5, y=300)

deux = ttk.Button(fenetre, text="2", padding = 5, command=lambda:affiche("2"))
deux.place(x=90, y=300)

trois = ttk.Button(fenetre, text="3", padding = 5, command=lambda:affiche("3"))
trois.place(x=175, y=300)

fois = ttk.Button(fenetre, text="X", padding = 5, command=lambda:affiche("x"))
fois.place(x=260, y=300)


zero = ttk.Button(fenetre, text="0", padding = 5, command=lambda:affiche("0"))
zero.place(x=5, y=350)

point = ttk.Button(fenetre, text=".", padding = 5, command=lambda:affiche("."))
point.place(x=90, y=350)

egale = ttk.Button(fenetre, text="=", padding = 5, command=equal)
egale.place(x=175, y=350)

division = ttk.Button(fenetre, text="/", padding = 5, command=lambda:affiche("/"))
division.place(x=260, y=350)









""" Fin de la configuration de la fenetre de la calculatrice"""


fenetre.mainloop()

