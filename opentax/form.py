import inspect
import crayons

class Form:
    line_calc_table = {}

    def __init__(self, filename=None, data=None):
        self.filename = None
        self.lines = {}
        self.line_description = {}

    def read(self, filename, data):
        self.filename = filename
        self.data = data

        if data is None:
            self.lines = {}
        else:
            self.lines = data["lines"]

    def line_calc(self, line_name):
        try:
            func = self.line_calc_table[line_name]
        except KeyError:
            raise
        else:
            return func()
    
    def line(self, line_name):

        try:
            return self.line_calc(line_name)
        except KeyError:
            pass

        try:
            return self.lines[line_name]
        except KeyError:
            msg = "{} in file {} does not have line {}".format(
                self.__class__.__name__,
                repr(self.filename),
                repr(line_name))
            print(crayons.red(msg))
            raise Exception(msg)

    def print_lines(self, lines):
        for line in lines:
            print("line {:3}: {:30}: {:12.2f}".format(
                line, 
                self.line_description.get(line, ""),
                self.line(line), 
                ))
    
