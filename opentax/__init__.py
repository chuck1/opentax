import json
import os

class Taxes(object):
    forms_input = []
    def load_input(self, folder):

        for root, dirs, files in os.walk(folder):
            print root, dirs, files
            
            for fn in files:
                print fn
                print os.path.join(root, fn)

                with open(os.path.join(root, fn), "r") as f:
                    form = json.loads(f.read())

                print form

                self.forms_input.append(form)



