import json
import numpy
import os

import opentax.form

class _Form_1040_Schedule_A(opentax.form.Form):
    pass

class Form_1040_Schedule_A(_Form_1040_Schedule_A):
    def __init__(self):
        super(Form_1040_Schedule_A, self).__init__()
    
        self.line_calc_table = {
                "15": self.line_15,
                "29": self.line_29,
                }

    def line_15(self):
        return self.line("10") + self.line("13")

    def line_29(self):
        return self.line("4") + self.line("9") + self.line("15")

    def fill(self, taxes):
        
        # medical and dental expenses
        self.lines["4"] = 0
        
        # income taxes paid
        self.lines["5"] = taxes.forms_W_2.line("17")
        
        # real estate taxes
        self.lines["6"] = 0
        #taxes.forms_1098.line("10")
        
        # personal property taxes
        self.lines["7"] = 0

        # other taxes
        self.lines["8"] = 0

        self.lines["9"] = sum([
            self.line("5"),
            self.line("6"),
            self.line("7"),
            self.line("8"),
            ])

        # interest paid
        self.lines["10"] = taxes.forms_1098.line("1") + taxes.forms_1098.line("6")

        self.lines["13"] = taxes.forms_1098.line("5")
       

