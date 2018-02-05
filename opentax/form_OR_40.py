
import opentax.form

class Worksheet_OR_40_line_10(opentax.form.Form):
    def fill(self, taxes):

        self.lines["1"] = taxes.form_1040().line("56")

        self.lines["2"] = taxes.form_1040().line("46")

        self.lines["3"] = self.line("1") - self.line("2")

        self.lines["4"] = taxes.form_1040().line("59")

        self.lines["5"] = self.line("3") + self.line("4")

        self.lines["6"] = taxes.form_1040().line("68")

        self.lines["7"] = 0

        self.lines["8"] = self.line("6") + self.line("7")

        self.lines["9"] = self.line("5") - self.line("8")

        self.lines["10"] = 6500

        self.lines["11"] = min(self.line("9"), self.line("10"))

        print("Worksheet_OR_40_line_10")
        print(self.line("11"))



class _Form_OR_40(opentax.form.Form):
    line_calc_table = {}

class Form_OR_40(_Form_OR_40):
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

        if (self.line("21") > 50000) and (self.line("21") < 125000):
            self.lines["22"] = 4028 + (self.line("21") - 50000) * 0.09

        
        print("{:<32}{:16.2f}".format("line  21: taxable income", self.line("21")))
        print("{:<32}{:16.2f}".format("line  22: tax", self.line("22")))





