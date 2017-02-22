# -*- coding: utf-8 -*-

# Created by: PyQt4 UI code generator 4.11.4

from PyQt4 import QtCore, QtGui
import os

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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(os.getcwd() + "/ui/icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(56, 56, 56);"))
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)


        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))


        self.button_about = QtGui.QPushButton(self.centralwidget)
        self.button_about.setGeometry(QtCore.QRect(541, 420, 91, 28))
        self.button_about.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_about.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n""font: 63 11pt \"Ubuntu\";\n""border-radius: 5px;\n""color: rgb(0, 0, 0);"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("gnome-about-logo"))
        self.button_about.setIcon(icon)
        self.button_about.setObjectName(_fromUtf8("button_about"))


        self.widget_category = QtGui.QWidget(self.centralwidget)
        self.widget_category.setEnabled(True)
        self.widget_category.setGeometry(QtCore.QRect(0, 10, 641, 441))
        self.widget_category.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.widget_category.setAcceptDrops(False)
        self.widget_category.setAutoFillBackground(False)
        self.widget_category.setObjectName(_fromUtf8("widget_category"))


        self.button_theme = QtGui.QPushButton(self.widget_category)
        self.button_theme.setGeometry(QtCore.QRect(220, 100, 200, 56))
        self.button_theme.setStyleSheet(_fromUtf8("background-color: rgb(170, 85, 0);\n""font: 75 16pt \"Arial\";\n""border-radius: 5px;\n""color: rgb(255, 255, 255);"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("theme-config"))
        self.button_theme.setIcon(icon)
        self.button_theme.setIconSize(QtCore.QSize(48, 48))
        self.button_theme.setObjectName(_fromUtf8("button_theme"))


        self.button_icon = QtGui.QPushButton(self.widget_category)
        self.button_icon.setGeometry(QtCore.QRect(430, 100, 200, 56))
        self.button_icon.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 0);\n""font: 75 16pt \"Arial\";\n""border-radius: 5px;\n""color: rgb(255, 255, 255);"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("icon"))
        self.button_icon.setIcon(icon)
        self.button_icon.setIconSize(QtCore.QSize(48, 48))
        self.button_icon.setObjectName(_fromUtf8("button_icon"))


        self.button_cursor = QtGui.QPushButton(self.widget_category)
        self.button_cursor.setGeometry(QtCore.QRect(220, 190, 200, 56))
        self.button_cursor.setStyleSheet(_fromUtf8("background-color: rgb(85, 0, 127);\n""font: 75 16pt \"Arial\";\n""border-radius: 5px;\n""color: rgb(255, 255, 255);"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("mouse"))
        self.button_cursor.setIcon(icon)
        self.button_cursor.setIconSize(QtCore.QSize(48, 48))
        self.button_cursor.setObjectName(_fromUtf8("button_cursor"))


        self.button_font = QtGui.QPushButton(self.widget_category)
        self.button_font.setGeometry(QtCore.QRect(430, 190, 200, 56))
        self.button_font.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n""font: 75 16pt \"Arial\";\n""border-radius: 5px;\n""color: rgb(255, 255, 255);"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("fonts"))
        self.button_font.setIcon(icon)
        self.button_font.setIconSize(QtCore.QSize(48, 48))
        self.button_font.setObjectName(_fromUtf8("button_font"))


        self.button_conky = QtGui.QPushButton(self.widget_category)
        self.button_conky.setGeometry(QtCore.QRect(10, 190, 200, 56))
        self.button_conky.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 0);\n""font: 75 16pt \"Arial\";\n""border-radius: 5px;\n""color: rgb(255, 255, 255);"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("conky"))
        self.button_conky.setIcon(icon)
        self.button_conky.setIconSize(QtCore.QSize(48, 48))
        self.button_conky.setObjectName(_fromUtf8("button_conky"))


        self.button_app = QtGui.QPushButton(self.widget_category)
        self.button_app.setGeometry(QtCore.QRect(10, 100, 200, 56))
        self.button_app.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 255);\n""font: 75 16pt \"Arial\";\n""border-radius: 5px;\n""color: rgb(255, 255, 255);"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("software"))
        self.button_app.setIcon(icon)
        self.button_app.setIconSize(QtCore.QSize(48, 48))
        self.button_app.setObjectName(_fromUtf8("button_app"))


        self.line = QtGui.QFrame(self.widget_category)
        self.line.setGeometry(QtCore.QRect(20, 260, 601, 20))
        self.line.setStyleSheet(_fromUtf8(""))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))


        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 621, 331))
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        #self.tableWidget.setRowCount(20)


        self.lineEdit_search = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_search.setGeometry(QtCore.QRect(402, 40, 231, 30))
        self.lineEdit_search.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_search.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\nselection-color: rgb(255, 255, 255);"))
        self.lineEdit_search.setInputMask(_fromUtf8(""))
        self.lineEdit_search.setText(_fromUtf8(""))
        self.lineEdit_search.setMaxLength(32767)
        self.lineEdit_search.setObjectName(_fromUtf8("lineEdit_search"))


        self.label_search = QtGui.QLabel(self.centralwidget)
        self.label_search.setGeometry(QtCore.QRect(320, 40, 71, 31))
        self.label_search.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_search.setObjectName(_fromUtf8("label_search"))


        self.label_logo = QtGui.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 231, 61))
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setPixmap(QtGui.QPixmap(_fromUtf8(os.getcwd() + "/ui/logo.png")))
        self.label_logo.setObjectName(_fromUtf8("label_logo"))


        self.frame_about = QtGui.QFrame(self.centralwidget)
        self.frame_about.setGeometry(QtCore.QRect(120, 90, 411, 312))
        self.frame_about.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.frame_about.setStyleSheet(_fromUtf8(""))
        self.frame_about.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_about.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_about.setObjectName(_fromUtf8("frame_about"))


        self.label_logo_about = QtGui.QLabel(self.frame_about)
        self.label_logo_about.setGeometry(QtCore.QRect(90, 20, 231, 61))
        self.label_logo_about.setText(_fromUtf8(""))
        self.label_logo_about.setPixmap(QtGui.QPixmap(_fromUtf8(os.getcwd() + "/ui/logo.png")))
        self.label_logo_about.setObjectName(_fromUtf8("label_logo_about"))


        self.text_about = QtGui.QTextBrowser(self.frame_about)
        self.text_about.setGeometry(QtCore.QRect(10, 91, 391, 211))
        self.text_about.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.text_about.setObjectName(_fromUtf8("text_about"))


        self.close_about = QtGui.QPushButton(self.frame_about)
        self.close_about.setGeometry(QtCore.QRect(380, 10, 21, 21))
        self.close_about.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);\n""color: rgb(255, 255, 255);\n""font: 75 12pt \"Arial\";\n""border-radius: 10px;"))
        self.close_about.setObjectName(_fromUtf8("close_about"))


        self.button_home = QtGui.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(10, 420, 90, 28))
        self.button_home.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_home.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n""font: 63 11pt \"Ubuntu\";\n""border-radius: 5px;\n""color: rgb(0, 0, 0);"))
        self.button_home.setObjectName(_fromUtf8("button_home"))


        self.frame_about.raise_()
        self.label_search.raise_()
        self.lineEdit_search.raise_()
        self.tableWidget.raise_()
        self.button_home.raise_()
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
        QtCore.QObject.connect(self.button_about, QtCore.SIGNAL(_fromUtf8("clicked()")), self.frame_about.raise_)
        QtCore.QObject.connect(self.close_about, QtCore.SIGNAL(_fromUtf8("clicked()")), self.frame_about.lower)
        QtCore.QObject.connect(self.button_home, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget_category.show)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add(self, name, patch):
        print(name, patch)
        #rowz = self.tableWidget.rowCount()
        self.tableWidget.insertRow()

        # button in column 0
        button = QtGui.QPushButton(name)
        button.setProperty("name", name)
        button.clicked.connect(self.tableWidget.on_click)
        self.tableWidget.setCellWidget(row, 0, button)

        # text in column 1
        self.tableWidget.setItem(rowz, 1, QtGui.QTableWidgetItem(name))

    def on_click(self):
        # find the item with the same name to get the row
        print("Button click")

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
        self.text_about.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#000000;\">CatInstall 1.4</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Desenvolvedor:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Raphael Sander &lt;</span><span style=\" text-decoration: underline; color:#0000ff;\">raphael.sander75@gmail.com</span></a><span style=\" color:#000000;\">&gt;</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Colaboradores:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Cainã D\'Ajuda</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Reni Alkimim Dantas</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Github: </span><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/raphaelsander/CatInstall</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Site: </span><span style=\" text-decoration: underline; color:#0000ff;\">http://blackcat8080.xyz/catinstall</span></a></p></body></html>", None))
        self.close_about.setText(_translate("MainWindow", "X", None))
        self.button_home.setText(_translate("MainWindow", "Início", None))
