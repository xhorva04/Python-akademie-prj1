# Projekt 01 – Tomáš H.
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

db_uzivatelu = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}


oddelovac = "_" * 64

uzivatel = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")

if db_uzivatelu.get(uzivatel) == heslo:
    print(oddelovac)
    print("Vitejte v Aplikaci:", uzivatel)
    print("K analyze jsou k dispozici 3 texty.")
    print(oddelovac)
else:
    print("Neplatne jmeno nebo heslo. Ukoncuji...")
    quit()

volba_textu = input("Zadejte text k analyze od 0 do 2: ")

if volba_textu.isdigit() and ((int(volba_textu)) in range(0, 3, 1)):
    print(oddelovac)
else:
    print("Zadej cislo v uvedeném rozsahu")
    quit()

pocet_slov = 0
prvni_velke = 0
vse_velke = 0
vse_male = 0
pocet_cisel = 0
ciselne_slovo = list()
soucet_cisel = 0

for slovo in TEXTS[int(volba_textu)].split():
    pocet_slov += 1
    if slovo.istitle():
        prvni_velke += 1
    if slovo.isupper():
        vse_velke += 1
    if slovo.islower():
        vse_male += 1
    if slovo.isnumeric():
        pocet_cisel += 1
    if slovo.isdigit():
        ciselne_slovo.append(int(slovo))

# Proč nemohu říct for INT(prvek) – prvek je int

for prvek in ciselne_slovo:
    soucet_cisel += int(prvek)


# Počítání délek slov ve for cyklu
a = 0

for slovo in TEXTS[int(volba_textu)].split():
    if len(slovo) == 4:
        a += 1


print(f"Celkový počet slov je: {pocet_slov}")
print(f"Počet slov zacinajici velkym pismene je: {prvni_velke}")
print(f"Počet slov, které jsou psané velkými písmeny: {vse_velke}")
print(f"Počet slov, které jsou psané malými písmeny: {vse_male}")
print(f"Celkově analyzovaný text obsahuje {pocet_cisel} čísel.")
print(f"Součet těchto čísel je: {soucet_cisel}")
print(oddelovac)