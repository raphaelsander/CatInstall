# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os
import json

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui(object):
    def setupUi(self, MainWindow):

        # Janela principal
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))

        # Ícone do software
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/home/blackcat/Projects/CatInstall/ui/icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        # Widget Central
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.button_about = QtGui.QPushButton(self.centralwidget)
        self.button_about.setEnabled(True)
        self.button_about.setGeometry(QtCore.QRect(541, 420, 91, 28))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_about.sizePolicy().hasHeightForWidth())

        # Button about
        self.button_about.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("gnome-about-logo"))
        self.button_about.setIcon(icon)
        self.button_about.setObjectName(_fromUtf8("button_about"))

        # Widget category
        self.widget_category = QtGui.QWidget(self.centralwidget)
        self.widget_category.setEnabled(True)
        self.widget_category.setGeometry(QtCore.QRect(0, 10, 641, 441))
        self.widget_category.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.widget_category.setAcceptDrops(False)
        self.widget_category.setAutoFillBackground(True)
        self.widget_category.setObjectName(_fromUtf8("widget_category"))

        # Button theme
        self.button_theme = QtGui.QPushButton(self.widget_category)
        self.button_theme.setGeometry(QtCore.QRect(220, 100, 200, 56))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("theme-config"))
        self.button_theme.setIcon(icon)
        self.button_theme.setIconSize(QtCore.QSize(48, 48))
        self.button_theme.setObjectName(_fromUtf8("button_theme"))

        # Button icon
        self.button_icon = QtGui.QPushButton(self.widget_category)
        self.button_icon.setGeometry(QtCore.QRect(430, 100, 200, 56))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("icon"))
        self.button_icon.setIcon(icon)
        self.button_icon.setIconSize(QtCore.QSize(48, 48))
        self.button_icon.setObjectName(_fromUtf8("button_icon"))

        # Button cursor
        self.button_cursor = QtGui.QPushButton(self.widget_category)
        self.button_cursor.setGeometry(QtCore.QRect(220, 190, 200, 56))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("mouse"))
        self.button_cursor.setIcon(icon)
        self.button_cursor.setIconSize(QtCore.QSize(48, 48))
        self.button_cursor.setObjectName(_fromUtf8("button_cursor"))

        # Button font
        self.button_font = QtGui.QPushButton(self.widget_category)
        self.button_font.setGeometry(QtCore.QRect(430, 190, 200, 56))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("fonts"))
        self.button_font.setIcon(icon)
        self.button_font.setIconSize(QtCore.QSize(48, 48))
        self.button_font.setObjectName(_fromUtf8("button_font"))

        # Button conky
        self.button_conky = QtGui.QPushButton(self.widget_category)
        self.button_conky.setGeometry(QtCore.QRect(10, 190, 200, 56))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("conky"))
        self.button_conky.setIcon(icon)
        self.button_conky.setIconSize(QtCore.QSize(48, 48))
        self.button_conky.setObjectName(_fromUtf8("button_conky"))

        # Button app
        self.button_app = QtGui.QPushButton(self.widget_category)
        self.button_app.setGeometry(QtCore.QRect(10, 100, 200, 56))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("software"))
        self.button_app.setIcon(icon)
        self.button_app.setIconSize(QtCore.QSize(48, 48))
        self.button_app.setObjectName(_fromUtf8("button_app"))

        # Linha horizontal
        self.line = QtGui.QFrame(self.widget_category)
        self.line.setGeometry(QtCore.QRect(20, 270, 601, 20))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        # ListView para aplicativos
        self.listView_app = QtGui.QListWidget(self.centralwidget)
        self.listView_app.setGeometry(QtCore.QRect(10, 90, 621, 321))
        self.listView_app.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listView_app.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.listView_app.setInputMethodHints(QtCore.Qt.ImhNone)
        self.listView_app.setFrameShape(QtGui.QFrame.StyledPanel)
        self.listView_app.setFrameShadow(QtGui.QFrame.Sunken)
        self.listView_app.setEditTriggers(QtGui.QAbstractItemView.EditKeyPressed)
        self.listView_app.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.listView_app.setObjectName(_fromUtf8("listView_app"))

        try:
            changelog = open(os.path.expanduser("~/.local/share/CatInstall/CHANGELOG"), 'r')
            data_changelog = json.load(changelog)
        except IOError:
            print("Arquivo de CHANGELOG não existe. É necessário internet!!!! :)")

        for category in data_changelog:
            # Carregando o arquivo de CHANGELOG e transformando os scripts em objetos
            for script in data_changelog['%s' % category]:
                name = data_changelog[category][script]['name']
                #patch = os.path.expanduser("~/.local/share/CatInstall") + data_changelog[category][script]['patch']

                self.gridLayoutWidget = QtGui.QWidget(self.listView_app)
                self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 621, 31))
                self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
                self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
                self.gridLayout.setSpacing(0)
                self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

                self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
                self.pushButton.setEnabled(True)
                sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
                self.pushButton.setSizePolicy(sizePolicy)
                self.pushButton.setMaximumSize(QtCore.QSize(85, 50))
                icon = QtGui.QIcon.fromTheme(_fromUtf8("exec"))
                self.pushButton.setIcon(icon)
                self.pushButton.setIconSize(QtCore.QSize(20, 20))
                self.pushButton.setObjectName(_fromUtf8("pushButton"))
                self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

                self.label = QtGui.QLabel(self.gridLayoutWidget)
                self.label.setObjectName(_fromUtf8("%s" %name))
                self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

                print(name)

                item = QtGui.QListWidgetItem(self.gridLayout)
                self.listView_app.addItem(iten)

        # Campo search
        self.lineEdit_search = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_search.setGeometry(QtCore.QRect(392, 40, 241, 30))
        self.lineEdit_search.setInputMask(_fromUtf8(""))
        self.lineEdit_search.setText(_fromUtf8(""))
        self.lineEdit_search.setMaxLength(32767)
        self.lineEdit_search.setObjectName(_fromUtf8("lineEdit_search"))

        # Label pesquisar
        self.label_search = QtGui.QLabel(self.centralwidget)
        self.label_search.setGeometry(QtCore.QRect(320, 40, 62, 31))
        self.label_search.setObjectName(_fromUtf8("label_search"))

        # Logo CatInstall
        self.label_logo = QtGui.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(10, 20, 231, 61))
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setPixmap(QtGui.QPixmap(_fromUtf8("/home/blackcat/Projects/CatInstall/ui/logo.png")))
        self.label_logo.setObjectName(_fromUtf8("label_logo"))

        # Button início
        self.button_home = QtGui.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(10, 420, 90, 28))
        self.button_home.setObjectName(_fromUtf8("button_home"))
        self.button_home.raise_()

        #####
        self.label_search.raise_()
        self.lineEdit_search.raise_()
        self.listView_app.raise_()
        self.widget_category.raise_()
        self.button_about.raise_()
        self.label_logo.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QObject.connect(self.button_app, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget_category.hide)
        QtCore.QObject.connect(self.button_theme, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget_category.hide)
        QtCore.QObject.connect(self.button_icon, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget_category.hide)
        QtCore.QObject.connect(self.button_conky, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget_category.hide)
        QtCore.QObject.connect(self.button_cursor, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget_category.hide)
        QtCore.QObject.connect(self.button_font, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget_category.hide)
        QtCore.QObject.connect(self.button_home, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget_category.show)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "CatInstall 1.4", None))

        self.button_about.setText(_translate("MainWindow", "Sobre", None))
        self.button_theme.setText(_translate("MainWindow", "Temas", None))
        self.button_icon.setText(_translate("MainWindow", "Ícones", None))
        self.button_cursor.setText(_translate("MainWindow", "Cursor", None))
        self.button_font.setText(_translate("MainWindow", "Fontes", None))
        self.button_conky.setText(_translate("MainWindow", "Conky", None))
        self.button_app.setText(_translate("MainWindow", "Aplicativos", None))
        self.label_search.setText(_translate("MainWindow", "Pesquisar:", None))
        self.button_home.setText(_translate("MainWindow", "Início", None))