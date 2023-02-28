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
    
def poredajBridove(lista):
    bridovi = []
    for key, value in lista.items():
            for i in value:
                if i[1] not in bridovi:
                    bridovi.append(i[1])
    return sorted(bridovi)

if __name__ == "__main__":
    listaSusjedstva = citajPisiListuSusjedstva("airports-split.net.txt")
    for key, value in listaSusjedstva.items():
        print(key, ":", value)
        
    temp1 = copy.deepcopy(listaSusjedstva)
    print("Lista:\n - broj čvorova je", len(temp1), "\n - početni čvor je čvor \"0\"")
    
    print("\nKruskalov algoritam:")
    bridovi = poredajBridove(listaSusjedstva)
    kruskal = []
    kandidati = []
    pocetni = 0
    krajnji = 0
    checkP = 0
    checkTemp = 0
    
    početak = time.time()
    for brid in bridovi:
        for key, value in temp1.items():
            for i in value:
                if i[1] == brid and checkP == 0:
                    pocetni = i[0]
                    checkP = 1  
                    break               
                if i[1] == brid and checkP == 1:
                    krajnji = i[0]
                    checkP = 0
                    checkTemp = 1
                    break
            if checkTemp == 1:
                temp = (pocetni, brid, krajnji)
                if (temp[0] not in kruskal) and (temp[2] not in kruskal):
                    kruskal.append(temp)
                    checkTemp = 0
    kraj = time.time()
    
    print("Početni: ", end = "")
    for čvor in kruskal:
        print("",čvor, "=>",end ="")
    print(" Kraj")
    print("Izvršen za ", kraj - početak, " sekundi!")