from functions import osvjezi_rjecnik, stepen_dvojke, inicijalizuj_rjecnik, dekodiranje
import matplotlib.image as img
import numpy as np
import matplotlib.pyplot as plt

rjecnik = inicijalizuj_rjecnik()
index = 256
image = img.imread('sah.bmp')
dim = image.shape
poruka = image.reshape(-1)
duzina = len(poruka)
kod = ''
i = 0
while i < duzina - 1:
    elem = str(poruka[i]) + " " + str(poruka[i+1])
    i += 1
    while elem in rjecnik and i < duzina - 1:
        i += 1
        elem += " " + str(poruka[i])
    if elem in rjecnik:
        kod += " " + rjecnik[elem]
    else:
        kod += " " + rjecnik[" ".join(elem.split()[:-1])]
        if i == duzina - 1:
            kod += " " + rjecnik[elem.split()[-1]]
        if stepen_dvojke(index):
            osvjezi_rjecnik(rjecnik)
        rjecnik[elem] = bin(index)
        index += 1
kod = kod.split()
brbita2 = 0
for rijec in kod:
    brbita2 += (len(rijec)-2) #jer su binarni brojevi u formi stringa: 0b + binarni zapis
print(f'Dužina kodne riječi: {brbita2}')
print(f'Dužina originalne poruke: {duzina*8}')
print(f'Ušteda memeorijskog prostora: {round((1-brbita2/(duzina*8))*100,2)}%')
poruka = list(poruka)
dekodirana = dekodiranje(kod)
suma = 0
suma = sum((a - b)**2 for a, b in zip(poruka, dekodirana))
print(f'Suma kvadrata grešaka: {suma}')
nova_slika = np.array(dekodirana, dtype='uint8')
nova_slika = nova_slika.reshape(dim)
plt.imshow(nova_slika, cmap='gray')
plt.show()
