# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QToolBar,
    QToolButton, QTreeWidgetItem, QVBoxLayout, QWidget)

from image_list_widget import ImageListWidget
from image_viewer import ImageViewer
from metadata_tree import MetadataTree
from settings_window import GenerationSettingsWindow
from textbox import TextBox
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1680, 1168)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks|QMainWindow.VerticalTabs)
        self.actionOpen_Folder = QAction(MainWindow)
        self.actionOpen_Folder.setObjectName(u"actionOpen_Folder")
        icon = QIcon()
        icon.addFile(u"icons/folder-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_Folder.setIcon(icon)
        self.actionE_xit = QAction(MainWindow)
        self.actionE_xit.setObjectName(u"actionE_xit")
        self.actionE_xit.setMenuRole(QAction.QuitRole)
        self.actionAdd_to_Favorites = QAction(MainWindow)
        self.actionAdd_to_Favorites.setObjectName(u"actionAdd_to_Favorites")
        self.actionAdd_to_Favorites.setCheckable(True)
        icon1 = QIcon()
        icon1.addFile(u":/image/icons/heart-medical.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/image/icons/heart-break.svg", QSize(), QIcon.Normal, QIcon.On)
        self.actionAdd_to_Favorites.setIcon(icon1)
        self.actionAdd_to_Favorites.setMenuRole(QAction.ApplicationSpecificRole)
        self.actionRemove_from_Favorites = QAction(MainWindow)
        self.actionRemove_from_Favorites.setObjectName(u"actionRemove_from_Favorites")
        icon2 = QIcon()
        icon2.addFile(u":/image/icons/heart-break.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRemove_from_Favorites.setIcon(icon2)
        self.actionRemove_from_Favorites.setMenuRole(QAction.ApplicationSpecificRole)
        self.actionShow_Favorites_Only = QAction(MainWindow)
        self.actionShow_Favorites_Only.setObjectName(u"actionShow_Favorites_Only")
        self.actionShow_Favorites_Only.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(u":/image/icons/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionShow_Favorites_Only.setIcon(icon3)
        self.actionShow_Favorites_Only.setMenuRole(QAction.ApplicationSpecificRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_27 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(3, 6, 3, 6)
        self.imageView = ImageViewer(self.centralwidget)
        self.imageView.setObjectName(u"imageView")
        sizePolicy.setHeightForWidth(self.imageView.sizePolicy().hasHeightForWidth())
        self.imageView.setSizePolicy(sizePolicy)
        self.imageView.setFrameShape(QFrame.Box)

        self.verticalLayout_27.addWidget(self.imageView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1680, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.promptDock = QDockWidget(MainWindow)
        self.promptDock.setObjectName(u"promptDock")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.promptDock.sizePolicy().hasHeightForWidth())
        self.promptDock.setSizePolicy(sizePolicy1)
        self.promptDock.setFloating(False)
        self.promptDock.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.promptDock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_25 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_15 = QLabel(self.dockWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)

        self.promptFilter = QToolButton(self.dockWidgetContents)
        self.promptFilter.setObjectName(u"promptFilter")
        self.promptFilter.setText(u"")
        self.promptFilter.setIconSize(QSize(18, 18))
        self.promptFilter.setCheckable(True)
        self.promptFilter.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.promptFilter)


        self.verticalLayout_22.addLayout(self.horizontalLayout_3)

        self.promptText = TextBox(self.dockWidgetContents)
        self.promptText.setObjectName(u"promptText")
        self.promptText.setReadOnly(True)

        self.verticalLayout_22.addWidget(self.promptText)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_16 = QLabel(self.dockWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_18.addWidget(self.label_16)

        self.negativePromptFilter = QToolButton(self.dockWidgetContents)
        self.negativePromptFilter.setObjectName(u"negativePromptFilter")
        self.negativePromptFilter.setText(u"")
        self.negativePromptFilter.setCheckable(True)
        self.negativePromptFilter.setAutoRaise(True)

        self.horizontalLayout_18.addWidget(self.negativePromptFilter)


        self.verticalLayout_23.addLayout(self.horizontalLayout_18)

        self.negativePromptText = TextBox(self.dockWidgetContents)
        self.negativePromptText.setObjectName(u"negativePromptText")
        self.negativePromptText.setReadOnly(True)

        self.verticalLayout_23.addWidget(self.negativePromptText)


        self.verticalLayout_22.addLayout(self.verticalLayout_23)


        self.verticalLayout_21.addLayout(self.verticalLayout_22)


        self.verticalLayout_25.addLayout(self.verticalLayout_21)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_7)

        self.promptDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.promptDock)
        self.metadataDock = QDockWidget(MainWindow)
        self.metadataDock.setObjectName(u"metadataDock")
        sizePolicy1.setHeightForWidth(self.metadataDock.sizePolicy().hasHeightForWidth())
        self.metadataDock.setSizePolicy(sizePolicy1)
        self.metadataDock.setFloating(False)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.metadataWidget = MetadataTree(self.dockWidgetContents_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.metadataWidget.setHeaderItem(__qtreewidgetitem)
        self.metadataWidget.setObjectName(u"metadataWidget")
        self.metadataWidget.setRootIsDecorated(True)
        self.metadataWidget.setUniformRowHeights(False)
        self.metadataWidget.setSortingEnabled(True)
        self.metadataWidget.setWordWrap(True)
        self.metadataWidget.setColumnCount(2)
        self.metadataWidget.header().setVisible(True)

        self.verticalLayout_3.addWidget(self.metadataWidget)

        self.metadataDock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.metadataDock)
        self.SettingsDock = GenerationSettingsWindow(MainWindow)
        self.SettingsDock.setObjectName(u"SettingsDock")
        self.SettingsDock.setFloating(False)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.SettingsDock)
        self.thumbnailsDock = QDockWidget(MainWindow)
        self.thumbnailsDock.setObjectName(u"thumbnailsDock")
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.verticalLayout_28 = QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(1, 1, 1, 1)
        self.frame = QFrame(self.dockWidgetContents_5)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(32, 32))
        self.toolButton.setMaximumSize(QSize(32, 32))
        icon4 = QIcon()
        icon4.addFile(u"icons/letter-english-a.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon4)
        self.toolButton.setIconSize(QSize(30, 30))
        self.toolButton.setCheckable(True)
        self.toolButton.setChecked(True)
        self.toolButton.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.frame_2)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy2)
        self.toolButton_2.setMinimumSize(QSize(32, 32))
        self.toolButton_2.setMaximumSize(QSize(32, 32))
        icon5 = QIcon()
        icon5.addFile(u"icons/calender.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon5)
        self.toolButton_2.setIconSize(QSize(30, 30))
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setChecked(False)
        self.toolButton_2.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.toolButton_2)


        self.horizontalLayout.addWidget(self.frame_2)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolButton_3 = QToolButton(self.frame_3)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(32, 32))
        self.toolButton_3.setMaximumSize(QSize(32, 32))
        icon6 = QIcon()
        icon6.addFile(u"icons/sort-amount-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon6)
        self.toolButton_3.setIconSize(QSize(30, 30))
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setChecked(True)
        self.toolButton_3.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.toolButton_3)

        self.toolButton_4 = QToolButton(self.frame_3)
        self.toolButton_4.setObjectName(u"toolButton_4")
        sizePolicy2.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy2)
        self.toolButton_4.setMinimumSize(QSize(32, 32))
        self.toolButton_4.setMaximumSize(QSize(32, 32))
        icon7 = QIcon()
        icon7.addFile(u"icons/sort-amount-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon7)
        self.toolButton_4.setIconSize(QSize(30, 30))
        self.toolButton_4.setCheckable(True)
        self.toolButton_4.setChecked(False)
        self.toolButton_4.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.toolButton_4)


        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_28.addWidget(self.frame)

        self.imageList = ImageListWidget(self.dockWidgetContents_5)
        self.imageList.setObjectName(u"imageList")

        self.verticalLayout_28.addWidget(self.imageList)

        self.thumbnailsDock.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.thumbnailsDock)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setOrientation(Qt.Horizontal)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionE_xit)
        self.toolBar.addAction(self.actionOpen_Folder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_to_Favorites)
        self.toolBar.addAction(self.actionShow_Favorites_Only)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u".inviewer", None))
        self.actionOpen_Folder.setText(QCoreApplication.translate("MainWindow", u"&Open Folder...", None))
        self.actionE_xit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.actionAdd_to_Favorites.setText(QCoreApplication.translate("MainWindow", u"Add to Favorites", None))
#if QT_CONFIG(tooltip)
        self.actionAdd_to_Favorites.setToolTip(QCoreApplication.translate("MainWindow", u"Add to Favorites", None))
#endif // QT_CONFIG(tooltip)
        self.actionRemove_from_Favorites.setText(QCoreApplication.translate("MainWindow", u"Remove from Favorites", None))
#if QT_CONFIG(tooltip)
        self.actionRemove_from_Favorites.setToolTip(QCoreApplication.translate("MainWindow", u"Remove from Favorites", None))
#endif // QT_CONFIG(tooltip)
        self.actionShow_Favorites_Only.setText(QCoreApplication.translate("MainWindow", u"Show Favorites Only", None))
#if QT_CONFIG(tooltip)
        self.actionShow_Favorites_Only.setToolTip(QCoreApplication.translate("MainWindow", u"Show Favorites Only", None))
#endif // QT_CONFIG(tooltip)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.promptDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Prompt", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Prompt", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.metadataDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.SettingsDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Generation Settings", None))
        self.thumbnailsDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Thumbnails", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

