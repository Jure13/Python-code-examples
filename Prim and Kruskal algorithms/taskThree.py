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


if __name__ == "__main__":
    listaSusjedstva = citajPisiListuSusjedstva("football.net.txt")
    temp1 = copy.deepcopy(listaSusjedstva)
    temp2 = copy.deepcopy(listaSusjedstva)
    temp3 = copy.deepcopy(listaSusjedstva)
    temp4 = copy.deepcopy(listaSusjedstva)
    for key, value in listaSusjedstva.items():
        print(key, " : ", value)
    
    veze = []
    vezeBezBridova = []
    for key, value in temp1.items():
        for i in value:
            veze.append((key, i[1], i[0]))
    for veza in veze:
        vezeBezBridova.append((veza[0], veza[2]))
    
    print(vezeBezBridova)
    komponente = ["Prva: ", 1]
    while(1 > 0):
        for key, value in temp2.items():
            if key in komponente:
                for par in vezeBezBridova:
                    if key == par[0]:
                        if key not in komponente:
                            komponente.append(key)
                        if par[1] not in komponente:
                            komponente.append(par[1])
                    if key == par[1]:
                        if key not in komponente:
                            komponente.append(key)
                        if par[0] not in komponente:
                            komponente.append(par[0])
        komponente.append("Sljedeća: ")
        if(komponente[-1] == "Sljedeća: " and komponente[-2] == "Sljedeća: "):
            komponente = komponente[:-1]
            komponente = komponente[:-1]
            break
        for key in temp3.keys():
            if key not in komponente:
                komponente.append(key)
                break
    brojač = 1
    max = 0
    print(komponente)
    for član in komponente:
        if član == "Sljedeća: ":
            brojač += 1
        if len(komponente) > max:
            max = len(komponente)
            najveća = brojač
    print("Graf sadrži", brojač, "komponenti!")
    print("Najveća je", najveća,". komponenta!")
    
    print("Prva 3 čvora:\n")
    counter = 0
    for key, value in temp4.items():
        print("Čvor", key, "ima", len(value), "veza!")
        counter += 1
        if counter == 3:
            break
            