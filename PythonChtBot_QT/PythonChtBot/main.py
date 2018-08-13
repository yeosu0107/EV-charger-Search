import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Intro import *


if __name__=="__main__":
    app=QApplication(sys.argv)
    EvChargingsystem_Intro_UI=InputCity();
    EvChargingsystem_Intro_UI.show();
    app.exec_()
