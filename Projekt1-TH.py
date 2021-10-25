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

oddelovac = "_" * 48

uzivatel = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")

if db_uzivatelu.get(uzivatel) == heslo:
    print(oddelovac)
    print("Vítejte v Aplikaci:", uzivatel)
    print("K analýze jsou k dispozici 3 texty.")
    print(oddelovac)
else:
    print("Neplatné jméno nebo heslo. Ukončuji...")
    quit()

volba_textu = input("Zadejte text k analýze od 1 do 3: ")

if volba_textu.isdigit() and ((int(volba_textu) - 1) in range(0, 3)):
    print(oddelovac)
else:
    print("Zadej číslo v uvedeném rozsahu!")
    quit()

pocet_slov = 0
prvni_velke = 0
vse_velke = 0
vse_male = 0
pocet_cisel = 0
ciselne_slovo = list()
soucet_cisel = 0

for slovo in TEXTS[int(volba_textu) - 1].split():
    pocet_slov += 1
    if slovo.istitle():
        prvni_velke += 1
    elif slovo.isupper():
        vse_velke += 1
    elif slovo.islower():
        vse_male += 1
    elif slovo.isnumeric():
        pocet_cisel += 1
        ciselne_slovo.append(int(slovo))

# Součet všech čísel z vytvořeného listu
for prvek in ciselne_slovo:
    soucet_cisel += int(prvek)

# Výpis podle zadání
print(f"Celkový počet slov je: {pocet_slov}.")
print(f"Počet slov začínající velkým písmenem je: {prvni_velke}.")
print(f"Počet slov, které jsou psané velkými písmeny: {vse_velke}.")
print(f"Počet slov, které jsou psané malými písmeny: {vse_male}.")
print(f"Celkově analyzovaný text obsahuje {pocet_cisel} číslice.")
print(f"Součet těchto čísel je: {soucet_cisel}.")
print(oddelovac)

# Počítání délek slov ve for cyklu
pocty_slov = dict()


# Výpočet délek slov a uložení typu klíč:hodnota do slovníčku -- nutno stripnout nežádoucí znaky u slova
for slovo in TEXTS[int(volba_textu) - 1].split():
    slovo = slovo.rstrip(",.:;")
    delka = len(slovo)
    if delka not in pocty_slov:
        pocty_slov[delka] = 0

    pocty_slov[delka] += 1

# Serazeni slovnicku klíč:hodnota
pocty_slov_sorted = dict(sorted(zip(pocty_slov.keys(), pocty_slov.values())))

# Formátování nadpisu pro graf
print(" LEN|".ljust(4), " OCCURENCES".ljust(14), "|NR".rjust(7))
print(oddelovac)

# Vykresleni grafu se správným odsazením
for i, hodnota in enumerate(pocty_slov_sorted.values()):
    print(f"{(i + 1):4}|  {'*' * hodnota:17} |{hodnota:1}")
