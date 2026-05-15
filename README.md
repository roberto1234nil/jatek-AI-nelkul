Python Szöveges RPG Játék
Ez egy konzol alapú, körökre osztott harci rendszeren alapuló szerepjáték (RPG), amely Python nyelven készült. A játék célja a túlélés minél több szinten keresztül, miközben karaktered fejlődik, szörnyeket győz le és kincseket gyűjt.

Kiválasztott Téma
Téma: Interaktív kalandjáték külső adatkezeléssel.
A program komplex osztálystruktúrát használ, kezeli az inventory-t, a szintezést, és JSON alapú külső adatforrásokat használ a mentések tárolására és betöltésére.

Főbb Funkciók
Karakterkészítés: Három különböző kaszt (Harcos, Mágus, Íjász) egyedi statisztikákkal (HP, Sebzés, Mana).

Körökre osztott harc: Taktikai döntések (támadás, gyógyítás, mentés/kilépés).

Dinamikus nehézség: A szörnyek életereje és sebzése szintenként skálázódik.

Fejlődési rendszer: Tapasztalati pont (XP) gyűjtése, szintlépés statisztikai bónuszokkal.

Mentési rendszer: A játékos elnevezheti a mentését, amit a program .json fájlként tárol. Indításkor listázza az elérhető mentéseket.

Permanens halál: Ha a karakter életereje elfogy, a mentett állás automatikusan törlődik a kihívás érdekében.

Fájlszerkezet
rpg_jatek.py: A fő futtatható Python kód.

[karakternev].json: Automatikusan generált mentési fájlok (JSON formátum).

Használati útmutató
Előfeltételek
A futtatáshoz csak a Python 3.x verzióra van szükség. Külső könyvtárakat (a standard library-n kívül) nem igényel.

Futtatás
Töltsd le vagy másold ki a kódot egy fájlba, például: rpg_jatek.py.

Nyisd meg a terminált / parancssort a fájl mappájában.

Futtasd a következő paranccsal:

Bash
python rpg_jatek.py
Játékmenet
Indítás: Válassz a korábbi mentések közül, vagy hozz létre újat.

Harc: A körödben válaszd az 1, 2 vagy 3 opciókat.

Mentés: Ha abba szeretnéd hagyni, a harc közben válaszd a mentés opciót, így később onnan folytathatod.
