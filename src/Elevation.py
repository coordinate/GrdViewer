# PyQt5 widgets import
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QAction, qApp, QDialog, QLineEdit, \
                            QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QFileDialog, QLabel, \
                            QGridLayout, QCheckBox

cstFElevation = 10

class Elevation(object):

    def __init__(self, fElevation=cstFElevation):
        self.fAngle = fElevation


class ElevDialog(QDialog):

    def __init__(self, parent=None):
        # Parent constructor
        super().__init__()

        self.earthPlt = parent.earthPlt

        # Add Title to the widget
        self.setWindowTitle('Add/Remove Elevation contour')
        self.setMinimumSize(100, 50)

        # Everything in a vertical Layout
        vboxElev = QVBoxLayout(self)

        # Add longitude field
        self.lblElev = QLabel('Elevation (deg)', parent=self)
        self.fldElev = QLineEdit('10', parent=self)
        hboxElev = QHBoxLayout(None)
        hboxElev.addWidget(self.lblElev)
        hboxElev.addStretch(1)
        hboxElev.addWidget(self.fldElev)
        vboxElev.addLayout(hboxElev)

        # Add Ok/Cancel buttons
        addButton = QPushButton('Add',self)
        remButton = QPushButton('Remove',self)
        cancelButton = QPushButton('Cancel',self)

        # Place Ok/Cancel button in an horizontal box layout
        hboxButton = QHBoxLayout()
        hboxButton.addStretch(1)
        hboxButton.addWidget(addButton)
        hboxButton.addWidget(remButton)
        hboxButton.addWidget(cancelButton)

        # put the button layout in the Vertical Layout
        vboxElev.addLayout(hboxButton)

        # set dialog box layout
        self.setLayout(vboxElev)

        # connect buttons to actions
        addButton.clicked.connect(self.addElevContour)
        remButton.clicked.connect(self.remElevContour)
        cancelButton.clicked.connect(self.close)

        # Dialog is modal to avoid reentry and weird behaviour
        self.setModal(True)
        self.show()
    # end of constructor

    def addElevContour(self):
        self.close()
        self.earthPlt.dicElev['Elev' + self.fldElev.text()] = Elevation(float(self.fldElev.text()))
        self.earthPlt.draw()

    def remElevContour(self):
        self.close()
        del self.earthPlt.dicElev['Elev' + self.fldElev.text()]
        self.earthPlt.draw()