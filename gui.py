import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QToolbar

class Window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Lumiere")
        self.setMinimumHeight(500)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        ##############################################################################################
        # Toolbar
        ##############################################################################################

        self.tools = {
            "cursor": {
                "tool": "CursorToolButton",
                "var": '_isCursor'
            },
            "color_picker": {
                "tool": "ColorPickerToolButton",
                "var": '_isColorPicking'
            },
            "histogram": {
                "tool": "HistogramToolButton",
                "var": '_isShowingHistogram'
            },
            "paint": {
                "tool": "PaintToolButton",
                "var": '_isPainting'
            },
            "fill": {
                "tool": "FillToolButton",
                "var": '_isFilling'
            },
            "select_rect": {
                "tool": "RectSelectToolButton",
                "var": '_isSelectingRect',
                "destructor": 'exitSelectRect'
            },
            "select_path": {
                "tool": "PathSelectToolButton",
                "var": '_isSelectingPath',
                "destructor": 'exitSelectPath'
            },
            "crop": {
                "tool": "CropToolButton",
                "var": '_isCropping'
            },
            "spot_removal": {
                "tool": "SpotRemovalToolButton",
                "var": '_isRemovingSpots'
            },
            "eraser": {
                "tool": "EraserToolButton",
                "var": '_isErasing'
            },
            "blur": {
                "tool": "BlurToolButton",
                "var": '_isBlurring'
            },
            "instagram_filters": {
                "tool": "InstagramFiltersToolButton",
                "var": '_isApplyingFilter'
            },
        }
        self.ToolbarDockWidget = QtWidgets.QDockWidget("Tools")
        self.ToolbarDockWidget.setTitleBarWidget(QtWidgets.QWidget())
        ToolbarContent = QtWidgets.QWidget()
        ToolbarLayout = QFlowLayout(ToolbarContent)
        ToolbarLayout.setSpacing(0)

       ##############################################################################################
        # Right Dock
        ##############################################################################################
        

        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea, self.ToolbarDockWidget)
        self.ToolbarDockWidget.setFloating(True)
        self.ToolbarDockWidget.setGeometry(QtCore.QRect(20, 20, 90, 600))

        
        ##############################################################################################
        # Show Window
        ##############################################################################################
        

        self.initImageViewer()
        self.ToolbarDockWidget.setParent(self.image_viewer)
        self.showMaximized()

        self.threadpool = QtCore.QThreadPool()
        self.sliderChangedPixmap = None
        self.sliderExplanationOfChange = None
        self.sliderTypeOfChange = None
        self.sliderValueOfChange = None
        self.sliderObjectOfChange = None
        self.sliderChangeSignal.connect(self.onUpdateImageCompleted)
        self.sliderWorkers = []

        self.resizeDockWidgets()

    def setIconPixmapWithColor(self, button, filename, findColor='black', newColor='white'):
        pixmap = QPixmap(filename)
        mask = pixmap.createMaskFromColor(QtGui.QColor(findColor), Qt.MaskMode.MaskOutColor)
        pixmap.fill((QtGui.QColor(newColor)))
        pixmap.setMask(mask)
        button.setIcon(QtGui.QIcon(pixmap))

    def setToolButtonStyleChecked(self, button):
        button.setStyleSheet('''
            border-color: rgb(22, 22, 22);
            background-color: rgb(22, 22, 22);
            border-style: solid;
        ''')
      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
