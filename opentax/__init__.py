import json
import numpy
import os
import enum

import opentax.form_w_2
import opentax.form_OR_40
import opentax.form_1040
import opentax.form_1098

class FilingStatus(enum.Enum):
    MARRIED_JOINT = 2

def form_factory(filename):
    with open(filename, "r") as f:
        data = json.loads(f.read())
    
    forms = {
            "W-2": opentax.form_w_2.Form_W_2,
            "1040": opentax.form_1040.Form_1040,
            "1098": opentax.form_1098.Form_1098,
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









