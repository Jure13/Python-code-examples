import copy
import time

def citajPisiListuSusjedstva(datoteka):
    listaSusjedstva = {}

    with open(datoteka, 'r') as dat:
        vrhovi = False
        usmjereni = False

        redovi = dat.readlines()
        for red in redovi:
            if "*vertices" in red:
                vrhovi = True
            if "*arcs" in red:
                usmjereni = True
                vrhovi = False         
            else:
                if red.strip():                    
                    if vrhovi == True:
                        if "*vertices" not in red:
                            listaSusjedstva[int(red.split()[0])] = []
                    if usmjereni == True:
                        if "*arcs" not in red:
                            pocetni, ciljni, tezina = red.split()
                            listaSusjedstva[int(pocetni)].append((int(ciljni), int(tezina)))
    return listaSusjedstva
    
    

if __name__ == "__main__":
    listaSusjedstva = citajPisiListuSusjedstva("airports-split.net.txt")
    for key, value in listaSusjedstva.items():
        print(key, ":", value)
        
    temp1 = copy.deepcopy(listaSusjedstva)
    print("Lista:\n - broj čvorova je", len(temp1), "\n - početni čvor je čvor \"0\"")
    
    print("\nPrimov algoritam:")
    prim = [0]
    kandidati = []
    početak = time.time()
    while(len(prim) != len(temp1.items())):
        for key, value in temp1.items():
            if key in prim or key in kandidati:
                min = float("inf")
                for i in value:
                    if i[0] not in prim:
                        if i[1] < min:
                            min = i[1]
                i = 0
                for i in value:
                    if min == i[1]:
                        if i[0] not in prim:
                            prim.append(i[0])
                            check = 1
                    else:
                        if i[0] not in prim and i[0] not in kandidati:
                            kandidati.append(i[0])
                if check == 1:
                    check = 0
                    break
    kraj = time.time()                
    
    print("Početni: ", end = "")
    for čvor in prim:
        print("",čvor, "=>",end ="")
    print(" Kraj")
    print("Izvršen za ", kraj - početak, " sekundi!")
