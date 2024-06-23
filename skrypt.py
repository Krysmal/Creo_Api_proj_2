import creopyson
import subprocess
import time
import pprint
import os

pathStart="C:\Program Files\PTC\Creo 9.0.3.0\Parametric\\bin\parametric.bat"

c = creopyson.Client()

c.connect()



def wait(c) -> None:
    i = 0
    while i < 20:
        if isCreoRunning(c):
            return
        time.sleep(5)
        i = i + 1
    return

def isCreoRunning(c) -> bool:
    try:
        c.disconnect()
        c.connect()
        c.creo_get_config()
        return True
    except:
        return False

if c.is_creo_running() == False:
    subprocess.Popen(pathStart)
    print('Uruchamianie') 
    wait(c)
    print('Gotowe')
else:
    print('Gotowe')

c.creo_set_creo_version(9)

c.creo_cd("C:\\Users\\CAD\Desktop\\Krzysztof Malinowski\\P2")

while(True):

    path=input("podaj ścieżkę ")
    while not os.path.isdir(path):
        path=input("podaj poprawną ścieżkę ")

    c.file_open("model.prt")

    roz=input("Podaj numer klasy W (1-9) ")

    while not (roz.isdigit() and int(roz)>=1 and int(roz)<=9):
        roz=input("Podaj numer klasy W (1-9) ")

    class typ:
        def __init__(self,A,B,C,D,E,F,name):
            self.A=A
            self.B=B
            self.C=C
            self.D=D
            self.E=E
            self.F=F
            self.name=name

    WWYB=typ(100,100,8,100,36,10,"W1")
    W1=typ(100,100,8,100,36,10,"W1")
    W2=typ(100,140,8,100,36,10,"W2")
    W3=typ(100,180,8,100,36,10,"W3")
    W4=typ(140,100,10,100,38,12,"W4")
    W5=typ(140,140,10,100,38,12,"W5")
    W6=typ(140,180,10,100,38,12,"W6")
    W7=typ(180,100,11,100,40,14,"W7")
    W8=typ(180,140,11,100,40,14,"W8")
    W9=typ(180,180,11,100,40,14,"W9")

    if int(roz)==1:
        WWYB=W1

    elif int(roz)==2:
        WWYB=W2
    elif int(roz)==3:
        WWYB=W3
    elif int(roz)==4:
        WWYB=W4
    elif int(roz)==5:
        WWYB=W5
    elif int(roz)==6:
        WWYB=W6
    elif int(roz)==7:
        WWYB=W7
    elif int(roz)==8:
        WWYB=W8
    elif int(roz)==9:
        WWYB=W9
    else:
        print("błąd wyboru klasy ")


    c.feature_resume(name="OTW_180_A")


    c.feature_resume(name="OTW_180_A")
    c.feature_resume(name="OTW_140_A")
    c.feature_resume(name="OTW_O1_A")
    c.feature_resume(name="OTW_O2_A")
    c.feature_resume(name="R_OTW_A")


    c.feature_resume(name="OTW_180_B")


    c.feature_resume(name="OTW_180_B")
    c.feature_resume(name="OTW_140_B")
    c.feature_resume(name="OTW_O1_B")
    c.feature_resume(name="OTW_O2_B")
    c.feature_resume(name="R_OTW_B")


    c.parameter_set("A",value=WWYB.A)
    c.parameter_set("B",value=WWYB.B)
    c.parameter_set("C",value=WWYB.C)
    c.parameter_set("D",value=WWYB.D)
    c.parameter_set("E",value=WWYB.E)
    c.parameter_set("F",value=WWYB.F)

    c.file_load_material_file("STEEL_CAST","C:\\Program Files\\PTC\\Creo 9.0.3.0\\Common Files\\text\materials-library\\Standard-Materials_Granta-Design\\Ferrous_metals")
    c.file_load_material_file("ALUMINUM_WROUGHT","C:\\Program Files\\PTC\\Creo 9.0.3.0\\Common Files\\text\materials-library\\Standard-Materials_Granta-Design\\Non-ferrous_metals")
    c.file_load_material_file("ABS","C:\\Program Files\\PTC\\Creo 9.0.3.0\\Common Files\\text\materials-library\\Standard-Materials_Granta-Design\\Plastics")


    c.file_set_cur_material("STEEL_CAST")

    mat=input("Podaj materiał 1-stal, 2-aluminium, 3-plastik ")

    while not (mat.isdigit() and int(mat)>=1 and int(mat)<=3):
        mat=input("Podaj materiał 1-stal, 2-aluminium, 3-plastik ")

    if int(mat)==1:
        c.file_set_cur_material("STEEL_CAST")
    elif int(mat)==2:
        c.file_set_cur_material("ALUMINUM_WROUGHT")
    elif int(mat)==3:
        c.file_set_cur_material("ABS")
    else:
        print("błąd wyboru materiału ")

    if WWYB.A==140:
        c.feature_suppress(name="OTW_180_A")

    if WWYB.A==100:
        c.feature_suppress(name="OTW_180_A")
        c.feature_suppress(name="OTW_140_A")
        c.feature_suppress(name="OTW_O1_A")
        c.feature_suppress(name="OTW_O2_A")
        c.feature_suppress(name="R_OTW_A")

    if WWYB.B==140:
        c.feature_suppress(name="OTW_180_B")

    if WWYB.B==100:
        c.feature_suppress(name="OTW_180_B")
        c.feature_suppress(name="OTW_140_B")
        c.feature_suppress(name="OTW_O1_B")
        c.feature_suppress(name="OTW_O2_B")
        c.feature_suppress(name="R_OTW_B")


    c.file_regenerate()
    mass=c.file_massprops()
    file = open('model.txt', 'w')
    file.write("Nazwa: "+ WWYB.name)
    file.write("\nA="+ str(WWYB.A))
    file.write("\nB="+ str(WWYB.B))
    file.write("\nC="+ str(WWYB.C))
    file.write("\nD="+ str(WWYB.D))
    file.write("\nE="+ str(WWYB.E))
    file.write("\nF="+ str(WWYB.F))
    file.write("\nNazwa materiału: "+ str(c.file_get_cur_material()))
    file.write("\nMasa modelu: "+ str(mass.get("mass")))
    file.close()

    c.interface_export_file("STEP")

    c.interface_export_3dpdf(sheet_range="all")

    export=input("Czy wyeksportowac do modelu złożenia? (tak/nie) ")

    if str(export)=="tak":
        c.file_save()
        c.file_close_window()
        c.file_open("zlozenie.asm")
        c.file_assemble("model.prt")
    else:
        print("ok")

    loop=input("Czy kontynuować? (tak/nie)")

    if not loop=="tak":
        break
    
