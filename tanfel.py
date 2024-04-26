with open("beosztas.txt", "r", encoding="utf-8") as fi:
    beosztas_lista = fi.read().split("\n")
    
beosztas = []
for i in range(0, len(beosztas_lista), 4):
    beosztas.append({"nev": beosztas_lista[i],
                     "tantargy": beosztas_lista[i+1],
                     "osztaly": beosztas_lista[i+2],
                     "oraszam": int(beosztas_lista[i+3])})

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

def get_tanarlista(l):
    t = []
    for i in l:
        if i['nev'] not in t:
            t.append(i['nev'])
    return t

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
print(f"7. feladat\nAz iskolában {len(get_tanarlista(beosztas))} tanár tanít.")

tanarok_egyedi = get_tanarlista(beosztas)
with open("tanarok.txt", "w", encoding="utf-8") as fo:
    for tanar in tanarok_egyedi:
        print(tanar, file=fo)