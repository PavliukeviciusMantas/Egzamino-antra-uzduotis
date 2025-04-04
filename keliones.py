from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.labelVardas = QtWidgets.QLabel(parent=Form)
        self.labelVardas.setText("Vardas")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelVardas)
        self.vardasInput = QtWidgets.QLineEdit(parent=Form)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.vardasInput)

        self.labelPavarde = QtWidgets.QLabel(parent=Form)
        self.labelPavarde.setText("Pavardė")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelPavarde)
        self.pavardeInput = QtWidgets.QLineEdit(parent=Form)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pavardeInput)

        self.labelPastas = QtWidgets.QLabel(parent=Form)
        self.labelPastas.setText("El. paštas")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelPastas)
        self.pastasInput = QtWidgets.QLineEdit(parent=Form)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pastasInput)

        self.labelTelefonas = QtWidgets.QLabel(parent=Form)
        self.labelTelefonas.setText("Telefonas")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelTelefonas)
        self.telefonasInput = QtWidgets.QLineEdit(parent=Form)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.telefonasInput)

        self.labelIsvykimo = QtWidgets.QLabel(parent=Form)
        self.labelIsvykimo.setText("Išvykimo vieta")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelIsvykimo)
        self.isvykimoInput = QtWidgets.QLineEdit(parent=Form)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.isvykimoInput)

        self.labelAtvykimo = QtWidgets.QLabel(parent=Form)
        self.labelAtvykimo.setText("Atvykimo vieta")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelAtvykimo)
        self.atvykimoInput = QtWidgets.QLineEdit(parent=Form)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.atvykimoInput)

        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.pridetiButton = QtWidgets.QPushButton(parent=Form)
        self.pridetiButton.setText("Pridėti")
        self.buttonLayout.addWidget(self.pridetiButton)
        self.atnaujintiButton = QtWidgets.QPushButton(parent=Form)
        self.atnaujintiButton.setText("Atnaujinti")
        self.buttonLayout.addWidget(self.atnaujintiButton)
        self.salintiButton = QtWidgets.QPushButton(parent=Form)
        self.salintiButton.setText("Ištrinti")
        self.buttonLayout.addWidget(self.salintiButton)
        self.verticalLayout.addLayout(self.buttonLayout)

        self.kelionesTable = QtWidgets.QTableWidget(parent=Form)
        self.kelionesTable.setColumnCount(8)
        self.kelionesTable.setHorizontalHeaderLabels([
            "Vardas", "Pavardė", "El. paštas", "Telefonas",
            "Išvykimo vieta", "Atvykimo vieta", "Sukurta", "Atnaujinta"
        ])
        self.verticalLayout.addWidget(self.kelionesTable)

        QtCore.QMetaObject.connectSlotsByName(Form)