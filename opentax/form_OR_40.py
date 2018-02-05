
class Worksheet_OR_40_line_10(object):
    def fill(self, taxes):

        line1 = taxes.form_1040().line("56")

        line2 = taxes.form_1040.line46

        line3 = line1 - line2

        line4 = taxes.form_1040.line59

        line5 = line3 + line4

        line6 = taxes.form_1040.line68

        line7 = 0

        line8 = line6 + line7

        line9 = line5 - line8

        line10 = 6500

        self.line11 = min(line9, line10)

        print("Worksheet_OR_40_line_10")
        print(self.line11)


class Form_OR_40(object):
    def fill(self, taxes):

        worksheet_OR_40_line_10 = Worksheet_OR_40_line_10()
        worksheet_OR_40_line_10.fill(taxes)

        line7 = taxes.form_1040.line37

        line8 = 0

        line9 = line7 + line8

        line10 = worksheet_OR_40_line_10.line11

        line14 = line10
    
        line15 = line9 - line14

        line16 = taxes.form_1040_schedule_A.line29

        line17 = taxes.form_1040_schedule_A.line5

        line18 = line16 - line17
        
        line19 = 0

        line20 = max(line18, line19)

        line21 = line15 - line20

        if (line21 > 50000) and (line21 < 125000):
            line22 = 4028 + (line21 - 50000) * 0.09

        
        print("{:<32}{:16.2f}".format("line  21: taxable income", line21))
        print("{:<32}{:16.2f}".format("line  22: tax", line22))





