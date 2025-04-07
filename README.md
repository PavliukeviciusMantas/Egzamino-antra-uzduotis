**Kelionių Registratorius**

Kelionių registratorius – tai administracinė aplikacija, sukurta naudojant PyQt6 ir SQLite. Ji leidžia valdyti kelionių registracijas: kurti, peržiūrėti, atnaujinti ir trinti duomenis.

Funkcionalumas

✅ Kurti naujus kelionių įrašus

📋 Peržiūrėti ir filtruoti įrašus lentelėje

✏️ Redaguoti pasirinktus įrašus

❌ Ištrinti nereikalingus įrašus

🔐 Tikrinamas el. pašto ir telefono numerio formatas

💾 Duomenys saugomi keliones.db SQLite duomenų bazėje

**Naudojimo instrukcija**

Įsitikinkite, kad turite įdiegtą Python 3.9+.

Įdiekite PyQt6:
```
pip install PyQt6
```
Paleiskite programą:

python main.py

**Naudokite vartotojo sąsają duomenims įvesti ir valdyti.**

*Laukai*

*Vardas*

*Pavardė*

*El. paštas – turi būti galiojantis formatas (pvz., vardas@pavyzdys.lt, test@example.com)*

*Telefono numeris – turi prasidėti +370 ir turėti 8 skaitmenis (pvz., +37061234567)*

*Išvykimo vieta*

*Atvykimo vieta*

**Katalogo struktūra**

kelioniu_registratorius/

├── main.py              # Pagrindinis aplikacijos kodas

├── keliones.db          # SQLite duomenų bazė

├── keliones.ui          # Qt Designer sukurtas UI failas

├── keliones.py          # Sugeneruotas Python failas iš .ui (naudojant pyuic)

├── README.md            # Šis dokumentas

**UI failas**

Grafinė vartotojo sąsaja (keliones.ui) buvo sukurta naudojant Qt Designer. Jei redaguosite keliones.ui, atnaujinkite keliones.py naudodami komandą:
```
pyuic6 keliones.ui -o keliones.py
```
**Licencija**

Šis projektas yra skirtas mokymuisi ir gali būti laisvai naudojamas nekomerciniais tikslais.
