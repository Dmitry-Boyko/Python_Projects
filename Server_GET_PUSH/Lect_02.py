#__author__ = 'dmitryboyko'

from PySide.QtCore import *
from PySide.QtGui import *

import sys
import time

app = QApplication(sys.argv)

due = QTime.curentTime()
message = 'Alert'

try:

    if len(sys.argv)<2:
        raise ValueError




except:
    pass