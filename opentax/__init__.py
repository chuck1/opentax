import json
import numpy
import os

import opentax.form_w_2
import opentax.form_OR_40
import opentax.form_1040
import opentax.form_1098

class Worksheet_6251(object):
    def fill(self, taxes):
        
        print("Worksheet 6251")

        line1 = taxes.form_1040.line41

        line2 = 0

        line3 = sum([
            taxes.form_1040_schedule_A.line9,
            taxes.form_1040_schedule_A.line9,
            ])

        line4 = sum([
            line1,
            line2,
            line3,
            ])
        
        line5 = sum([
            taxes.form_1040.line10,
            taxes.form_1040.line21,
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

def form_factory(filename):
    with open(filename, "r") as f:
        data = json.loads(f.read())
    
    forms = {
            "W-2": opentax.form_w_2.Form_W_2,
            "1040": opentax.form_1040.Form_1040,
            }
    
    form = forms[data["form"]]()
    form.read(filename, data)
    return form

"""
sum of lines or boxes for a set of forms
"""
class FormGroup:
    def __init__(self, forms):
        self.forms = list(forms)

    def line(self, line_name):
        return sum(f.line(line_name) for f in self.forms)

class Taxes(object):
    forms_input = []
    
    def load_input(self, folder):
        for root, dirs, files in os.walk(folder):
            for fn in files:
                form = form_factory(os.path.join(root, fn))
                self.forms_input.append(form)

        self.forms_W_2 = FormGroup(self.forms_W_2())
        self.forms_1098 = FormGroup(self.forms_1098())

    def form_totals(self, form, box):
        y = 0
        for f in self.forms_input:
            if f["form"] == form:
                y += f[box]
        return y

    def forms_W_2(self):
        for f in self.forms_input:
            if isinstance(f, opentax.form_w_2.Form_W_2):
                yield f

    def forms_1098(self):
        for f in self.forms_input:
            if isinstance(f, opentax.form_1098.Form_1098):
                yield f

    def form_1040(self):
        forms = iter(f for f in self.forms_input if isinstance(f, opentax.form_1040.Form_1040))
        
        try:
            form = next(forms)
        except StopIteration:
            raise Exception("no 1040 input")

        try:
            next(forms)
        except StopIteration:
            pass
        else:
            raise Exception("more than one 1040")

        return form
        
    def form_OR_40(self):
        
        self.form_OR_40 = opentax.form_OR_40.Form_OR_40()
        self.form_OR_40.fill(self)









