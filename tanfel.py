with open("beosztas.txt", "r", encoding="utf-8") as fi:
    beosztas_list = fi.read().split("\n")
    
beosztas = []
for i in range(0, len(beosztas_list), 4):
    beosztas.append({"nev": beosztas_list[i],
                     "tantargy": beosztas_list[i+1],
                     "osztaly": beosztas_list[i+2],
                     "oraszam": int(beosztas_list[i+3])})

def get_osszoraszam(l):
    o = 0
    for item in l:
        o+=item['oraszam']
    return o

def get_oraszam(t, l):
    o = 0
    for e in l:
        if e['nev'] == t:
            o+=e['oraszam']
    return o

def get_csopbontas(o, t, l):
    o_sz = o.split(".")[0]
    i = 0
    while i<len(l) and not (l[i]['osztaly'] == f"{o_sz}.x" and l[i]['tantargy'] == t):
        i+=1
    return i<len(l)

def get_ossztanar(l):
    d = []
    for i in l:
        if i['nev'] not in d:
            d.append(i['nev'])
    return len(d)

def get_ossztanar_alt(l):
    t = []
    for i in l:
        t.append(i['nev'])
    return len(list(dict.fromkeys(t)))

print(f"2. feladat\nA fájlban {len(beosztas)} bejegyzés van.")
print(f"3. feladat\nAz iskolában a heti összóraszám: {get_osszoraszam(beosztas)}")
print("4. feladat")
tanar_neve = input("Add meg egy tanár nevét: ") or "Albatrosz Aladin"
print(f"Heti óraszáma: {get_oraszam(tanar_neve, beosztas)}")
print("6. feladat")
osztaly = input("Adj meg egy osztályt: ") or "10.b"
tantargy = input("Adj meg egy tantárgyat: ") or "matematika"
if get_csopbontas(osztaly, tantargy, beosztas):
    print("Csoportbontásban vannak.")
else:
    print("Nincsenek csoportbontásban.")
print(f"7. feladat\nAz iskolában {get_ossztanar(beosztas)} tanár tanít.")