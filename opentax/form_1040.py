import json
import numpy
import os

import opentax.form_1040_sch_a
import opentax.worksheet_6251
import opentax.worksheet_child_tax_credit

class _Form_1040(opentax.form.Form):
    line_calc_table = {}

class Form_1040(_Form_1040):

    line_42_adjusted_gross_income_limit = 156900
    line_42_exemption = 4050

    def __init__(self):
        super(Form_1040, self).__init__()

        self.line_description["37"] = "adjusted gross income"
        self.line_description["38"] = "adjusted gross income"
        self.line_description["40"] = "itemized deductions"
        self.line_description["42"] = "exemptions"
        self.line_description["42"] = "taxable income"
        self.line_description["75"] = "overpaid"
        
        self.line_calc_table = {
                "6d": self.line_6d,
                "22": self.line_22,
                "37": self.line_37,
                "38": self.line_38,
                "41": self.line_41,
                "42": self.line_42,
                "43": self.line_43,
                "47": self.line_47,
                "56": self.line_56,
                "63": self.line_63,
                "74": self.line_74,
                "75": self.line_75,
                }

    def status(self):
        if self.line("2"):
            return opentax.FilingStatus.MARRIED_JOINT

    def line_6d(self):
        return self.line("6a") + self.line("6b") + len(self.line("6c"))

    def line_22(self):
        # total income
        # just W-2
        return self.line("7")

    def line_37(self):
        return self.line("22") - self.line("36")

    def line_38(self):
        return self.line("37")

    def line_41(self):
        return self.line("38") - self.line("40")

    def line_42(self):
        if self.line("38") < self.line_42_adjusted_gross_income_limit:
            return self.line_42_exemption * self.line("6d")
        raise NotImplementedError()

    def line_43(self):
        return max(self.line("41") - self.line("42"), 0)

    def line_47(self):
        return sum([
                self.line("44"),
                self.line("45"),
                self.line("46"),
                ])

    def line_56(self):
        return max(self.line("47") - self.line("55"), 0)

    def line_63(self):
        return sum([
            self.line("56"),
            ])

    def line_74(self):
        return sum([
            self.line("64"),
            ])

    def line_75(self):
        return max(self.line("74") - self.line("63"), 0)

    def line_(self):
        return

    def line_(self):
        return

    def line_(self):
        return

    def fill(self, taxes):
        
        taxes.form_1040_schedule_A = opentax.form_1040_sch_a.Form_1040_Schedule_A()

        # line 7
        self.lines["7"] = taxes.forms_W_2.line("1")
        
        # taxable refunds, credits, or offsets of state and local income taxes
        self.lines["10"] = 0

        # other income
        self.lines["21"] = 0

        # adjustment a gross income
        self.lines["36"] = 0
        
        # fill schedule A
        taxes.form_1040_schedule_A.fill(taxes)
        
        # line 40
        self.lines["40"] = taxes.form_1040_schedule_A.line("29")


        self.lines["44"] = taxes.tax_table.lookup(self.line("43"), 1)

        self.lines["46"] = 0

        # line 45
        worksheet_6251 = opentax.worksheet_6251.Worksheet_6251()
        worksheet_6251.fill(taxes)
        self.lines["45"] = 0

        worksheet_child = opentax.worksheet_child_tax_credit.WorksheetChildTaxCredit()
        worksheet_child.fill(taxes)
        self.lines["52"] = worksheet_child.line("10")


        self.lines["55"] = sum([
            self.line("48", 0),
            self.line("49", 0),
            self.line("50", 0),
            self.line("51", 0),
            self.line("52", 0),
            self.line("53", 0),
            self.line("54", 0),
            ])
        

        self.lines["59"] = 0

        # line 63

        # payments
        self.lines["64"] = taxes.forms_W_2.line("2")

        self.lines["68"] = 0

        print("Form 1040")
        print("----------------------------------------------")
        self.print_lines([
            "7", "10", "21", "22", "36", "37", "38", "40", "41", "42", "43", "44", "47", 
            "52", "55", "56", "61", "63", "64", "74", "75"])
        print()

        print("Schedule A")
        print("----------------------------------------------")
        taxes.form_1040_schedule_A.print_lines(["5", "6","9", "10", "13", "15", "29"])
        print()
 
