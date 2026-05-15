import random
import time
import json
import os

print("=== ÜDVÖZÖLLEK A KALANDBAN! ===")

jatekos = None
kilepes = False

# --- 1. BETÖLTÉS VAGY ÚJ JÁTÉK ---
mentesek = [f for f in os.listdir() if f.endswith('.json')]

if mentesek:
    print("\n=== ELÉRHETŐ MENTÉSEK ===")
    for i, mentes in enumerate(mentesek):
        print(f"{i + 1}. {mentes}")
    print("0. Új játék indítása")

    valasztas = input("\nVálassz egy számot: ")
    if valasztas != "0" and valasztas.isdigit():
        index = int(valasztas) - 1
        if 0 <= index < len(mentesek):
            with open(mentesek[index], "r", encoding="utf-8") as f:
                jatekos = json.load(f)

# Ha nem töltöttünk be semmit, hozzunk létre egy új karaktert
if jatekos is None:
    print("\n=== ÚJ KARAKTER LÉTREHOZÁSA ===")
    nev = input("Add meg a karaktered nevét (ez lesz a mentés neve is): ").strip()
    if not nev:
        nev = "Hero"

    hosok = [
        {"kaszt": "Harcos", "hp": 150, "atk": 20, "mana": 10},
        {"kaszt": "Mágus", "hp": 80, "atk": 30, "mana": 60},
        {"kaszt": "Íjász", "hp": 110, "atk": 25, "mana": 25}
    ]

    print("\nVálassz kasztot:")
    for i, h in enumerate(hosok):
        print(f"{i + 1}. {h['kaszt']} (HP: {h['hp']}, ATK: {h['atk']})")

    v = input("Választás: ")
    if v.isdigit() and 0 < int(v) <= len(hosok):
        k = hosok[int(v) - 1]
    else:
        k = hosok[0]

    jatekos = {
        "nev": nev,
        "kaszt": k["kaszt"],
        "hp": k["hp"],
        "max_hp": k["hp"],
        "tamadas": k["atk"],
        "mana": k["mana"],
        "inventory": ["Gyógyital"],
        "szint": 1,
        "xp": 0
    }

# --- 2. FŐ JÁTÉK CIKLUS ---
kor = jatekos["szint"]

# Addig fut a játék, amíg élünk, és nem kértük a kilépést
while jatekos["hp"] > 0 and not kilepes:

    # --- 3. HARC ELŐKÉSZÍTÉSE ---
    szornyek = ["Goblin", "Farkas", "Ork", "Gonosz Programozó"]
    e_nev = random.choice(szornyek)
    e_hp = 30 + (kor * 15)
    e_atk = 5 + (kor * 5)

    print(f"\n--- ELLENSÉG: {e_nev} (Szint: {kor}) ---")

    # --- 4. MAGA A HARC  ---
    while jatekos["hp"] > 0 and e_hp > 0:
        print(f"\n{jatekos['nev']} ({jatekos['hp']} HP) vs {e_nev} ({e_hp} HP)")
        valasz = input("1. Támadás | 2. Gyógyítás | 3. Mentés és Kilépés: ")

        # 3. Mentés és Kilépés
        if valasz == "3":
            fajlnev = f"{jatekos['nev']}.json"
            with open(fajlnev, "w", encoding="utf-8") as f:
                json.dump(jatekos, f, ensure_ascii=False, indent=4)
            print(f"\n>>> Játék elmentve mint: {fajlnev} <<<")

            kilepes = True  # Beállítjuk a kilépés jelzőt
            break  # Megszakítjuk a belső (harc) ciklust

        # 1. Támadás
        if valasz == "1":
            seb = random.randint(jatekos["tamadas"] - 5, jatekos["tamadas"] + 5)
            e_hp -= seb
            print(f"> Okoztál {seb} sebzést!")

        # 2. Gyógyítás
        elif valasz == "2":
            if "Gyógyital" in jatekos["inventory"]:
                jatekos["hp"] = min(jatekos["max_hp"], jatekos["hp"] + 40)
                jatekos["inventory"].remove("Gyógyital")
                print("> HP feltöltve! (+40)")
            else:
                print("> Nincs gyógyitalod!")

        # A szörny visszatámad, ha még él és nem léptünk ki
        if e_hp > 0 and not kilepes:
            s_seb = random.randint(e_atk - 2, e_atk + 2)
            jatekos["hp"] -= s_seb
            print(f"> {e_nev} visszacsapott: {s_seb} sebzés!")

    # --- 5. HARC UTÁNI ESEMÉNYEK ---

    # Ha mentettünk, megszakítjuk a külső ciklust is, vége a programnak
    if kilepes:
        break

    # Ha meghaltunk
    if jatekos["hp"] <= 0:
        print(f"\n{jatekos['nev']} elesett a harcban. A mentés törlődik.")
        if os.path.exists(f"{jatekos['nev']}.json"):
            os.remove(f"{jatekos['nev']}.json")
        break  # Kilépünk a külső ciklusból, vége a játéknak

    # Győzelem
    jatekos["xp"] += 50 + (kor * 10)

    # Szintlépés ellenőrzése
    szukseges_xp = jatekos["szint"] * 100
    if jatekos["xp"] >= szukseges_xp:
        jatekos["szint"] += 1
        jatekos["xp"] -= szukseges_xp
        jatekos["max_hp"] += 20
        jatekos["hp"] = jatekos["max_hp"]
        jatekos["tamadas"] += 5
        print(f"\n✨ SZINTLÉPÉS! Mostantól {jatekos['szint']}. szintű vagy!")

    # Esély gyógyitalra
    if random.random() < 0.3:
        jatekos["inventory"].append("Gyógyital")

    kor += 1
    print("\nKövetkező kör...")
    time.sleep(1)


print("\n=== JÁTÉK VÉGE ===")
