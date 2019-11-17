import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from calculator_ui import Ui_MainWindow
from math import *

class main(QMainWindow):
    
    def __init__(self):
        super(main,self).__init__()
        main.init(self)
        
    def init(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.get_operation = []

        self.ui.btn_1.clicked.connect(self.btn1)
        self.ui.btn_2.clicked.connect(self.btn2)
        self.ui.btn_3.clicked.connect(self.btn3)
        self.ui.btn_4.clicked.connect(self.btn4)
        self.ui.btn_5.clicked.connect(self.btn5)
        self.ui.btn_6.clicked.connect(self.btn6)
        self.ui.btn_7.clicked.connect(self.btn7)
        self.ui.btn_8.clicked.connect(self.btn8)
        self.ui.btn_9.clicked.connect(self.btn9)
        self.ui.btn_0.clicked.connect(self.btn0)
        self.ui.btn_dot.clicked.connect(self.btnDot)
        self.ui.btn_soma.clicked.connect(self.btnSum)
        self.ui.btn_sub.clicked.connect(self.btnSub)
        self.ui.btn_mult.clicked.connect(self.btnMult)
        self.ui.btn_div.clicked.connect(self.btnDiv)
        self.ui.btn_clear.clicked.connect(self.clearDisplay)
        self.ui.btn_ok.clicked.connect(self.enterOK)
        self.ui.btn_x2.clicked.connect(self.btnX2)
        self.ui.btn_x3.clicked.connect(self.btnX3)
        self.ui.btn_sqrt.clicked.connect(self.btnSqrt)
        self.ui.btn_1x.clicked.connect(self.btn1X)
        self.ui.btn_sin.clicked.connect(self.btnSin)
        self.ui.btn_cos.clicked.connect(self.btnCos)
        self.ui.btn_tg.clicked.connect(self.btnTg)
        self.ui.btn_1tg.clicked.connect(self.btn1Tg)
        
    def btn1(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '1')
        
         
    def btn2(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '2')

    def btn3(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '3')

    def btn4(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '4')

    def btn5(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '5')

    def btn6(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '6')

    def btn7(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '7')

    def btn8(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '8')

    def btn9(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '9')

    def btn0(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '0')

    def btnDot(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '.')

    def btnSum(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '+')
        self.get_operation.append('+')

    def btnSub(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '-')
        self.get_operation.append('-')

    def btnMult(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + 'x')
        self.get_operation.append('x')

    def btnDiv(self):
        self.ui.ln_display.setText(self.ui.ln_display.text() + '/')
        self.get_operation.append('/')

    def btnX2(self):
        try:
            display = float(self.ui.ln_display.text())
            xx = display**2
            self.ui.ln_display.setText('{}'.format(xx)) 
        except ValueError:
            pass    
        
    def btnX3(self):
        try:
            display = float(self.ui.ln_display.text())
            xxx = display**3
            self.ui.ln_display.setText('{}'.format(xxx)) 
        except ValueError:
            pass     
    
    def btnSqrt(self):
        try:
            display = float(self.ui.ln_display.text())
            op = sqrt(display)          
            
            self.ui.ln_display.setText('{}'.format(op))
        except ValueError:
            self.ui.ln_display.setText('Value Error.')
    
    def btn1X(self):
        try:
            display = float(self.ui.ln_display.text())
            op = 1 / display
            self.ui.ln_display.setText('{}'.format(op))
            
        except ZeroDivisionError:
            self.ui.ln_display.setText('Division by 0.')

        except ValueError:
            pass
     
    def btnSin(self):
        try:
            display = float(self.ui.ln_display.text())
            opsin = sin(display)
            self.ui.ln_display.setText('{}'.format(opsin)) 
        except ValueError:
            pass
    
    def btnCos(self):
        try:
            display = float(self.ui.ln_display.text())
            opcos = cos(display)
            self.ui.ln_display.setText('{}'.format(opcos)) 
        except ValueError:
            pass
    
    def btnTg(self):
        try:
            display = float(self.ui.ln_display.text())
            optg = tan(display)
            self.ui.ln_display.setText('{}'.format(optg)) 
        except ValueError:
            pass
        
    def btn1Tg(self):
        try:
            display = float(self.ui.ln_display.text())
            op1tg = 1 / tan(display)
            self.ui.ln_display.setText('{}'.format(op1tg)) 
        except ValueError:
            pass
       
    def clearDisplay(self):
        self.ui.ln_display.clear()
        self.get_operation.clear()
        
    def enterOK(self):
        try:
            display = self.ui.ln_display.text()
            operation = self.get_operation[0]
            sub_first = [oper for oper in display if oper == '-' or oper == '+']                
            if len(sub_first) == 2:
                if sub_first[0] == '-' and sub_first[1] == '-':
                    numbers = [nmb for nmb in display.split('-') if nmb != '-']
                    subb = -float(numbers[1]) - float(numbers[2])
                    self.ui.ln_display.setText('{}'.format(subb))
                        
                if sub_first[0] == '-' and sub_first[1] == '+':
                    numbers = [float(nmb) for nmb in display.split('+') if nmb != '-']
                    soma = numbers[0] + numbers[1]
                    self.ui.ln_display.setText('{}'.format(soma))               
                                
            else:
                numbers = [float(op) for op in display.split(operation)]
                
                if operation == '+':
                    soma = numbers[0] + numbers[1]
                    self.ui.ln_display.setText('{}'.format(soma))
                
                elif operation == '-':
                    sub = numbers[0] - numbers[1]
                    self.ui.ln_display.setText('{}'.format(sub))
                
                elif operation == 'x':
                    sub = numbers[0] * numbers[1]
                    self.ui.ln_display.setText('{}'.format(sub))
                
                elif operation == '/':
                    try:
                        div = numbers[0] / numbers[1]
                        self.ui.ln_display.setText('{}'.format(div))
                    except ZeroDivisionError:
                        self.ui.ln_display.setText('Division by 0.')

                self.get_operation.clear()
            
        except IndexError:
            pass
        except ValueError:
            pass
            
    def keyPressEvent(self, event):
        key = event.key()
        
        if key == Qt.Key_1:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '1')
        elif key == Qt.Key_2:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '2')
            
        elif key == Qt.Key_3:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '3')

        elif key == Qt.Key_4:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '4')

        elif key == Qt.Key_5:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '5')
        
        elif key == Qt.Key_6:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '6')
        
        elif key == Qt.Key_7:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '7')
        
        elif key == Qt.Key_8:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '8')

        elif key == Qt.Key_9:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '9')
        
        elif key == Qt.Key_0:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '0')
        
        elif key == Qt.Key_Period: #dot
            self.ui.ln_display.setText(self.ui.ln_display.text() + '.')

        elif key == Qt.Key_Plus:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '+')
            self.get_operation.append('+')
        
        elif key == Qt.Key_Minus:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '-')
            self.get_operation.append('-')

        elif key == Qt.Key_Asterisk:
            self.ui.ln_display.setText(self.ui.ln_display.text() + 'x')
            self.get_operation.append('x')
        
        elif key == Qt.Key_Slash:
            self.ui.ln_display.setText(self.ui.ln_display.text() + '/')
            self.get_operation.append('/')

        elif key == Qt.Key_Escape:
            self.ui.ln_display.clear()
            self.get_operation.clear()
                       
        if key == Qt.Key_Enter or key == Qt.Key_Return: #both enters
            try:
                display = self.ui.ln_display.text()
                operation = self.get_operation[0]
                sub_first = [oper for oper in display if oper == '-' or oper == '+']                
                if len(sub_first) == 2: #In case of double negative numbers or one negative and one positive
                    if sub_first[0] == '-' and sub_first[1] == '-':
                        numbers = [nmb for nmb in display.split('-') if nmb != '-']
                        subb = -float(numbers[1]) - float(numbers[2])
                        self.ui.ln_display.setText('{}'.format(subb))
                         
                    if sub_first[0] == '-' and sub_first[1] == '+':
                        numbers = [float(nmb) for nmb in display.split('+') if nmb != '-']
                        soma = numbers[0] + numbers[1]
                        self.ui.ln_display.setText('{}'.format(soma))               
                                    
                else: #Normal sum
                    numbers = [float(op) for op in display.split(operation)]
                    
                    if operation == '+':
                        soma = numbers[0] + numbers[1]
                        self.ui.ln_display.setText('{}'.format(soma))
                    
                    elif operation == '-':
                        sub = numbers[0] - numbers[1]
                        self.ui.ln_display.setText('{}'.format(sub))
                    
                    elif operation == 'x':
                        sub = numbers[0] * numbers[1]
                        self.ui.ln_display.setText('{}'.format(sub))
                    
                    elif operation == '/':
                        try:
                            div = numbers[0] / numbers[1]
                            self.ui.ln_display.setText('{}'.format(div))
                        except ZeroDivisionError:
                            self.ui.ln_display.setText('Division by 0.')

                    self.get_operation.clear()
                
            except IndexError:
                pass
            except ValueError:
                pass
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = main()
    gui.show()
    sys.exit(app.exec_())