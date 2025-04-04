import sys
import sqlite3
import re
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PyQt6.QtCore import QDateTime
from keliones import Ui_Form

class KelioniuRegistratorius(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Kelionių Registratorius")

        self.conn = sqlite3.connect("keliones.db")
        self.create_table()

        # Įvykiai
        self.pridetiButton.clicked.connect(self.prideti_irasa)
        self.atnaujintiButton.clicked.connect(self.atnaujinti_irasa)
        self.salintiButton.clicked.connect(self.salinti_irasa)
        self.kelionesTable.cellClicked.connect(self.pasirinkti_irasa)

        self.uzkrauti_duomenis()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS keliones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vardas TEXT,
                pavarde TEXT,
                pastas TEXT,
                telefonas TEXT,
                isvykimo_vieta TEXT,
                atvykimo_vieta TEXT,
                sukurta TEXT,
                atnaujinta TEXT
            )
        ''')
        self.conn.commit()

    def validuoti_el_pasta(self, pastas):
        # Tikrina ar el. paštas yra teisingo formato su bet kokiu TLD
        return re.match(r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$", pastas)

    def validuoti_telefono_numeri(self, telefonas):
        return re.match(r"^\+370\d{8}$", telefonas)

    def prideti_irasa(self):
        data = [
            self.vardasInput.text(),
            self.pavardeInput.text(),
            self.pastasInput.text(),
            self.telefonasInput.text(),
            self.isvykimoInput.text(),
            self.atvykimoInput.text()
        ]

        if any(x == "" for x in data):
            QMessageBox.warning(self, "Klaida", "Prašome užpildyti visus laukus.")
            return

        if not self.validuoti_el_pasta(data[2]):
            QMessageBox.warning(self, "Klaida", "Neteisingas el. pašto formatas. Įsitikinkite, kad adresas turi '@' ir galiojantį domeną.")
            return

        if not self.validuoti_telefono_numeri(data[3]):
            QMessageBox.warning(self, "Klaida", "Neteisingas telefono numerio formatas. Turi prasidėti +370 ir turėti 8 skaitmenis po to.")
            return

        dabar = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO keliones (vardas, pavarde, pastas, telefonas, isvykimo_vieta, atvykimo_vieta, sukurta, atnaujinta)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (*data, dabar, dabar))
        self.conn.commit()
        self.uzkrauti_duomenis()
        self.valyti_laukus()

    def uzkrauti_duomenis(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM keliones")
        irasai = cursor.fetchall()
        self.kelionesTable.setRowCount(0)
        for eilute in irasai:
            row_position = self.kelionesTable.rowCount()
            self.kelionesTable.insertRow(row_position)
            for i in range(1, 9):
                self.kelionesTable.setItem(row_position, i - 1, QTableWidgetItem(str(eilute[i])))

    def pasirinkti_irasa(self, row, column):
        self.vardasInput.setText(self.kelionesTable.item(row, 0).text())
        self.pavardeInput.setText(self.kelionesTable.item(row, 1).text())
        self.pastasInput.setText(self.kelionesTable.item(row, 2).text())
        self.telefonasInput.setText(self.kelionesTable.item(row, 3).text())
        self.isvykimoInput.setText(self.kelionesTable.item(row, 4).text())
        self.atvykimoInput.setText(self.kelionesTable.item(row, 5).text())
        self.selected_id = self.gauti_id_pagal_eilute(row)

    def gauti_id_pagal_eilute(self, row):
        cursor = self.conn.cursor()
        vardas = self.kelionesTable.item(row, 0).text()
        pavarde = self.kelionesTable.item(row, 1).text()
        cursor.execute("SELECT id FROM keliones WHERE vardas=? AND pavarde=?", (vardas, pavarde))
        result = cursor.fetchone()
        return result[0] if result else None

    def atnaujinti_irasa(self):
        if not hasattr(self, 'selected_id'):
            QMessageBox.warning(self, "Klaida", "Nepasirinktas įrašas.")
            return

        data = [
            self.vardasInput.text(),
            self.pavardeInput.text(),
            self.pastasInput.text(),
            self.telefonasInput.text(),
            self.isvykimoInput.text(),
            self.atvykimoInput.text()
        ]

        if not self.validuoti_el_pasta(data[2]):
            QMessageBox.warning(self, "Klaida", "Neteisingas el. pašto formatas. Įsitikinkite, kad adresas turi '@' ir galiojantį domeną.")
            return

        if not self.validuoti_telefono_numeri(data[3]):
            QMessageBox.warning(self, "Klaida", "Neteisingas telefono numerio formatas. Turi prasidėti +370 ir turėti 8 skaitmenis po to.")
            return

        dabar = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")

        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE keliones
            SET vardas=?, pavarde=?, pastas=?, telefonas=?, isvykimo_vieta=?, atvykimo_vieta=?, atnaujinta=?
            WHERE id=?
        """, (*data, dabar, self.selected_id))
        self.conn.commit()
        self.uzkrauti_duomenis()
        self.valyti_laukus()

    def salinti_irasa(self):
        if not hasattr(self, 'selected_id'):
            QMessageBox.warning(self, "Klaida", "Nepasirinktas įrašas.")
            return
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM keliones WHERE id=?", (self.selected_id,))
        self.conn.commit()
        self.uzkrauti_duomenis()
        self.valyti_laukus()

    def valyti_laukus(self):
        self.vardasInput.clear()
        self.pavardeInput.clear()
        self.pastasInput.clear()
        self.telefonasInput.clear()
        self.isvykimoInput.clear()
        self.atvykimoInput.clear()
        if hasattr(self, 'selected_id'):
            del self.selected_id

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KelioniuRegistratorius()
    window.show()
    sys.exit(app.exec())
