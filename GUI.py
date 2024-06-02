#-----------------------------#
#          6/2/2024           #
#-----------------------------#
from PyQt5.QtWidgets import *
import Color_Detection
import numpy as np
import sys


class GUI(QWidget):
    def __init__(self) -> None:
        super().__init__() 

        # To Check if we should put text for small detections or not
        self.PUT_TEXT_BOOL: bool = False

        self.FORM_LAYOUT: QFormLayout = QFormLayout(self)

        # Image Path Input

        self.Image_Input: QLineEdit  = QLineEdit(self)
        
        # Buttons
        
        self.File_Dialog_Button: QPushButton = QPushButton("Browse", self)
        self.Color_Dialog_Lower_Button: QPushButton = QPushButton("Browse Color", self)
        self.Color_Dialog_Upper_Button: QPushButton = QPushButton("Browse Color", self)
        self.Detect_Color_Button: QPushButton = QPushButton("Detect Colors in range", self)
        
        # Signing Functions to Buttons
        
        self.File_Dialog_Button.clicked.connect(self.File_Dialog__)
        self.Color_Dialog_Lower_Button.clicked.connect(self.Get_Color_Dialog_Lower)
        self.Color_Dialog_Upper_Button.clicked.connect(self.Get_Color_Dialog_Upper)
        self.Detect_Color_Button.clicked.connect(self.Detect_Color_In_Range)

        # All inputs for the Lower (minimum) range
        self.R_Input_Lower: QLineEdit = QLineEdit(self)
        self.G_Input_Lower: QLineEdit = QLineEdit(self)
        self.B_Input_Lower: QLineEdit = QLineEdit(self)
        # All inputs for the Upper (maximum) range
        self.R_Input_Upper: QLineEdit = QLineEdit(self)
        self.G_Input_Upper: QLineEdit = QLineEdit(self)
        self.B_Input_Upper: QLineEdit = QLineEdit(self)

        # To See if we should put text for small detections or not
        self.Put_Text_Check_Box: QCheckBox = QCheckBox("Put Text For small detections", None)
        self.Put_Text_Check_Box.stateChanged.connect(self.Put_Text_For_Small_Detections)

        # Adding All of the widgets to the layout

        self.FORM_LAYOUT.addRow(QLabel("Enter The Image Path : "), self.Image_Input)
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

        self.FORM_LAYOUT.addRow(self.Put_Text_Check_Box)

        self.FORM_LAYOUT.addRow(self.Detect_Color_Button)        
    
        self.setLayout(self.FORM_LAYOUT)


    def File_Dialog__(self) -> None:
        # Getting path of a file (By dialog)
        self.FileDIALOG: tuple[str, str] = QFileDialog.getOpenFileName(None, "Browse", None, "(*.png , *.jpg)")
        # Turning the Path ( From Dialog ) to an list and then getting the first value which is only the path
        self.FileDialogOutput: str = list(self.FileDIALOG)[0]

        self.Image_Input.setText(self.FileDialogOutput)
    

    def Put_Text_For_Small_Detections(self) -> None:
        # Changing the boolean to the opposite So we can detect changes in the check box properly
        self.PUT_TEXT_BOOL = not(self.PUT_TEXT_BOOL)


    def Detect_Color_In_Range(self) -> None:
        # Getting the image path
        IMAGE_PATH: str = str(self.Image_Input.text())
        # Getting all the lower( Minimum ) Colors
        RED_LOWER: str = self.R_Input_Lower.text()
        GREEN_LOWER: str = self.G_Input_Lower.text()
        BLUE_LOWER: str = self.B_Input_Lower.text()
        # Getting all the upper( Maximum ) Colors
        RED_UPPER: str = self.R_Input_Upper.text()
        GREEN_UPPER: str = self.G_Input_Upper.text()
        BLUE_UPPER: str = self.B_Input_Upper.text()
        # Turning them all to 2 numpy arrays that our program can handle and uint8 which is used to describe color values ( 0 to 255 )
        RGB_LOWER: np.array = np.array([BLUE_LOWER, GREEN_LOWER, RED_LOWER], dtype="uint8")

        RGB_UPPER: np.array = np.array([BLUE_UPPER, GREEN_UPPER, RED_UPPER], dtype="uint8")
        # if the checkbox is not checked then do not Show the texts for small detections
        if self.PUT_TEXT_BOOL == False:
            Color_Detection.Detect_Color(RGB_LOWER, RGB_UPPER, IMAGE_PATH, False)
        # if the checkbox is checked then do Show the texts for small detections
        if self.PUT_TEXT_BOOL == True:
            Color_Detection.Detect_Color(RGB_LOWER, RGB_UPPER, IMAGE_PATH, True)
    
    
    def Get_Color_Dialog_Lower(self) -> None:
        # Making a Dialog for lower colors ... 
        self.Color_Dialog: any = QColorDialog.getColor(parent=None)
        # ... And Getting Colors from the it
        RED: any = self.Color_Dialog.red()
        GREEN: any = self.Color_Dialog.green()
        BLUE: any = self.Color_Dialog.blue()

        self.R_Input_Lower.setText(str(RED))
        self.G_Input_Lower.setText(str(GREEN))
        self.B_Input_Lower.setText(str(BLUE))


    def Get_Color_Dialog_Upper(self) -> None:
        # Making a Dialog for upper colors ... 
        self.Color_Dialog: any = QColorDialog.getColor(parent=None)
        # ... And Getting Colors from the it
        RED: any = self.Color_Dialog.red()
        GREEN: any = self.Color_Dialog.green()
        BLUE: any = self.Color_Dialog.blue()

        self.R_Input_Upper.setText(str(RED))
        self.G_Input_Upper.setText(str(GREEN))
        self.B_Input_Upper.setText(str(BLUE))

# Running the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    app.exec_()
