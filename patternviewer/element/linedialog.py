"""This module implement a dialog widget to deal with line configuration.
"""

# Import third party modules
import sys

# PyQt5 widgets import
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, \
    QAction, qApp, QDialog, QLineEdit, QHBoxLayout, QVBoxLayout, \
    QPushButton, QWidget, QFileDialog, QLabel, QGridLayout, \
    QCheckBox, QComboBox
from PyQt5.QtGui import QColor, QPalette

# Import local modules
import patternviewer.utils as utils

import patternviewer.constant as cst


class LineDialog(QDialog):
    """This class implement a dialog widget to deal with line configuration.
    """

    def __init__(self, parent=None):
        """Constructor of the class LineDialog.
        parent is to line object to be configured using this dialog box
        """
        super().__init__()

        # parent is the object or list of object to modify
        self._parent = parent

        # dictionary containing the configuration of
        # the object to be configured
        self._config = {}

        self.initgui()
    # end of constructor

    def initgui(self):
        """Initialise GUI.
        """
        # get parent config
        config = self._parent.configure(None)

        # create this widget layout
        layout = QVBoxLayout(self)
        # add line parameters gui elements
        # linestyle
        linestylelayout = QHBoxLayout()
        labellinestyle = QLabel(self)
        labellinestyle.setText('linestyle')
        linestylelayout.addWidget(labellinestyle)
        self.combolinestyle = QComboBox(self)
        self.combolinestyle.addItems(['solid', 'dashed', 'dashdot', 'dotted',
                                      '-', '--', '-.', ':'])
        try:
            linestyles = config['linestyles']
        except KeyError:
            linestyles = 'solid'
        self.combolinestyle.setCurrentText(linestyles)
        linestylelayout.addWidget(self.combolinestyle)
        linestylelayout.addStretch(1)
        layout.addLayout(linestylelayout)
        # linewidth
        linewidthlayout = QHBoxLayout()
        labellinewidth = QLabel(self)
        labellinewidth.setText('linewidth')
        linewidthlayout.addWidget(labellinewidth)
        self.combolinewidth = QComboBox(self)
        self.combolinewidth.addItems(['no line', 'light',
                                      'medium', 'heavy'])
        try:
            linewidths = config['linewidths']
        except KeyError:
            linewidths = 'light'
        self.combolinewidth.setCurrentText(cst.getboldness(linewidths))
        linewidthlayout.addWidget(self.combolinewidth)
        linewidthlayout.addStretch(1)
        layout.addLayout(linewidthlayout)
        # label

        # add Apply/Ok/Cancel buttons
        buttonlayout = QHBoxLayout()
        applybutton = QPushButton('Apply', self)
        okbutton = QPushButton('Ok', self)
        cancelbutton = QPushButton('Cancel', self)
        buttonlayout.addStretch(1)
        buttonlayout.addWidget(applybutton)
        buttonlayout.addWidget(okbutton)
        buttonlayout.addWidget(cancelbutton)
        layout.addLayout(buttonlayout)

        # connect buttons to action
        applybutton.clicked.connect(self.config)
        okbutton.clicked.connect(self.configandclose)
        cancelbutton.clicked.connect(self.close)

    # end of method initGUI

    def config(self):
        """Collect value from widget and configure parent with
        the collected values.
        """
        # dictionary used to collect parameters
        conf = {}

        # get linewidth
        conf['linewidth'] = cst.BOLDNESS[self.combolinewidth.currentText()]
        conf['linewidths'] = cst.BOLDNESS[self.combolinewidth.currentText()]
        # get linestyle
        conf['linestyle'] = self.combolinestyle.currentText()
        conf['linestyles'] = self.combolinestyle.currentText()
        # call to parent configure method
        self._parent.configure(config=conf)
        self._parent.clearplot()
        if self._parent._plot is not None:
            self._parent.plot()
    # end of method config

    def configandclose(self):
        """Configure parent and close the widget.
        """
        self.config()
        self.close()
    # end of method configandclose

# Getters and Setters

    def get_parent(self):
        """Return this instance parent object.
        """
        return self._parent
    # end of function parent


# end of class LineDialog

# Main execution
if __name__ == '__main__':
    # Create main window
    MAIN_WINDOW = QApplication(sys.argv)
    APP = LineDialog()

    # Start main loop
    sys.exit(MAIN_WINDOW.exec_())

# end of module linedialog
