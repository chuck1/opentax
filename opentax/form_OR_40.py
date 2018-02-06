import numpy as np

import opentax.form

class RangeTable:
    def lookup(self, x):
        X = self.table[:,0]
        #X0 = X[X < x]
        X1 = self.table[X > x]
        return X1[0]

class Worksheet_OR_40_line_10_Table_Married_Joint(RangeTable):
    def __init__(self):
        self.table = np.array([
            [125000, 6550],
            ])

class Worksheet_OR_40_line_10(opentax.form.Form):
    def __init__(self):
        super(Worksheet_OR_40_line_10, self).__init__(self)

        self.line_calc_table = {
                "10": self.line_10,
                }

    def line_10(self):

        if self.taxes.form_1040().status() == opentax.FilingStatus.MARRIED_JOINT:
            table = Worksheet_OR_40_line_10_Table_Married_Joint()

            return table.lookup(self.taxes.form_1040().line("37"))[1]
            

    def fill(self, taxes):
        self.taxes = taxes

        self.lines["1"] = taxes.form_1040().line("56")

        self.lines["2"] = taxes.form_1040().line("46")

        self.lines["3"] = self.line("1") - self.line("2")

        self.lines["4"] = taxes.form_1040().line("59")

        self.lines["5"] = self.line("3") + self.line("4")

        self.lines["6"] = taxes.form_1040().line("68")

        self.lines["7"] = 0

        self.lines["8"] = self.line("6") + self.line("7")

        self.lines["9"] = self.line("5") - self.line("8")

        self.lines["11"] = min(self.line("9"), self.line("10"))

        print(self.__class__.__name__)
        self.print_lines(["11"])
        print()


class Form_OR_40(opentax.form.Form):
    def __init__(self):
        super(Form_OR_40, self).__init__()

        self.line_calc_table = {
                "22": self.line_22,
                }

        self.line_description["21"] = "taxable income"
        self.line_description["22"] = "tax"
        
    def line_22(self):
        if (self.line("21") > 50000) and (self.line("21") < 125000):
            return 4024 + (self.line("21") - 50000) * 0.09

        raise NotImplementedError()

    def fill(self, taxes):

        worksheet_OR_40_line_10 = Worksheet_OR_40_line_10()
        worksheet_OR_40_line_10.fill(taxes)

        self.lines["7"] = taxes.form_1040().line("37")

        self.lines["8"] = 0

        self.lines["9"] = self.line("7") + self.line("8")

        self.lines["10"] = worksheet_OR_40_line_10.line("11")

        self.lines["14"] = self.line("10")
    
        self.lines["15"] = self.line("9") - self.line("14")

        self.lines["16"] = taxes.form_1040_schedule_A.line("29")

        self.lines["17"] = taxes.form_1040_schedule_A.line("5")

        self.lines["18"] = self.line("16") - self.line("17")
        
        self.lines["19"] = 0

        self.lines["20"] = max(self.line("18"), self.line("19"))

        self.lines["21"] = self.line("15") - self.line("20")
        
        self.lines["22"] = 0

        
        print(self.__class__.__name__)
        self.print_lines(["21", "22"])
        print()



