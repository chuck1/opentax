import crayons

class Form:
    def __init__(self, filename=None, data=None):
        pass

    def read(self, filename, data):
        self.filename = filename
        self.data = data
        self.line_calc_table = {}

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
            print(crayons.red("{} in file {} does not have line {}".format(
                self.__class__.__name__,
                repr(self.filename),
                repr(line_name))))
            raise


