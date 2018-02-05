import json
import numpy
import os



class Form_1040_Schedule_A:
    def fill(self, taxes):
        
        # medical and dental expenses
        self.line4 = 0
        
        # income taxes paid
        self.line5 = taxes.forms_W_2.line("box 17")
        
        # real estate taxes
        self.line6 = taxes.forms_1098.line("box 10")

        self.line9 = self.line5 + self.line6

        # interest paid
        self.line10 = taxes.forms_1098.line("box 1") + taxes.forms_1098.line("box 6")

        self.line13 = taxes.forms_1098.line("box 5")
       
        self.line15 = self.line10 + self.line13

        self.line29 = self.line4 + self.line9 + self.line15



