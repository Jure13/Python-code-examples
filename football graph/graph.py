import copy

def citajPisiListuSusjedstva(datoteka):
    listaSusjedstva = {}

    with open(datoteka, 'r') as dat:
        vrhovi = False
        bridovi = False
        usmjereni = False

        redovi = dat.readlines()
        for red in redovi:
            if "*Vertices" in red:
                vrhovi = True
            if "*Arcs" in red:
                usmjereni = True
                vrhovi = False
            if "*Edges" in red:
                bridovi = True 
                usmjereni = False           
            else:
                if red.strip():                    
                    if vrhovi == True:
                        if "*Vertices" not in red:
                            #provjera
                            listaSusjedstva[int(red.split()[0])] = []
                        #print(red)
                    if usmjereni == True:
                        if "*Arcs" not in red:
                            #print(red)
                            pocetni, ciljni, tezina = red.split()
                            #print(pocetni, ciljni)
                            listaSusjedstva[int(pocetni)].append((int(ciljni), int(tezina)))
                            #print(listaSusjedstva)
                    if bridovi == True:
                        if "*Edges" not in red:
                            #print(red)
                            pocetni, ciljni = red.split()
                            #print(pocetni, ciljni)
                            listaSusjedstva[int(pocetni)].append(int(ciljni))
                            listaSusjedstva[int(ciljni)].append(int(pocetni))     
                            #print(listaSusjedstva)
        dat.seek(0,0)
    return listaSusjedstva
    
    
def printListu(lista):
    i = 0
    print("Lista susjedstva:")
    for key, value in lista.items():
        for i in range(len(value)):
            print("Iz", key, "u", value[i][0], "je težina", value[i][1])


def ulazniStupanj(lista):
    i = 0
    ulazi = {}
    
    for key, value in lista.items():
        for i in range(len(value)):
            if value[i][0] in lista.keys():
                if value[i][0] in ulazi.keys():
                    ulazi[int(value[i][0])] = ulazi[int(value[i][0])] + int(value[i][1])
                else:
                    ulazi[int(value[i][0])] = int(value[i][1])
                    
    for key, value in ulazi.items():
        print("Ulaz od", key, "ima vrijednost", value)
    
    return ulazi


def izlazniStupanj(lista):
    i = 0
    brojac = 0
    
    for key, value in lista.items():
        brojac = 0
        for i in range(len(value)):
            brojac += value[i][1]
        print("Izlaz od", key, "ima vrijednost", brojac)


def izvoz(lista):
    i = 0
    brojac = 0
    izvozi = {}
    maks = 0
    temp = 0
    
    for key, value in lista.items():
        brojac = 0
        for i in range(len(value)):
            brojac += value[i][1]
        izvozi[key + 1] = brojac
        
    for key, value in izvozi.items():
        if value >= maks:
            maks = value
            temp = key
    
    with open("football.net.txt", 'r') as dat:
        vrhovi = False
        bridovi = False
        usmjereni = False

        redovi = dat.readlines()
        for red in redovi:
            if "*Vertices" in red:
                vrhovi = True
            if "*Arcs" in red:
                usmjereni = True
                vrhovi = False
            if "*Edges" in red:
                bridovi = True 
                usmjereni = False
                vrhovi = False           
            else:
                if red.strip():                    
                    if vrhovi == True:
                        if "*Vertices" not in red:
                            if int(red.split()[0]) == temp:
                                naziv = red.split()[1]
                                
        dat.seek(0,0)    
    print("Država", temp - 1, ",", naziv, "ima najviše izvoza:", maks)


def uvoz(lista):
    maks = 0
    temp = 0
    
    for key, value in lista.items():
        if value >= maks:
            maks = value
            temp = key
    
    with open("football.net.txt", 'r') as dat:
        vrhovi = False
        bridovi = False
        usmjereni = False

        redovi = dat.readlines()
        for red in redovi:
            if "*Vertices" in red:
                vrhovi = True
            if "*Arcs" in red:
                usmjereni = True
                vrhovi = False
            if "*Edges" in red:
                bridovi = True 
                usmjereni = False
                vrhovi = False           
            else:
                if red.strip():                    
                    if vrhovi == True:
                        if "*Vertices" not in red:
                            if int(red.split()[0]) == temp:
                                naziv = red.split()[1]
                                
        dat.seek(0,0)
    print("Država", temp, ",", naziv, "ima najviše uvoza:", maks)


if __name__ == "__main__":
    listaSusjedstva = citajPisiListuSusjedstva("football.net.txt")
    printListu(listaSusjedstva)
    print("")
    print(listaSusjedstva)
    temp1 = copy.deepcopy(listaSusjedstva)
    ulazi = ulazniStupanj(temp1)
    print("")
    
    temp2 = copy.deepcopy(listaSusjedstva)
    izlazniStupanj(temp2)
    print("")
    
    temp3 = copy.deepcopy(listaSusjedstva)
    izvoz(temp3)
    print("")
    
    temp4 = copy.deepcopy(ulazi)
    uvoz(temp4)
    print("")