from PyQt5.QtCore import QThread, pyqtSignal
import requests
from bs4 import BeautifulSoup


class newTaskThread(QThread):
    success = pyqtSignal(int, str, str, str)
    error = pyqtSignal(int, str, str, str)

    def __init__(self, row_index, asin, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row_index = row_index
        self.asin = asin
    def run(self):
        self.success.emit(self.row_index, "xx", "xx", "xx")
        # self.error.emit(1, "xx", "xx", "xx")
        