import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        back_btn = QAction(QIcon('icons/back.png'), 'Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        forward_btn = QAction(QIcon('icons/ford.png'), 'Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        navbar = QToolBar()
        self.addToolBar(navbar)
        self.setWindowIcon(QIcon('icons/tufway.png'))
        self.showMaximized()
        reload_btn = QAction(QIcon('icons/reload.png'), 'Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        home_btn = QAction(QIcon('icons/home'), 'Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_urlbar)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_urlbar(self, q):
        self.url_bar.setText(q.toString())

# run the browser
app = QApplication(sys.argv)
QApplication.setApplicationName('TuflerWave')
window = MainWindow()
app.exec_()