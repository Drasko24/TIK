def osvjezi_rjecnik(rjecnik):
    for key in rjecnik:
        rjecnik[key] = rjecnik[key][0:2] + '0' + rjecnik[key][2:]


def stepen_dvojke(num):
    while num % 2 == 0:
        num /= 2
    return num == 1


def inicijalizuj_rjecnik():
    rjecnik = dict()
    pocetna_duzina = 8 + 2
    for i in range(256):
        rjecnik[str(i)] = bin(i)
        temp = len(rjecnik[str(i)])
        if temp < pocetna_duzina:
            rjecnik[str(i)] = rjecnik[str(i)][0:2] + (pocetna_duzina - temp) * '0' + rjecnik[str(i)][2:]
    return rjecnik


def vrati_kljuc(rjecnik, trenutni, prosli):
    try:
        return list(rjecnik.keys())[list(rjecnik.values()).index(trenutni)]
    except:
        return list(rjecnik.keys())[list(rjecnik.values()).index(prosli)]


def dekodiranje(kod):
    rjecnik = inicijalizuj_rjecnik()
    duzina = len(kod)
    index = 256
    i = 0
    dekodirana_poruka = []
    dekodirana_poruka.extend([vrati_kljuc(rjecnik, kod[i], 0)])
    i += 1
    while i < duzina:
        stara = vrati_kljuc(rjecnik, kod[i - 1], 0)
        if stepen_dvojke(index):
            osvjezi_rjecnik(rjecnik)
            nova = vrati_kljuc(rjecnik, kod[i], kod[i-1][0:2]+'0'+kod[i-1][2:])
        else:
            nova = vrati_kljuc(rjecnik, kod[i], kod[i - 1])
        nova = nova.split()[0]
        fraza = stara + " " + nova
        rjecnik[fraza] = bin(index)
        index += 1
        dek = vrati_kljuc(rjecnik, kod[i], 0)
        dek = dek.split()
        dekodirana_poruka.extend(dek)
        i += 1
    for i in range(len(dekodirana_poruka)):
        dekodirana_poruka[i] = int(dekodirana_poruka[i])
    return dekodirana_poruka
