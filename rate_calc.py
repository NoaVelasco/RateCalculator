# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora_tarifasIynNOc.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize,
                            QLocale, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout,
                               QLabel, QMainWindow, QRadioButton, QSizePolicy,
                               QSlider, QSpacerItem, QSpinBox, QTabWidget,
                               QWidget, QPushButton, QToolButton, QFileDialog,
                               QMessageBox, QCheckBox)
import qtawesome as qta
from math import ceil
from time import localtime
import sys


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # MainWindow.resize(691, 391)
        MainWindow.setFixedSize(690, 390)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(20, 80, 80);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 691, 391))
        font = QFont()
        font.setFamilies([u"Bookerly"])
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"background-color: rgb(0, 139, 139);\n"
                                     "")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_corr = QWidget()
        self.tab_corr.setObjectName(u"tab_corr")
        sizePolicy.setHeightForWidth(
            self.tab_corr.sizePolicy().hasHeightForWidth())
        self.tab_corr.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Bookerly"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.tab_corr.setFont(font1)
        self.tab_corr.setStyleSheet(u"font: 9pt \"Bookerly\";\n"
                                    "color: \"white\";")
        self.label_8 = QLabel(self.tab_corr)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 40, 401, 31))
        self.label_8.setStyleSheet(u"font: 20pt \"Bookerly\";")
        self.layoutWidget = QWidget(self.tab_corr)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 130, 551, 163))
        self.gridLayout_corr = QGridLayout(self.layoutWidget)
        self.gridLayout_corr.setObjectName(u"gridLayout_corr")
        self.gridLayout_corr.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                   | Qt.AlignVCenter)

        self.gridLayout_corr.addWidget(self.label_15, 6, 5, 1, 1)

        self.lbl_pags = QLabel(self.layoutWidget)
        self.lbl_pags.setObjectName(u"lbl_pags")
        self.lbl_pags.setStyleSheet(u"background-color: #006666;\n"
                                    "color: \"white\";\n"
                                    "font: 10pt \"Cascadia Code\";")
        self.lbl_pags.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                   | Qt.AlignVCenter)
        self.lbl_pags.setIndent(5)

        self.gridLayout_corr.addWidget(self.lbl_pags, 2, 7, 1, 1)

        self.radioBtn_sty = QRadioButton(self.layoutWidget)
        self.radioBtn_sty.setObjectName(u"radioBtn_sty")

        self.gridLayout_corr.addWidget(self.radioBtn_sty, 7, 4, 1, 1)

        self.slider_compl = QSlider(self.layoutWidget)
        self.slider_compl.setObjectName(u"slider_compl")
        self.slider_compl.setStyleSheet(u"")
        self.slider_compl.setMinimum(1)
        self.slider_compl.setMaximum(5)
        self.slider_compl.setPageStep(2)
        self.slider_compl.setValue(3)
        self.slider_compl.setOrientation(Qt.Horizontal)

        self.gridLayout_corr.addWidget(self.slider_compl, 3, 2, 1, 1)

        self.lbl_show_full = QLabel(self.layoutWidget)
        self.lbl_show_full.setObjectName(u"lbl_show_full")
        self.lbl_show_full.setStyleSheet(u"background-color: #006666;\n"
                                         "color: \"white\";\n"
                                         "font: 10pt \"Cascadia Code\";")
        self.lbl_show_full.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                        | Qt.AlignVCenter)
        self.lbl_show_full.setIndent(5)

        self.gridLayout_corr.addWidget(self.lbl_show_full, 9, 2, 1, 1)

        self.radioBtn_full = QRadioButton(self.layoutWidget)
        self.radioBtn_full.setObjectName(u"radioBtn_full")

        self.gridLayout_corr.addWidget(self.radioBtn_full, 9, 4, 1, 1)

        self.lbl_iva = QLabel(self.layoutWidget)
        self.lbl_iva.setObjectName(u"lbl_iva")
        self.lbl_iva.setStyleSheet(u"background-color: #006666;\n"
                                   "color: \"white\";\n"
                                   "font: 10pt \"Cascadia Code\";")
        self.lbl_iva.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                  | Qt.AlignVCenter)
        self.lbl_iva.setIndent(5)

        self.gridLayout_corr.addWidget(self.lbl_iva, 7, 7, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLineWidth(-1)
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(True)

        self.gridLayout_corr.addWidget(self.label_9, 2, 0, 1, 1)

        self.radioBtn_orto = QRadioButton(self.layoutWidget)
        self.radioBtn_orto.setObjectName(u"radioBtn_orto")

        self.gridLayout_corr.addWidget(self.radioBtn_orto, 6, 4, 1, 1)

        self.lbl_irpf = QLabel(self.layoutWidget)
        self.lbl_irpf.setObjectName(u"lbl_irpf")
        self.lbl_irpf.setStyleSheet(u"background-color: #006666;\n"
                                    "color: \"white\";\n"
                                    "font: 10pt \"Cascadia Code\";")
        self.lbl_irpf.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                   | Qt.AlignVCenter)
        self.lbl_irpf.setIndent(5)

        self.gridLayout_corr.addWidget(self.lbl_irpf, 6, 7, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_corr.addWidget(self.label_3, 9, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_corr.addWidget(self.label_4, 0, 0, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_corr.addWidget(self.label, 6, 0, 1, 1)

        self.lbl_show_orto = QLabel(self.layoutWidget)
        self.lbl_show_orto.setObjectName(u"lbl_show_orto")
        self.lbl_show_orto.setStyleSheet(u"background-color: #006666;\n"
                                         "color: \"white\";\n"
                                         "font: 10pt \"Cascadia Code\";")
        self.lbl_show_orto.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                        | Qt.AlignVCenter)
        self.lbl_show_orto.setMargin(0)
        self.lbl_show_orto.setIndent(5)

        self.gridLayout_corr.addWidget(self.lbl_show_orto, 6, 2, 1, 1)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                   | Qt.AlignVCenter)

        self.gridLayout_corr.addWidget(self.label_17, 9, 5, 1, 1)

        self.spinBox_matr = QSpinBox(self.layoutWidget)
        self.spinBox_matr.setObjectName(u"spinBox_matr")
        font2 = QFont()
        font2.setFamilies([u"Cascadia Code"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.spinBox_matr.setFont(font2)
        self.spinBox_matr.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_matr.setAutoFillBackground(False)
        self.spinBox_matr.setStyleSheet(u"background-color: #006666;\n"
                                        "color: \"white\";\n"
                                        "font: 10pt \"Cascadia Code\";\n"
                                        "")
        self.spinBox_matr.setWrapping(False)
        self.spinBox_matr.setFrame(True)
        self.spinBox_matr.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                       | Qt.AlignVCenter)
        self.spinBox_matr.setProperty("showGroupSeparator", True)
        self.spinBox_matr.setMinimum(0)
        self.spinBox_matr.setMaximum(10000000)
        self.spinBox_matr.setSingleStep(1000)
        self.spinBox_matr.setValue(0)

        self.gridLayout_corr.addWidget(self.spinBox_matr, 0, 2, 1, 1)

        self.lbl_base = QLabel(self.layoutWidget)
        self.lbl_base.setObjectName(u"lbl_base")
        self.lbl_base.setStyleSheet(u"background-color: #006666;\n"
                                    "color: \"white\";\n"
                                    "font: 10pt \"Cascadia Code\";")
        self.lbl_base.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                   | Qt.AlignVCenter)
        self.lbl_base.setIndent(5)

        self.gridLayout_corr.addWidget(self.lbl_base, 4, 7, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                            QSizePolicy.Minimum)

        self.gridLayout_corr.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed,
                                              QSizePolicy.Minimum)

        self.gridLayout_corr.addItem(self.horizontalSpacer_4, 0, 6, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                  | Qt.AlignVCenter)

        self.gridLayout_corr.addWidget(self.label_7, 2, 5, 1, 1)

        self.lbl_palab = QLabel(self.layoutWidget)
        self.lbl_palab.setObjectName(u"lbl_palab")
        self.lbl_palab.setStyleSheet(u"background-color: #006666;\n"
                                     "color: \"white\";\n"
                                     "font: 10pt \"Cascadia Code\";")
        self.lbl_palab.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                    | Qt.AlignVCenter)
        self.lbl_palab.setIndent(5)

        self.gridLayout_corr.addWidget(self.lbl_palab, 0, 7, 1, 1)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                   | Qt.AlignVCenter)

        self.gridLayout_corr.addWidget(self.label_16, 7, 5, 1, 1)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"font: 10pt \"Cascadia Code\";")

        self.gridLayout_corr.addWidget(self.label_13, 2, 3, 1, 1)

        self.lbl_show_sty = QLabel(self.layoutWidget)
        self.lbl_show_sty.setObjectName(u"lbl_show_sty")
        self.lbl_show_sty.setStyleSheet(u"background-color: #006666;\n"
                                        "color: \"white\";\n"
                                        "font: 10pt \"Cascadia Code\";")
        self.lbl_show_sty.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                       | Qt.AlignVCenter)
        self.lbl_show_sty.setIndent(5)

        self.gridLayout_corr.addWidget(self.lbl_show_sty, 7, 2, 1, 1)

        self.lbl_total = QLabel(self.layoutWidget)
        self.lbl_total.setObjectName(u"lbl_total")
        self.lbl_total.setStyleSheet(u"background-color: #006666;\n"
                                     "color: \"white\";\n"
                                     "font: 10pt \"Cascadia Code\";")
        self.lbl_total.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                    | Qt.AlignVCenter)
        self.lbl_total.setIndent(5)

        self.gridLayout_corr.addWidget(self.lbl_total, 9, 7, 1, 1)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                   | Qt.AlignVCenter)

        self.gridLayout_corr.addWidget(self.label_14, 4, 5, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_corr.addWidget(self.label_2, 7, 0, 1, 1)

        self.spinBox_percen = QDoubleSpinBox(self.layoutWidget)
        self.spinBox_percen.setObjectName(u"spinBox_percen")
        self.spinBox_percen.setLocale(
            QLocale(QLocale.English, QLocale.UnitedStates))
        self.spinBox_percen.setFont(font2)
        self.spinBox_percen.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_percen.setAutoFillBackground(False)
        self.spinBox_percen.setStyleSheet(u"background-color: #006666;\n"
                                          "color: \"white\";\n"
                                          "font: 10pt \"Cascadia Code\";\n"
                                          "")
        self.spinBox_percen.setWrapping(False)
        self.spinBox_percen.setFrame(True)
        self.spinBox_percen.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                         | Qt.AlignVCenter)
        self.spinBox_percen.setProperty("showGroupSeparator", True)
        self.spinBox_percen.setDecimals(2)
        self.spinBox_percen.setMinimum(-50.000000000000000)

        self.gridLayout_corr.addWidget(self.spinBox_percen, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed,
                                              QSizePolicy.Minimum)

        self.gridLayout_corr.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"font: 10pt \"Cascadia Code\";")

        self.gridLayout_corr.addWidget(self.label_11, 7, 3, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"font: 10pt \"Cascadia Code\";")

        self.gridLayout_corr.addWidget(self.label_12, 9, 3, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_corr.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                  | Qt.AlignVCenter)

        self.gridLayout_corr.addWidget(self.label_6, 0, 5, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"font: 10pt \"Cascadia Code\";")

        self.gridLayout_corr.addWidget(self.label_10, 6, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                              QSizePolicy.Minimum)

        self.gridLayout_corr.addItem(self.horizontalSpacer_3, 3, 7, 1, 1)

        icon = qta.icon('ph.info-fill', color=('DarkSlateGray'))
        self.psBtnSave = QPushButton(self.tab_corr)
        self.psBtnSave.setObjectName(u"psBtnSave")
        self.psBtnSave.setGeometry(QRect(480, 320, 121, 31))
        self.btn_about = QToolButton(self.tab_corr)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setGeometry(QRect(440, 320, 31, 31))
        # icon = QIcon(QIcon.fromTheme(u"system-help"))
        self.btn_about.setIcon(icon)
        self.btn_about.setIconSize(QSize(28, 28))

        self.tabWidget.addTab(self.tab_corr, "")

        # -------------- TAB INFORM --------------------

        self.tab_inf = QWidget()
        self.tab_inf.setObjectName(u"tab_inf")
        self.tab_inf.setStyleSheet(u"font: 9pt \"Bookerly\";\n"
                                   "color: \"white\";")
        self.label_18 = QLabel(self.tab_inf)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 40, 401, 31))
        self.label_18.setStyleSheet(
            u"font: 20pt \"Bookerly\"; color: 'white';")
        self.label_20 = QLabel(self.tab_inf)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(70, 120, 131, 41))
        self.label_23 = QLabel(self.tab_inf)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(70, 180, 141, 21))
        self.checkBox_GA = QCheckBox(self.tab_inf)
        self.checkBox_GA.setObjectName(u"checkBox_GA")
        self.checkBox_GA.setGeometry(QRect(50, 210, 141, 20))
        self.checkBox_MR = QCheckBox(self.tab_inf)
        self.checkBox_MR.setObjectName(u"checkBox_MR")
        self.checkBox_MR.setGeometry(QRect(50, 240, 141, 20))
        self.spinBox_inf_pal = QSpinBox(self.tab_inf)
        self.spinBox_inf_pal.setObjectName(u"spinBox_inf_pal")
        self.spinBox_inf_pal.setGeometry(QRect(220, 130, 111, 22))
        self.spinBox_inf_pal.setStyleSheet(u"background-color: #006666;\n"
                                           "color: \"white\";\n"
                                           "font: 10pt \"Cascadia Code\";\n"
                                           "")
        self.spinBox_inf_pal.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                          | Qt.AlignVCenter)
        self.spinBox_inf_pal.setMinimum(0)
        self.spinBox_inf_pal.setMaximum(1000000)
        self.spinBox_inf_pal.setSingleStep(1000)
        self.lbl_show_infBase = QLabel(self.tab_inf)
        self.lbl_show_infBase.setObjectName(u"lbl_show_infBase")
        self.lbl_show_infBase.setGeometry(QRect(220, 180, 92, 16))
        self.lbl_show_infBase.setStyleSheet(u"background-color: #006666;\n"
                                            "color: \"white\";\n"
                                            "font: 10pt \"Cascadia Code\";")
        self.lbl_show_infBase.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                           | Qt.AlignVCenter)
        self.lbl_show_infBase.setMargin(0)
        self.lbl_show_infBase.setIndent(5)
        self.lbl_show_infGA = QLabel(self.tab_inf)
        self.lbl_show_infGA.setObjectName(u"lbl_show_infGA")
        self.lbl_show_infGA.setGeometry(QRect(220, 210, 92, 16))
        self.lbl_show_infGA.setStyleSheet(u"background-color: #006666;\n"
                                          "color: \"white\";\n"
                                          "font: 10pt \"Cascadia Code\";")
        self.lbl_show_infGA.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                         | Qt.AlignVCenter)
        self.lbl_show_infGA.setMargin(0)
        self.lbl_show_infGA.setIndent(5)
        self.lbl_show_infMR = QLabel(self.tab_inf)
        self.lbl_show_infMR.setObjectName(u"lbl_show_infMR")
        self.lbl_show_infMR.setGeometry(QRect(220, 240, 92, 16))
        self.lbl_show_infMR.setStyleSheet(u"background-color: #006666;\n"
                                          "color: \"white\";\n"
                                          "font: 10pt \"Cascadia Code\";")
        self.lbl_show_infMR.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                         | Qt.AlignVCenter)
        self.lbl_show_infMR.setMargin(0)
        self.lbl_show_infMR.setIndent(5)
        self.label_21 = QLabel(self.tab_inf)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(320, 180, 8, 16))
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"font: 10pt \"Cascadia Code\";")
        self.label_22 = QLabel(self.tab_inf)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(320, 210, 8, 16))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"font: 10pt \"Cascadia Code\";")
        self.label_24 = QLabel(self.tab_inf)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(320, 240, 8, 16))
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"font: 10pt \"Cascadia Code\";")
        self.label_25 = QLabel(self.tab_inf)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(70, 280, 141, 21))
        self.lbl_show_infTot = QLabel(self.tab_inf)
        self.lbl_show_infTot.setObjectName(u"lbl_show_infTot")
        self.lbl_show_infTot.setGeometry(QRect(220, 280, 92, 16))
        self.lbl_show_infTot.setStyleSheet(u"background-color: #006666;\n"
                                           "color: \"white\";\n"
                                           "font: 10pt \"Cascadia Code\";")
        self.lbl_show_infTot.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                          | Qt.AlignVCenter)
        self.lbl_show_infTot.setMargin(0)
        self.lbl_show_infTot.setIndent(5)
        self.label_26 = QLabel(self.tab_inf)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(320, 280, 8, 16))
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"font: 10pt \"Cascadia Code\";")
        self.psBtnSave_inf = QPushButton(self.tab_inf)
        self.psBtnSave_inf.setObjectName(u"psBtnSave_inf")
        self.psBtnSave_inf.setGeometry(QRect(410, 270, 121, 31))
        self.tabWidget.addTab(self.tab_inf, "")


        # -------------- TAB LAYOUT --------------------

        self.tab_maq = QWidget()
        self.tab_maq.setObjectName(u"tab_maq")
        self.tab_maq.setStyleSheet(u"font: 9pt \"Bookerly\";\n"
                                   "color: \"white\";")
        self.label_19 = QLabel(self.tab_maq)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 40, 401, 31))
        self.label_19.setStyleSheet(
            u"font: 20pt \"Bookerly\"; color: 'white';")
        self.label_27 = QLabel(self.tab_maq)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(50, 120, 131, 41))
        self.label_28 = QLabel(self.tab_maq)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(50, 170, 89, 19))
        self.label_28.setFont(font1)
        self.label_28.setAlignment(Qt.AlignLeading | Qt.AlignLeft
                                   | Qt.AlignVCenter)
        self.spinBox_maqPal = QSpinBox(self.tab_maq)
        self.spinBox_maqPal.setObjectName(u"spinBox_maqPal")
        self.spinBox_maqPal.setGeometry(QRect(170, 130, 111, 22))
        self.spinBox_maqPal.setStyleSheet(u"background-color: #006666;\n"
                                          "color: \"white\";\n"
                                          "font: 10pt \"Cascadia Code\";\n"
                                          "")
        self.spinBox_maqPal.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                         | Qt.AlignVCenter)
        self.spinBox_maqPal.setMaximum(1000000)
        self.spinBox_maqPal.setSingleStep(1000)
        self.lbl_show_maqPag = QLabel(self.tab_maq)
        self.lbl_show_maqPag.setObjectName(u"lbl_show_maqPag")
        self.lbl_show_maqPag.setGeometry(QRect(170, 170, 92, 21))
        self.lbl_show_maqPag.setStyleSheet(u"background-color: #006666;\n"
                                           "color: \"white\";\n"
                                           "font: 10pt \"Cascadia Code\";")
        self.lbl_show_maqPag.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                          | Qt.AlignVCenter)
        self.lbl_show_maqPag.setMargin(0)
        self.lbl_show_maqPag.setIndent(5)
        self.lbl_show_maqLib = QLabel(self.tab_maq)
        self.lbl_show_maqLib.setObjectName(u"lbl_show_maqLib")
        self.lbl_show_maqLib.setGeometry(QRect(460, 130, 92, 21))
        self.lbl_show_maqLib.setStyleSheet(u"background-color: #006666;\n"
                                           "color: \"white\";\n"
                                           "font: 10pt \"Cascadia Code\";")
        self.lbl_show_maqLib.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                          | Qt.AlignVCenter)
        self.lbl_show_maqLib.setMargin(0)
        self.lbl_show_maqLib.setIndent(5)
        self.lbl_show_maqeB1 = QLabel(self.tab_maq)
        self.lbl_show_maqeB1.setObjectName(u"lbl_show_maqeB1")
        self.lbl_show_maqeB1.setGeometry(QRect(460, 170, 92, 21))
        self.lbl_show_maqeB1.setStyleSheet(u"background-color: #006666;\n"
                                           "color: \"white\";\n"
                                           "font: 10pt \"Cascadia Code\";")
        self.lbl_show_maqeB1.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                          | Qt.AlignVCenter)
        self.lbl_show_maqeB1.setMargin(0)
        self.lbl_show_maqeB1.setIndent(5)
        self.lbl_show_maqeB2 = QLabel(self.tab_maq)
        self.lbl_show_maqeB2.setObjectName(u"lbl_show_maqeB2")
        self.lbl_show_maqeB2.setGeometry(QRect(460, 210, 92, 21))
        self.lbl_show_maqeB2.setStyleSheet(u"background-color: #006666;\n"
                                           "color: \"white\";\n"
                                           "font: 10pt \"Cascadia Code\";")
        self.lbl_show_maqeB2.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                          | Qt.AlignVCenter)
        self.lbl_show_maqeB2.setMargin(0)
        self.lbl_show_maqeB2.setIndent(5)
        self.lbl_show_maqTot = QLabel(self.tab_maq)
        self.lbl_show_maqTot.setObjectName(u"lbl_show_maqTot")
        self.lbl_show_maqTot.setGeometry(QRect(460, 250, 92, 21))
        self.lbl_show_maqTot.setStyleSheet(u"background-color: #006666;\n"
                                           "color: \"white\";\n"
                                           "font: 10pt \"Cascadia Code\";")
        self.lbl_show_maqTot.setAlignment(Qt.AlignRight | Qt.AlignTrailing
                                          | Qt.AlignVCenter)
        self.lbl_show_maqTot.setMargin(0)
        self.lbl_show_maqTot.setIndent(5)
        self.label_32 = QLabel(self.tab_maq)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(370, 250, 89, 19))
        self.label_32.setFont(font1)
        self.label_32.setAlignment(Qt.AlignLeading | Qt.AlignLeft
                                   | Qt.AlignVCenter)
        self.psBtnSave_maq = QPushButton(self.tab_maq)
        self.psBtnSave_maq.setObjectName(u"psBtnSave_maq")
        self.psBtnSave_maq.setGeometry(QRect(50, 240, 121, 31))
        self.checkBox_libro = QCheckBox(self.tab_maq)
        self.checkBox_libro.setObjectName(u"checkBox_libro")
        self.checkBox_libro.setGeometry(QRect(350, 130, 66, 18))
        self.checkBox_ebook1 = QCheckBox(self.tab_maq)
        self.checkBox_ebook1.setObjectName(u"checkBox_ebook1")
        self.checkBox_ebook1.setGeometry(QRect(350, 170, 66, 18))
        self.checkBox_ebook2 = QCheckBox(self.tab_maq)
        self.checkBox_ebook2.setObjectName(u"checkBox_ebook2")
        self.checkBox_ebook2.setGeometry(QRect(350, 210, 66, 18))
        self.label_29 = QLabel(self.tab_maq)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(560, 132, 8, 16))
        self.label_29.setFont(font2)
        self.label_29.setStyleSheet(u"font: 10pt \"Cascadia Code\";")
        self.label_30 = QLabel(self.tab_maq)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(560, 172, 8, 16))
        self.label_30.setFont(font2)
        self.label_30.setStyleSheet(u"font: 10pt \"Cascadia Code\";")
        self.label_31 = QLabel(self.tab_maq)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(560, 212, 8, 16))
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"font: 10pt \"Cascadia Code\";")
        self.label_33 = QLabel(self.tab_maq)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(560, 252, 8, 16))
        self.label_33.setFont(font2)
        self.label_33.setStyleSheet(u"font: 10pt \"Cascadia Code\";")
        self.tabWidget.addTab(self.tab_maq, "")

        # -------------- TAB END --------------------//

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

        # ----------MY LOGIC CODE------------------
        self.var_tab = None

        self.spinBox_matr.valueChanged.connect(self.aproximate_corr)

        self.spinBox_matr.valueChanged.connect(self.set_corr_rates)
        self.slider_compl.valueChanged.connect(self.set_corr_rates)
        self.spinBox_percen.valueChanged.connect(self.set_corr_rates)

        self.radioBtn_orto.toggled.connect(self.set_corr_rates)
        self.radioBtn_sty.toggled.connect(self.set_corr_rates)
        self.radioBtn_full.toggled.connect(self.set_corr_rates)
        self.psBtnSave.pressed.connect(self.save_corr)
        self.psBtnSave.clicked.connect(self.save)
        self.btn_about.clicked.connect(self.about_this)


        self.psBtnSave_inf.pressed.connect(self.save_inf)
        self.psBtnSave_inf.clicked.connect(self.save)
        self.spinBox_inf_pal.valueChanged.connect(self.set_inf_rates)
        self.checkBox_GA.toggled.connect(self.set_inf_rates)
        self.checkBox_MR.toggled.connect(self.set_inf_rates)


        self.spinBox_maqPal.valueChanged.connect(self.aproximate_maq)
        self.spinBox_maqPal.valueChanged.connect(self.set_maq_rates)
        self.checkBox_libro.toggled.connect(self.set_maq_rates)
        self.checkBox_ebook1.toggled.connect(self.set_maq_rates)
        self.checkBox_ebook2.toggled.connect(self.set_maq_rates)
        self.psBtnSave_maq.pressed.connect(self.save_maq)
        self.psBtnSave_maq.clicked.connect(self.save)

    def save_corr(self):
        self.dia = localtime()
        self.var_tab = self.export_corr()

    def save_inf(self):
        self.dia = localtime()
        self.var_tab = self.export_inf()

    def save_maq(self):
        self.dia = localtime()
        self.var_tab = 'maq'

