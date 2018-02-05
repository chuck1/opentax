import json
import numpy
import os

import opentax.form

class Worksheet_6251(opentax.form.Form):
    def fill(self, taxes):
        
        print("Worksheet 6251")

        line1 = taxes.form_1040().line("41")

        line2 = 0

        line3 = taxes.form_1040_schedule_A.line("9")

        line4 = sum([
            line1,
            line2,
            line3,
            ])
        
        line5 = sum([
            taxes.form_1040().line("10"),
            taxes.form_1040().line("21"),
            ])

        line6 = 0

        line7 = sum([
            line5,
            line6,
            ])

        line8 = line4 - line7

        line9 = 83800

        if line8 < line9:
            print("you do not need to fill in Form 6251")
            return

        print("continue with worksheet")

        line10 = line8 - line9

        line11 = 159700

        if line8 > line11:
            line12 = line8 - line11
            line13 = min(line12 * 0.25, line9)
            line14 = line10 + line13
        else:
            line12 = 0
            line14 = line10

        print("line14",line14)

        if line14 > 186300:
            print("you need to fill in Form 6251")
            return
        
        line15 = line14 * 0.26

        line16 = sum([
            taxes.form_1040.line44,
            taxes.form_1040.line46,
            ])
        
        print("line15", line15)
        print("line16", line16)

        if line15 > line16:
            print("you need to fill in Form 6251")
        else:
            print("you do not need to fill in Form 6251")


