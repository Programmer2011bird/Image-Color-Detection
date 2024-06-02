from PyQt5.QtWidgets import *
import Color_Detection
import numpy as np
import sys


class GUI(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.FORM_LAYOUT: QFormLayout = QFormLayout(self)

        Image_Input_Label: QLabel = QLabel("Enter The Image Path : ", self) 
        self.Image_Input: QLineEdit  = QLineEdit(self)

        self.File_Dialog_Button: QPushButton = QPushButton("Browse", self)
        self.Color_Dialog_Lower_Button: QPushButton = QPushButton("Browse Color", self)
        self.Color_Dialog_Upper_Button: QPushButton = QPushButton("Browse Color", self)
        self.Detect_Color_Button: QPushButton = QPushButton("Detect Colors in range", self)

        self.File_Dialog_Button.clicked.connect(self.File_Dialog__)
        self.Color_Dialog_Lower_Button.clicked.connect(self.Get_Color_Dialog_Lower)
        self.Color_Dialog_Upper_Button.clicked.connect(self.Get_Color_Dialog_Upper)
        self.Detect_Color_Button.clicked.connect(self.Detect_Color_In_Range)


        self.R_Input_Lower: QLineEdit = QLineEdit(self)
        self.G_Input_Lower: QLineEdit = QLineEdit(self)
        self.B_Input_Lower: QLineEdit = QLineEdit(self)
        
        self.R_Input_Upper: QLineEdit = QLineEdit(self)
        self.G_Input_Upper: QLineEdit = QLineEdit(self)
        self.B_Input_Upper: QLineEdit = QLineEdit(self)


        self.FORM_LAYOUT.addRow(Image_Input_Label, self.Image_Input)
        self.FORM_LAYOUT.addRow(self.File_Dialog_Button)

        self.FORM_LAYOUT.addRow(QLabel('Minimum Color : '))
        
        self.FORM_LAYOUT.addRow(QLabel("R : "), self.R_Input_Lower)
        self.FORM_LAYOUT.addRow(QLabel("G : "), self.G_Input_Lower)
        self.FORM_LAYOUT.addRow(QLabel("B : "), self.B_Input_Lower)
        self.FORM_LAYOUT.addRow(self.Color_Dialog_Lower_Button)
        
        self.FORM_LAYOUT.addRow(QLabel('Maximum Color : '))

        self.FORM_LAYOUT.addRow(QLabel("R : "), self.R_Input_Upper)
        self.FORM_LAYOUT.addRow(QLabel("G : "), self.G_Input_Upper)
        self.FORM_LAYOUT.addRow(QLabel("B : "), self.B_Input_Upper)
        self.FORM_LAYOUT.addRow(self.Color_Dialog_Upper_Button)

        self.FORM_LAYOUT.addRow(self.Detect_Color_Button)        
    
        self.setLayout(self.FORM_LAYOUT)


    def File_Dialog__(self):
        self.FileDIALOG: tuple[str, str] = QFileDialog.getOpenFileName(None, "Browse", None, "(*.png , *.jpg)")

        self.FileDialogOutput: str = list(self.FileDIALOG)[0]

        self.Image_Input.setText(self.FileDialogOutput)
    
    
    def Detect_Color_In_Range(self):
        
        IMAGE_PATH: str = str(self.Image_Input.text())

        RED_LOWER: str = self.R_Input_Lower.text()
        GREEN_LOWER: str = self.G_Input_Lower.text()
        BLUE_LOWER: str = self.B_Input_Lower.text()

        RGB_LOWER: np.array = np.array([BLUE_LOWER, GREEN_LOWER, RED_LOWER], dtype="uint8")

        RED_UPPER: str = self.R_Input_Upper.text()
        GREEN_UPPER: str = self.G_Input_Upper.text()
        BLUE_UPPER: str = self.B_Input_Upper.text()
        
        RGB_UPPER: np.array = np.array([BLUE_UPPER, GREEN_UPPER, RED_UPPER], dtype="uint8")

        Color_Detection.Detect_Color(RGB_LOWER, RGB_UPPER, IMAGE_PATH)
    
    
    def Get_Color_Dialog_Lower(self):
        self.Color_Dialog: any = QColorDialog.getColor(parent=None)

        RED = self.Color_Dialog.red()
        GREEN = self.Color_Dialog.green()
        BLUE = self.Color_Dialog.blue()


        self.R_Input_Lower.setText(str(RED))
        self.G_Input_Lower.setText(str(GREEN))
        self.B_Input_Lower.setText(str(BLUE))


    def Get_Color_Dialog_Upper(self):
        self.Color_Dialog: any = QColorDialog.getColor(parent=None)

        RED = self.Color_Dialog.red()
        GREEN = self.Color_Dialog.green()
        BLUE = self.Color_Dialog.blue()


        self.R_Input_Upper.setText(str(RED))
        self.G_Input_Upper.setText(str(GREEN))
        self.B_Input_Upper.setText(str(BLUE))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    app.exec_()