# --------------TAB CORR FUNCTIONS-----------------

    def aproximate_corr(self, chars):
        words = round(chars / 5.6)
        pags = ceil(words / 330)
        self.lbl_palab.setText(str(words))
        self.lbl_pags.setText(str(pags))

    def set_corr_rates(self):
        matr = self.spinBox_matr.value()
        perc = float(self.spinBox_percen.value())

        rates_lg = [[0.80, 1.25, 1.60], [0.83, 1.30, 1.63], [0.85, 1.35, 1.75],
                    [0.90, 1.42, 1.85], [0.95, 1.50, 1.95]]
        rates_sm = [[0.85, 1.30, 1.65], [0.88, 1.35, 1.73], [0.90, 1.40, 1.80],
                    [0.95, 1.50, 1.90], [1.00, 1.60, 2.00]]
        rates = []
        if matr > 90000:
            rates = rates_lg
        else:
            rates = rates_sm

        orto_rate = rates[self.slider_compl.sliderPosition() - 1][0]
        sty_rate = rates[self.slider_compl.sliderPosition() - 1][1]
        full_rate = rates[self.slider_compl.sliderPosition() - 1][2]
        orto_rate = round(matr / 1000 * orto_rate, 2)
        sty_rate = round(matr / 1000 * sty_rate, 2)
        full_rate = round(matr / 1000 * full_rate, 2)
        if int(perc) != 0:
            orto_rate += orto_rate / 100 * perc
            sty_rate += sty_rate / 100 * perc
            full_rate += full_rate / 100 * perc
        orto_rate = round(orto_rate, 2)
        sty_rate = round(sty_rate, 2)
        full_rate = round(full_rate, 2)
        self.lbl_show_orto.setText(f'{orto_rate:.2f}')
        self.lbl_show_sty.setText(f'{sty_rate:.2f}')
        self.lbl_show_full.setText(f'{full_rate:.2f}')

        if self.radioBtn_orto.isChecked():
            self.invoice(orto_rate)
        if self.radioBtn_sty.isChecked():
            self.invoice(sty_rate)
        if self.radioBtn_full.isChecked():
            self.invoice(full_rate)

    def invoice(self, ammount):
        self.lbl_base.setText(f'{ammount:.2f}')
        irpf = (float(ammount) * 15) / 100
        iva = (float(ammount) * 21) / 100
        total = round(float(ammount) - irpf + iva, 2)
        self.lbl_irpf.setText(f'{-(irpf):.2f}')
        self.lbl_iva.setText(f'{iva:.2f}')
        self.lbl_total.setText(f'{total:.2f}')

    def save(self):
        fname, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", ".",
                                               "Archivo de texto (*.txt)")

        if fname:
            with open(fname, "w", encoding="utf-8") as f:
                f.write(self.var_tab)

    def export_corr(self):
        # set_corr_rates
        matr = self.spinBox_matr.value()
        perc = self.spinBox_percen.value()
        compl = self.slider_compl.sliderPosition()
        orto_rate = self.lbl_show_orto.text()
        sty_rate = self.lbl_show_sty.text()
        full_rate = self.lbl_show_full.text()
        # aproximate
        words = self.lbl_palab.text()
        pags = self.lbl_pags.text()
        # invoice
        rate = self.lbl_base.text()
        irpf = self.lbl_irpf.text()
        iva = self.lbl_iva.text()
        total = self.lbl_total.text()

        chain01_h1 = 'CALCULADORA DE TARIFAS\npresupuesto: '
        chain02_ts = f'{str(self.dia[0])[2:]}{self.dia[1]:02d}{self.dia[2]:02d} {self.dia[3]:02d}:{self.dia[4]:02d}'
        chain03 = '\n\n+----------------------------+\n|                            |\n| Matrices:'
        chain04_mt = (' ' * (14 - len(str(matr))) + str(matr))
        chain05 = '    |\n| Complejidad:        '
        chain06_cm = str(compl) + '/5'
        chain07 = '    |\n| Desc./recargo:'
        chain08_pr = (' ' * (9 - len(str(perc))) + str(perc))
        chain09 = ' %  |\n\
|                            |\n\
| Palabras aprox.:'

        chain10_wr = (' ' * (7 - len(words)) + words)
        chain11 = '    |\n\
| Páginas aprox.:'

        chain12_pg = (' ' * (8 - len(pags)) + pags)
        chain13 = '    |\n\
|                            |\n\
+----------------------------+\n\
\n\
Presupuesto:\n\
+----------------------------+\n\
| ORTOTIPOGRÁFICA '

        chain14_or = (' ' * (8 - len(orto_rate)) + orto_rate)
        chain15 = ' € |\n\
+----------------------------+\n\
| DE ESTILO       '

        chain16_sr = (' ' * (8 - len(sty_rate)) + sty_rate)
        chain17 = ' € |\n\
+----------------------------+\n\
| COMPLETA        '

        chain18_fr = (' ' * (8 - len(full_rate)) + full_rate)
        chain19 = ' € |\n\
+----------------------------+\n\
\n'

        if rate == 0:
            chain20_rt = 'SIN FACTURA'
        else:
            if rate == orto_rate:
                chain20_rt = 'Factura c. ORTOTIPOGRÁFICA:\n'
            elif rate == sty_rate:
                chain20_rt = 'Factura c. DE ESTILO:\n'
            elif rate == full_rate:
                chain20_rt = 'Factura c. COMPLETA:\n'

        output01 = [
            chain01_h1, chain02_ts, chain03, chain04_mt, chain05, chain06_cm,
            chain07, chain08_pr, chain09, chain10_wr, chain11, chain12_pg,
            chain13, chain14_or, chain15, chain16_sr, chain17, chain18_fr,
            chain19, chain20_rt
        ]

        if rate != '0':
            chain21 = '+----------------------------+\n\
| Precio base     '

            chain22_pb = (' ' * (8 - len(rate)) + rate)
            chain23 = ' € |\n\
+----------------------------+\n\
| IRPF            '

            chain24_ir = (' ' * (8 - len(irpf)) + irpf)
            chain25 = ' € |\n\
+----------------------------+\n\
| IVA             '

            chain26_iv = (' ' * (8 - len(iva)) + iva)
            chain27 = ' € |\n\
+----------------------------+\n\
| Total           '

            chain28_tt = (' ' * (8 - len(total)) + total)
            chain29 = ' € |\n\
+----------------------------+'

            output02 = [
                chain21, chain22_pb, chain23, chain24_ir, chain25, chain26_iv,
                chain27, chain28_tt, chain29
            ]

            return ("".join(output01 + output02))

        return ("".join(output01))

    def about_this(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Acerca de…")
        dialog.setStyleSheet(u"background-color: #5de5d7;")
        dialog.setText('Calculadora de tarifas\n\
© 2022 Noa Velasco [---vicios editoriales]'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   )
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.button(QMessageBox.Ok).setText("Aceptar")
        dialog.setIcon(QMessageBox.Information)

        dialog.exec_()


# --------------TAB INFORM FUNCTIONS-----------------

    def set_inf_rates(self):
        words = self.spinBox_inf_pal.value()
        sub_tot = 160 + (words/1000)
        base_rate = sub_tot - (sub_tot * 0.20)
        
        if self.checkBox_GA.isChecked():
            self.lbl_show_infGA.setText(f'{base_rate * 0.30:.2f}')
        else:
            self.lbl_show_infGA.setText('0')

        if self.checkBox_MR.isChecked():
            self.lbl_show_infMR.setText(f'{base_rate * 0.30:.2f}')
        else:
            self.lbl_show_infMR.setText('0')
            
        rate_ga = float(self.lbl_show_infGA.text())
        rate_mr = float(self.lbl_show_infMR.text())
        total = base_rate + rate_ga + rate_mr
        self.lbl_show_infTot.setText(f'{total:.2f}')

        if words != 0:
            self.lbl_show_infBase.setText(f'{base_rate:.2f}')
        else:
            self.lbl_show_infBase.setText('0')
            self.lbl_show_infGA.setText('0')
            self.lbl_show_infMR.setText('0')
            self.lbl_show_infTot.setText('0')

    def export_inf(self):
        words = self.spinBox_inf_pal.value()
        inf_base = self.lbl_show_infBase.text()
        inf_GA = self.lbl_show_infGA.text()
        inf_MR = self.lbl_show_infMR.text()
        inf_total = self.lbl_show_infTot.text()

        chain01 = 'CALCULADORA DE TARIFAS\npresupuesto: '
        chain02 = f'{str(self.dia[0])[2:]}{self.dia[1]:02d}{self.dia[2]:02d} {self.dia[3]:02d}:{self.dia[4]:02d}'
        chain03 = '\n\n\
Informe de lectura\n\
+----------------------------+\n\
|                            |\n\
| Palabras:'

        chain04 = (' ' * (15 - len(str(words))) + str(words))
        chain05 = '   |\n\
|                            |\n\
+----------------------------+\n\
| Informe base    '
        chain06 = (' ' * (8 - len(str(inf_base))) + str(inf_base))
        chain07 = ' € |\n\
+----------------------------+\n'

        # options
        chain08_op1 = '| Gráfica arg.    '
        chain09_op1 = (' ' * (8 - len(str(inf_GA))) + str(inf_GA))
        # finish with v: chain07

        chain10_op2 = '| Manuscrito rev. '
        chain11_op2 = (' ' * (8 - len(str(inf_MR))) + str(inf_MR))
        # finish with v: chain07

        # total
        chain12 = '| TOTAL           '
        chain13 = (' ' * (8 - len(str(inf_total))) + str(inf_total))
        # finish with v: chain07

        output = [
            chain01, chain02, chain03, chain04, chain05, chain06, chain07,
            chain12, chain13, chain07
        ]

        if self.checkBox_MR.isChecked():
            output.insert(7, chain07)
            output.insert(7, chain11_op2)
            output.insert(7, chain10_op2)
        if self.checkBox_GA.isChecked():
            output.insert(7, chain07)
            output.insert(7, chain09_op1)
            output.insert(7, chain08_op1)

        return ("".join(output))




# --------------TAB LAYOUT FUNCTIONS-----------------

    def aproximate_maq(self, chars):
        self.lbl_show_maqPag.setText(str(ceil(chars/330)))

    def set_maq_rates(self):
        book = self.spinBox_maqPal.value()/1000 * 3.5 + 50
        ebook1 = self.spinBox_maqPal.value() / 1000 * 0.15 + 30
        ebook2 = ebook1 - ebook1 * 0.20

        if self.checkBox_libro.isChecked():
            self.lbl_show_maqLib.setText(f'{book:.2f}')
        else:
            self.lbl_show_maqLib.setText('0')

        if self.checkBox_ebook1.isChecked():
            self.lbl_show_maqeB1.setText(f'{ebook1:.2f}')
        else:
            self.lbl_show_maqeB1.setText('0')

        if self.checkBox_ebook2.isChecked():
            self.lbl_show_maqeB2.setText(f'{ebook2:.2f}')
        else:
            self.lbl_show_maqeB2.setText('0')


        rate_bk = float(self.lbl_show_maqLib.text())
        rate_eb1 = float(self.lbl_show_maqeB1.text())
        rate_eb2 = float(self.lbl_show_maqeB2.text())
        total = rate_bk + rate_eb1 + rate_eb2
        self.lbl_show_maqTot.setText(f'{total:.2f}')

# setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Calculadora de tarifas",
                                        None))
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", u"Tarifas correcciones",
                                        None))
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", u"IRPF", None))
        self.lbl_pags.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.radioBtn_sty.setText("")
        self.lbl_show_full.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.radioBtn_full.setText("")
        self.lbl_iva.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", u"Descuentos o recargos",
                                        None))
        self.radioBtn_orto.setText("")
        self.lbl_irpf.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", u"Integral", None))
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"Matrices", None))
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"Ortotipogr\u00e1fica",
                                        None))
        self.lbl_show_orto.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.label_17.setText(
            QCoreApplication.translate("MainWindow", u"Total", None))
        self.lbl_base.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", u"P\u00e1ginas aprox.",
                                        None))
        self.lbl_palab.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", u"IVA", None))
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", u"%", None))
        self.lbl_show_sty.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_total.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", u"Precio base", None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"Estilo", None))
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", u"Complejidad", None))
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", u"Palabras aprox.", None))
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.psBtnSave.setText(
            QCoreApplication.translate("MainWindow", u"Exportar a texto\u2026",
                                        None))
        #if QT_CONFIG(shortcut)
        self.psBtnSave.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
        #endif // QT_CONFIG(shortcut)
        self.btn_about.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_corr),
            QCoreApplication.translate("MainWindow", u"Correcciones", None))
        self.label_18.setText(
            QCoreApplication.translate("MainWindow",
                                        u"Tarifas informes de lectura", None))
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", u"N.\u00ba de palabras",
                                        None))
        self.label_23.setText(
            QCoreApplication.translate("MainWindow", u"Informe base", None))
        self.checkBox_GA.setText(
            QCoreApplication.translate("MainWindow",
                                        u"Gr\u00e1fica argumental", None))
        self.checkBox_MR.setText(
            QCoreApplication.translate("MainWindow", u"Manuscrito revisado",
                                        None))
        self.lbl_show_infBase.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_show_infGA.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_show_infMR.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.label_21.setText(
            QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.label_22.setText(
            QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.label_24.setText(
            QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.label_25.setText(
            QCoreApplication.translate("MainWindow", u"Total", None))
        self.lbl_show_infTot.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.label_26.setText(
            QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.psBtnSave_inf.setText(
            QCoreApplication.translate("MainWindow", u"Exportar a texto\u2026",
                                        None))
        #if QT_CONFIG(shortcut)
        self.psBtnSave_inf.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
        #endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_inf),
            QCoreApplication.translate("MainWindow", u"Informes de lectura",
                                        None))
        self.label_19.setText(
            QCoreApplication.translate("MainWindow", u"Tarifas maquetaciones",
                                        None))
        self.label_27.setText(
            QCoreApplication.translate("MainWindow", u"N.\u00ba de palabras",
                                        None))
        self.label_28.setText(
            QCoreApplication.translate("MainWindow", u"P\u00e1ginas aprox.",
                                        None))
        self.lbl_show_maqPag.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_show_maqLib.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_show_maqeB1.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_show_maqeB2.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_show_maqTot.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.label_32.setText(
            QCoreApplication.translate("MainWindow", u"Total", None))
        self.psBtnSave_maq.setText(
            QCoreApplication.translate("MainWindow", u"Exportar a texto\u2026",
                                        None))
        #if QT_CONFIG(shortcut)
        self.psBtnSave_maq.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
        #endif // QT_CONFIG(shortcut)
        self.checkBox_libro.setText(
            QCoreApplication.translate("MainWindow", u"Libro", None))
        self.checkBox_ebook1.setText(
            QCoreApplication.translate("MainWindow", u"eBook 1", None))
        self.checkBox_ebook2.setText(
            QCoreApplication.translate("MainWindow", u"eBook 2", None))
        self.label_29.setText(
            QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.label_30.setText(
            QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.label_31.setText(
            QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.label_33.setText(
            QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_maq),
            QCoreApplication.translate("MainWindow", u"Maquetaciones", None))

    # retranslateUi


class MainWindow(QMainWindow, Ui_MainWindow):
    # Heredamos de QMainWindow y de la interfaz

    def __init__(self):

        # Llamamos al constructor explícito de QMainWindow
        super().__init__()

        # Ejecutamos el método setupUi heredado del diseño,
        # gracias al cual se generará la interfaz gráfica
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    iconWin = qta.icon('fa5s.calculator')
    app.setWindowIcon(iconWin)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
