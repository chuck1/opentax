import json
import numpy
import os
import opentax.form_1040_sch_a

class Form_1040(opentax.form.Form):
    def __init__(self):
        super(Form_1040, self).__init__()

        self.line_calc_table["6d"] = self.line_6d

    def line_6d(self):
        return self.line("6a") + self.line("6b") + len(self.line("6c"))

    def fill(self, taxes):
        
        taxes.form_1040_schedule_A = opentax.form_1040_sch_a.Form_1040_Schedule_A()

        # line 6
        line6d = self.line("6d")

        # line 7
        line7 = taxes.forms_W_2.line("1")
  
        self.line10 = 0
        self.line21 = 0

        # line 22
        line22 = line7

        # line 36
        line36 = 0

        # line 37
        self.line37 = line22 - line36

        # line 38
        line38 = self.line37

        # fill schedule A
        taxes.form_1040_schedule_A.fill(taxes)
        
        # line 40
        line40 = taxes.form_1040_schedule_A.line29

        # line 41
        self.line41 = line38 - line40

        if line38 < 155650:
            line42 = 4050 * line6d

        line43 = max(self.line41 - line42, 0)

        tt = taxes.tax_table
        
        self.line44 = tt.lookup(line43, 1)

        self.line46 = 0

        # line 45
        worksheet_6251 = Worksheet_6251()
        worksheet_6251.fill(taxes)

        line47 = sum([
                self.line44,
                ])

        line55 = 0
        
        self.line56 = max(line47 - line55, 0)

        self.line59 = 0

        # line 63
        line63 = sum([
            self.line56,
            ])

        # payments
        line64 = taxes.form_totals("W-2", "box2")

        self.line68 = 0

        line74 = sum([
            line64,
            ])

        # line 75
        line75 = max(line74 - line63, 0)

        # print output
        
        print("Form 1040")
        print("line   7: {:16.2f}".format(line7))
        print("line  10: {:16.2f}".format(self.line10))
        print("line  21: {:16.2f}".format(self.line21))
        print("line  22: {:16.2f}".format(line22))
        print("line  36: {:16.2f}".format(line36))
        print("line  37: {:16.2f}".format(self.line37))
        print("line  38: {:16.2f}".format(line38))

        print()
        print("schedule A")
        print("  {:<32}{:16.0f}".format("line   5: state and local tax",taxes.form_1040_schedule_A.line5))
        print("  {:<32}{:16.0f}".format("line   6", taxes.form_1040_schedule_A.line6))
        print("  {:<32}{:16.0f}".format("line   9", taxes.form_1040_schedule_A.line9))
        print("  {:<32}{:16.0f}".format("line  10", taxes.form_1040_schedule_A.line10))
        print("  {:<32}{:16.0f}".format("line  13", taxes.form_1040_schedule_A.line13))
        print("  {:<32}{:16.0f}".format("line  15", taxes.form_1040_schedule_A.line15))
        print("  {:<32}{:16.0f}".format("line  29", taxes.form_1040_schedule_A.line29))

        print("{:<32}{:16.2f}".format("line  40:", line40))
        print("{:<32}{:16.2f}".format("line  41:", self.line41))
        print("{:<32}{:16.2f}".format("line  43:", line43))
        print("{:<32}{:16.2f}".format("line  44:", self.line44))
        print("{:<32}{:16.2f}".format("line  47:", line47))
        print("{:<32}{:16.2f}".format("line  55:", line55))
        print("{:<32}{:16.2f}".format("line  56: line47 - line55", self.line56))
        print("{:<32}{:16.2f}".format("line  63: total tax", line63))
        print("{:<32}{:16.2f}".format("line  64:", line64))
        print("{:<32}{:16.2f}".format("line  74: payments", line74))
        print("{:<32}{:16.2f}".format("line  75:", line75))


