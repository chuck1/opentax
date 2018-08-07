import json
import numpy
import os

import opentax.form

class WorksheetChildTaxCredit(opentax.form.Form):
    def fill(self, taxes):
        
        print("Child Tax Credit Worksheet")

        form_1040 = taxes.form_1040()
   
        n = sum([1 for line in form_1040.line("6c") if line.get("tax credit", False)])

        #import pdb;pdb.set_trace()

        line_01 = n * 1000

        line_02 = form_1040.line("38")

        line_03 = 110000

        if line_02 > line_03:
            line_04 = math.ceil((line_02 - line_03) / 1000) * 1000
            line_05 = line_04 * 0.05
        else:
            line_05 = 0

        if line_01 > line_05:
            line_06 = line_01 - line_05
        else:
            line_10 = 0
            return
        

        line_07 = form_1040.line("47")

        line_08 = sum([
            form_1040.line("48", 0),
            form_1040.line("49", 0),
            form_1040.line("50", 0),
            form_1040.line("51", 0),
            ])

        if line_07 == line_08:
            line_10 = 0
            print("you may be able to take the additional child tax credit")
            return
        
        line_09 = line_07 - line_08

        if line_06 > line_09:
            line_10 = line_09
            print("you may be able to take the additional child tax credit")
            return

        self.lines["10"] = line_06


