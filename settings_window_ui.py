# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QSizePolicy, QSpacerItem, QTabWidget, QToolBox,
    QToolButton, QVBoxLayout, QWidget)

from textbox import LineEditBox
import resources_rc

class Ui_SettingsDock(object):
    def setupUi(self, SettingsDock):
        if not SettingsDock.objectName():
            SettingsDock.setObjectName(u"SettingsDock")
        SettingsDock.resize(464, 856)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDock.sizePolicy().hasHeightForWidth())
        SettingsDock.setSizePolicy(sizePolicy)
        SettingsDock.setFloating(False)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_19 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_9 = QLabel(self.dockWidgetContents_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.modelNameText = LineEditBox(self.dockWidgetContents_3)
        self.modelNameText.setObjectName(u"modelNameText")
        self.modelNameText.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.modelNameText)

        self.modelNameFilter = QToolButton(self.dockWidgetContents_3)
        self.modelNameFilter.setObjectName(u"modelNameFilter")
        self.modelNameFilter.setText(u"")
        self.modelNameFilter.setCheckable(True)
        self.modelNameFilter.setAutoRaise(True)

        self.horizontalLayout_5.addWidget(self.modelNameFilter)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.tabWidget_2 = QTabWidget(self.dockWidgetContents_3)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_9.addWidget(self.tabWidget_2)

        self.line_2 = QFrame(self.dockWidgetContents_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)


        self.verticalLayout_19.addLayout(self.verticalLayout_9)

        self.toolBox = QToolBox(self.dockWidgetContents_3)
        self.toolBox.setObjectName(u"toolBox")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setGeometry(QRect(0, 0, 446, 174))
        self.verticalLayout_26 = QVBoxLayout(self.page_8)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_10 = QLabel(self.page_8)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.numStepText = LineEditBox(self.page_8)
        self.numStepText.setObjectName(u"numStepText")
        self.numStepText.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.numStepText)

        self.numStepFilter = QToolButton(self.page_8)
        self.numStepFilter.setObjectName(u"numStepFilter")
        self.numStepFilter.setText(u"\ud83d\udd0d")
        icon = QIcon()
        icon.addFile(u"icons/filter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.numStepFilter.setIcon(icon)
        self.numStepFilter.setCheckable(True)
        self.numStepFilter.setAutoRaise(True)

        self.horizontalLayout_12.addWidget(self.numStepFilter)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_11 = QLabel(self.page_8)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.cfgScaleText = LineEditBox(self.page_8)
        self.cfgScaleText.setObjectName(u"cfgScaleText")
        self.cfgScaleText.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.cfgScaleText)

        self.cfgScaleFilter = QToolButton(self.page_8)
        self.cfgScaleFilter.setObjectName(u"cfgScaleFilter")
        self.cfgScaleFilter.setText(u"\ud83d\udd0d")
        self.cfgScaleFilter.setIcon(icon)
        self.cfgScaleFilter.setCheckable(True)
        self.cfgScaleFilter.setAutoRaise(True)

        self.horizontalLayout_13.addWidget(self.cfgScaleFilter)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_13)


        self.verticalLayout_26.addLayout(self.horizontalLayout_21)

        self.groupBox_10 = QGroupBox(self.page_8)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setFlat(True)
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(1, 3, 1, 3)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.groupBox_10)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_15.addWidget(self.label_12)

        self.imageWidthText = LineEditBox(self.groupBox_10)
        self.imageWidthText.setObjectName(u"imageWidthText")
        self.imageWidthText.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.imageWidthText)

        self.imageWidthFilter = QToolButton(self.groupBox_10)
        self.imageWidthFilter.setObjectName(u"imageWidthFilter")

        self.horizontalLayout_15.addWidget(self.imageWidthFilter)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.groupBox_10)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.imageHeightText = LineEditBox(self.groupBox_10)
        self.imageHeightText.setObjectName(u"imageHeightText")
        self.imageHeightText.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.imageHeightText)

        self.imageHeightFilter = QToolButton(self.groupBox_10)
        self.imageHeightFilter.setObjectName(u"imageHeightFilter")

        self.horizontalLayout_16.addWidget(self.imageHeightFilter)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_16)


        self.verticalLayout_26.addWidget(self.groupBox_10)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_17.addWidget(self.label_14)

        self.samplerText = LineEditBox(self.page_8)
        self.samplerText.setObjectName(u"samplerText")
        self.samplerText.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.samplerText)

        self.samplerFilter = QToolButton(self.page_8)
        self.samplerFilter.setObjectName(u"samplerFilter")
        self.samplerFilter.setText(u"")
        self.samplerFilter.setCheckable(True)
        self.samplerFilter.setAutoRaise(True)

        self.horizontalLayout_17.addWidget(self.samplerFilter)


        self.verticalLayout_26.addLayout(self.horizontalLayout_17)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page_8, u"General")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 446, 208))
        self.verticalLayout_17 = QVBoxLayout(self.page_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(1, 1, 1, 1)
        self.groupBox_22 = QGroupBox(self.page_7)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setFlat(False)
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_22)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_62 = QLabel(self.groupBox_22)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_81.addWidget(self.label_62)

        self.seedText = LineEditBox(self.groupBox_22)
        self.seedText.setObjectName(u"seedText")
        self.seedText.setReadOnly(True)

        self.horizontalLayout_81.addWidget(self.seedText)

        self.seedFilter = QToolButton(self.groupBox_22)
        self.seedFilter.setObjectName(u"seedFilter")
        self.seedFilter.setText(u"")
        self.seedFilter.setCheckable(True)

        self.horizontalLayout_81.addWidget(self.seedFilter)


        self.verticalLayout_20.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_64 = QLabel(self.groupBox_22)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_84.addWidget(self.label_64)

        self.perlinNoiseText = LineEditBox(self.groupBox_22)
        self.perlinNoiseText.setObjectName(u"perlinNoiseText")
        self.perlinNoiseText.setReadOnly(True)

        self.horizontalLayout_84.addWidget(self.perlinNoiseText)

        self.perlinNoiseFilter = QToolButton(self.groupBox_22)
        self.perlinNoiseFilter.setObjectName(u"perlinNoiseFilter")
        self.perlinNoiseFilter.setText(u"")
        self.perlinNoiseFilter.setCheckable(True)

        self.horizontalLayout_84.addWidget(self.perlinNoiseFilter)


        self.horizontalLayout_82.addLayout(self.horizontalLayout_84)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_65 = QLabel(self.groupBox_22)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_85.addWidget(self.label_65)

        self.noiseThresholdText = LineEditBox(self.groupBox_22)
        self.noiseThresholdText.setObjectName(u"noiseThresholdText")
        self.noiseThresholdText.setReadOnly(True)

        self.horizontalLayout_85.addWidget(self.noiseThresholdText)

        self.noiseThresholdFilter = QToolButton(self.groupBox_22)
        self.noiseThresholdFilter.setObjectName(u"noiseThresholdFilter")
        self.noiseThresholdFilter.setText(u"")
        self.noiseThresholdFilter.setCheckable(True)

        self.horizontalLayout_85.addWidget(self.noiseThresholdFilter)


        self.horizontalLayout_82.addLayout(self.horizontalLayout_85)


        self.verticalLayout_20.addLayout(self.horizontalLayout_82)


        self.verticalLayout_17.addWidget(self.groupBox_22)

        self.groupBox_21 = QGroupBox(self.page_7)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setFlat(True)
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_54 = QLabel(self.groupBox_21)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_66.addWidget(self.label_54)

        self.lineEdit_52 = QLineEdit(self.groupBox_21)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setReadOnly(True)

        self.horizontalLayout_66.addWidget(self.lineEdit_52)

        self.toolButton_34 = QToolButton(self.groupBox_21)
        self.toolButton_34.setObjectName(u"toolButton_34")
        self.toolButton_34.setText(u"")
        self.toolButton_34.setCheckable(True)

        self.horizontalLayout_66.addWidget(self.toolButton_34)


        self.verticalLayout_18.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_55 = QLabel(self.groupBox_21)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_67.addWidget(self.label_55)

        self.lineEdit_53 = QLineEdit(self.groupBox_21)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setReadOnly(True)

        self.horizontalLayout_67.addWidget(self.lineEdit_53)

        self.toolButton_35 = QToolButton(self.groupBox_21)
        self.toolButton_35.setObjectName(u"toolButton_35")
        self.toolButton_35.setText(u"")
        self.toolButton_35.setCheckable(True)

        self.horizontalLayout_67.addWidget(self.toolButton_35)


        self.verticalLayout_18.addLayout(self.horizontalLayout_67)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_2)


        self.verticalLayout_17.addWidget(self.groupBox_21)

        self.toolBox.addItem(self.page_7, u"Seed/Variations")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 446, 88))
        self.verticalLayout_24 = QVBoxLayout(self.page_3)
        self.verticalLayout_24.setSpacing(1)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_44 = QLabel(self.page_3)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_54.addWidget(self.label_44)

        self.lineEdit_42 = QLineEdit(self.page_3)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setReadOnly(True)

        self.horizontalLayout_54.addWidget(self.lineEdit_42)

        self.toolButton_28 = QToolButton(self.page_3)
        self.toolButton_28.setObjectName(u"toolButton_28")
        self.toolButton_28.setText(u"")
        self.toolButton_28.setCheckable(True)

        self.horizontalLayout_54.addWidget(self.toolButton_28)


        self.horizontalLayout_70.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_45 = QLabel(self.page_3)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_55.addWidget(self.label_45)

        self.lineEdit_43 = QLineEdit(self.page_3)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setReadOnly(True)

        self.horizontalLayout_55.addWidget(self.lineEdit_43)

        self.toolButton_29 = QToolButton(self.page_3)
        self.toolButton_29.setObjectName(u"toolButton_29")
        self.toolButton_29.setText(u"")
        self.toolButton_29.setCheckable(True)

        self.horizontalLayout_55.addWidget(self.toolButton_29)


        self.horizontalLayout_70.addLayout(self.horizontalLayout_55)


        self.verticalLayout_24.addLayout(self.horizontalLayout_70)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page_3, u"Face Restorations")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 446, 94))
        self.verticalLayout_16 = QVBoxLayout(self.page_4)
        self.verticalLayout_16.setSpacing(1)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_59 = QLabel(self.page_4)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_72.addWidget(self.label_59)

        self.lineEdit_57 = QLineEdit(self.page_4)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setReadOnly(True)

        self.horizontalLayout_72.addWidget(self.lineEdit_57)

        self.toolButton_37 = QToolButton(self.page_4)
        self.toolButton_37.setObjectName(u"toolButton_37")
        self.toolButton_37.setText(u"")
        self.toolButton_37.setCheckable(True)

        self.horizontalLayout_72.addWidget(self.toolButton_37)


        self.verticalLayout_16.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_60 = QLabel(self.page_4)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_73.addWidget(self.label_60)

        self.lineEdit_58 = QLineEdit(self.page_4)
        self.lineEdit_58.setObjectName(u"lineEdit_58")
        self.lineEdit_58.setReadOnly(True)

        self.horizontalLayout_73.addWidget(self.lineEdit_58)

        self.toolButton_38 = QToolButton(self.page_4)
        self.toolButton_38.setObjectName(u"toolButton_38")
        self.toolButton_38.setText(u"")
        self.toolButton_38.setCheckable(True)

        self.horizontalLayout_73.addWidget(self.toolButton_38)


        self.horizontalLayout_57.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_63 = QLabel(self.page_4)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_77.addWidget(self.label_63)

        self.lineEdit_61 = QLineEdit(self.page_4)
        self.lineEdit_61.setObjectName(u"lineEdit_61")
        self.lineEdit_61.setReadOnly(True)

        self.horizontalLayout_77.addWidget(self.lineEdit_61)

        self.toolButton_39 = QToolButton(self.page_4)
        self.toolButton_39.setObjectName(u"toolButton_39")
        self.toolButton_39.setText(u"")
        self.toolButton_39.setCheckable(True)

        self.horizontalLayout_77.addWidget(self.toolButton_39)


        self.horizontalLayout_57.addLayout(self.horizontalLayout_77)


        self.verticalLayout_16.addLayout(self.horizontalLayout_57)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_4)

        self.toolBox.addItem(self.page_4, u"Upscaling")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 446, 88))
        self.verticalLayout_8 = QVBoxLayout(self.page_5)
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.groupBox_2 = QGroupBox(self.page_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(True)
        self.horizontalLayout_58 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_58.setSpacing(6)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_49 = QLabel(self.groupBox_2)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_60.addWidget(self.label_49)

        self.lineEdit_47 = QLineEdit(self.groupBox_2)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setReadOnly(True)

        self.horizontalLayout_60.addWidget(self.lineEdit_47)

        self.toolButton_31 = QToolButton(self.groupBox_2)
        self.toolButton_31.setObjectName(u"toolButton_31")
        self.toolButton_31.setText(u"")
        self.toolButton_31.setCheckable(True)

        self.horizontalLayout_60.addWidget(self.toolButton_31)


        self.horizontalLayout_58.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_50 = QLabel(self.groupBox_2)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_61.addWidget(self.label_50)

        self.lineEdit_48 = QLineEdit(self.groupBox_2)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setReadOnly(True)

        self.horizontalLayout_61.addWidget(self.lineEdit_48)

        self.toolButton_32 = QToolButton(self.groupBox_2)
        self.toolButton_32.setObjectName(u"toolButton_32")
        self.toolButton_32.setText(u"")
        self.toolButton_32.setCheckable(True)

        self.horizontalLayout_61.addWidget(self.toolButton_32)


        self.horizontalLayout_58.addLayout(self.horizontalLayout_61)


        self.verticalLayout_8.addWidget(self.groupBox_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.toolBox.addItem(self.page_5, u"Symmetry")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 446, 98))
        self.verticalLayout_15 = QVBoxLayout(self.page_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = QCheckBox(self.page_6)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setCheckable(False)
        self.checkBox.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBox)

        self.toolButton_40 = QToolButton(self.page_6)
        self.toolButton_40.setObjectName(u"toolButton_40")
        self.toolButton_40.setText(u"")
        self.toolButton_40.setCheckable(True)

        self.horizontalLayout.addWidget(self.toolButton_40)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_15.addLayout(self.horizontalLayout)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox_25 = QGroupBox(self.page_6)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setFlat(False)
        self.horizontalLayout_59 = QHBoxLayout(self.groupBox_25)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_68 = QLabel(self.groupBox_25)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_83.addWidget(self.label_68)

        self.lineEdit_66 = QLineEdit(self.groupBox_25)
        self.lineEdit_66.setObjectName(u"lineEdit_66")
        self.lineEdit_66.setReadOnly(True)

        self.horizontalLayout_83.addWidget(self.lineEdit_66)

        self.toolButton_42 = QToolButton(self.groupBox_25)
        self.toolButton_42.setObjectName(u"toolButton_42")
        self.toolButton_42.setText(u"")
        self.toolButton_42.setCheckable(True)

        self.horizontalLayout_83.addWidget(self.toolButton_42)


        self.horizontalLayout_59.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.checkBox_2 = QCheckBox(self.groupBox_25)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_79.addWidget(self.checkBox_2)

        self.toolButton_41 = QToolButton(self.groupBox_25)
        self.toolButton_41.setObjectName(u"toolButton_41")
        self.toolButton_41.setText(u"")
        self.toolButton_41.setCheckable(True)

        self.horizontalLayout_79.addWidget(self.toolButton_41)


        self.horizontalLayout_59.addLayout(self.horizontalLayout_79)


        self.verticalLayout.addWidget(self.groupBox_25)


        self.horizontalLayout_56.addLayout(self.verticalLayout)


        self.verticalLayout_15.addLayout(self.horizontalLayout_56)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_6)

        self.toolBox.addItem(self.page_6, u"Other Options")

        self.verticalLayout_19.addWidget(self.toolBox)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_8)

        SettingsDock.setWidget(self.dockWidgetContents_3)

        self.retranslateUi(SettingsDock)

        self.tabWidget_2.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SettingsDock)
    # setupUi

    def retranslateUi(self, SettingsDock):
        SettingsDock.setWindowTitle(QCoreApplication.translate("SettingsDock", u"Generation Settings", None))
        self.label_9.setText(QCoreApplication.translate("SettingsDock", u"Model", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("SettingsDock", u"Tab 1", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("SettingsDock", u"Tab 2", None))
        self.label_10.setText(QCoreApplication.translate("SettingsDock", u"Steps", None))
        self.label_11.setText(QCoreApplication.translate("SettingsDock", u"CFG Scale", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("SettingsDock", u"Size", None))
        self.label_12.setText(QCoreApplication.translate("SettingsDock", u"W", None))
        self.imageWidthFilter.setText("")
        self.label_13.setText(QCoreApplication.translate("SettingsDock", u"H", None))
        self.imageHeightFilter.setText("")
        self.label_14.setText(QCoreApplication.translate("SettingsDock", u"Sampler", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_8), QCoreApplication.translate("SettingsDock", u"General", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("SettingsDock", u"Seed", None))
        self.label_62.setText(QCoreApplication.translate("SettingsDock", u"Seed", None))
        self.label_64.setText(QCoreApplication.translate("SettingsDock", u"Perlin Noise", None))
        self.label_65.setText(QCoreApplication.translate("SettingsDock", u"Noise Threshold", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("SettingsDock", u"Variations", None))
        self.label_54.setText(QCoreApplication.translate("SettingsDock", u"Amount", None))
        self.label_55.setText(QCoreApplication.translate("SettingsDock", u"Seed Weigths", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), QCoreApplication.translate("SettingsDock", u"Seed/Variations", None))
        self.label_44.setText(QCoreApplication.translate("SettingsDock", u"Type", None))
        self.label_45.setText(QCoreApplication.translate("SettingsDock", u"Strengh", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("SettingsDock", u"Face Restorations", None))
        self.label_59.setText(QCoreApplication.translate("SettingsDock", u"Scale", None))
        self.label_60.setText(QCoreApplication.translate("SettingsDock", u"Denoising Strength", None))
        self.label_63.setText(QCoreApplication.translate("SettingsDock", u"Upscale Strength", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("SettingsDock", u"Upscaling", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingsDock", u"Step", None))
        self.label_49.setText(QCoreApplication.translate("SettingsDock", u"H", None))
        self.label_50.setText(QCoreApplication.translate("SettingsDock", u"V", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("SettingsDock", u"Symmetry", None))
        self.checkBox.setText(QCoreApplication.translate("SettingsDock", u"Seamless Tilling", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("SettingsDock", u"High Res Optimization", None))
        self.label_68.setText(QCoreApplication.translate("SettingsDock", u"Strength", None))
        self.checkBox_2.setText(QCoreApplication.translate("SettingsDock", u"High Res Optimization", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("SettingsDock", u"Other Options", None))
    # retranslateUi

