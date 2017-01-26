import json
import numpy
import os

class TaxTable2016(object):

    def __init__(self):
        self.table = numpy.array([
            [55550, 9653, 7401, 9653, 8179],
            [55600, 9665, 7409, 9665, 8191],
            [55650, 9678, 7416, 9678, 8204],
            [55700, 9690, 7424, 9690, 8216],
            [55750, 9703, 7431, 9703, 8229],
            [55800, 9715, 7439, 9715, 8241],
            [55850, 9728, 7446, 9728, 8254],
            [55900, 9740, 7454, 9740, 8266],
            [55950, 9753, 7461, 9753, 8279],
            [56000, 9765, 7469, 9765, 8291],
            [57050, 10028, 7626, 10028, 8554],
            [57100, 10040, 7634, 10040, 8566],
            [57150, 10053, 7641, 10053, 8579],
            [57200, 10065, 7649, 10065, 8591],
            [57250, 10078, 7656, 10078, 8604],
            [57300, 10090, 7664, 10090, 8616],
            [57350, 10103, 7671, 10103, 8629],
            [57400, 10115, 7679, 10115, 8641],
            [57450, 10128, 7686, 10128, 8654],
            [57500, 10140, 7694, 10140, 8666],
            [57550, 10153, 7701, 10153, 8679],
            [57600, 10165, 7709, 10165, 8691],
            [57650, 10178, 7716, 10178, 8704],
            [57700, 10190, 7724, 10190, 8716],
            [57750, 10203, 7731, 10203, 8729],
            [57800, 10215, 7739, 10215, 8741],
            [57850, 10228, 7746, 10228, 8754],
            [57900, 10240, 7754, 10240, 8766],
            [57950, 10253, 7761, 10253, 8779],
            [58000, 10265, 7769, 10265, 8791],
            ])

    def lookup(self, line43, status):

        

        x = self.table[:,0]
        
        print x

        print numpy.logical_not(x > line43)
        
        x1 = x[numpy.logical_not(x > line43)]

        print x1

        x2 = x1[-1]
        
        print x2

        i = numpy.where(x==x2)

        print i[0][0]

        print self.table[i]
        print self.table[i,status+1]
        print self.table[i,status+1][0][0]

        return self.table[i,status+1][0][0]

class Worksheet_6251(object):
    def fill(self, taxes):
        
        print "Worksheet 6251"

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
            print "you do not need to fill in Form 6251"
            return

        print "continue with worksheet"

        line10 = line8 - line9

        line11 = 159700

        if line8 > line11:
            line12 = line8 - line11
            line13 = min(line12 * 0.25, line9)
            line14 = line10 + line13
        else:
            line12 = 0
            line14 = line10

        print "line14",line14

        if line14 > 186300:
            print "you need to fill in Form 6251"
            return
        
        line15 = line14 * 0.26

        line16 = sum([
            taxes.form_1040.line44,
            taxes.form_1040.line46,
            ])
        
        print "line15",line15
        print "line16",line16

        if line15 > line16:
            print "you need to fill in Form 6251"
        else:
            print "you do not need to fill in Form 6251"

class Form_1040(object):
    def fill(self, taxes):
        
        taxes.form_1040_schedule_A = Form_1040_Schedule_A()

        # line 6
        line6d = taxes.form_1040_input()["line6d"]

        # line 7
        line7 = taxes.forms_W_2_box1()
  
        self.line10 = 0
        self.line21 = 0

        # line 22
        line22 = line7

        # line 36
        line36 = 0

        # line 37
        line37 = line22 - line36

        # line 38
        line38 = line37

        # fill schedule A
        taxes.form_1040_schedule_A.fill(taxes)
        
        # line 40
        line40 = taxes.form_1040_schedule_A.line29

        # line 41
        self.line41 = line38 - line40

        if line38 < 155650:
            line42 = 4050 * line6d

        line43 = max(self.line41 - line42, 0)

        tt = TaxTable2016()
        
        self.line44 = tt.lookup(line43, 1)

        self.line46 = 0

        # line 45
        worksheet_6251 = Worksheet_6251()
        worksheet_6251.fill(taxes)

        line47 = sum([
                self.line44,
                ])

        line55 = 0
        
        line56 = max(line47 - line55, 0)

        # line 63
        line63 = sum([
            line56,
            ])

        # payments
        line64 = taxes.form_totals("W-2", "box2")

        line74 = sum([
            line64,
            ])

        # line 75
        line75 = max(line74 - line63, 0)

        # print output

        print "line   7: {:16.2f}".format(line7)
        print "line  22: {:16.2f}".format(line22)
        print "line  36: {:16.2f}".format(line36)
        print "line  37: {:16.2f}".format(line37)
        print "line  38: {:16.2f}".format(line38)

        print
        print "schedule A"
        print "  line   5: {:16.2f}".format(taxes.form_1040_schedule_A.line5)
        print "  line   6: {:16.2f}".format(taxes.form_1040_schedule_A.line6)
        print "  line   9: {:16.2f}".format(taxes.form_1040_schedule_A.line9)
        print "  line  10: {:16.2f}".format(taxes.form_1040_schedule_A.line10)
        print "  line  13: {:16.2f}".format(taxes.form_1040_schedule_A.line13)
        print "  line  15: {:16.2f}".format(taxes.form_1040_schedule_A.line15)

        print "{:<32}{:16.2f}".format("line  40:", line40)
        print "{:<32}{:16.2f}".format("line  41:", self.line41)
        print "{:<32}{:16.2f}".format("line  43:", line43)
        print "{:<32}{:16.2f}".format("line  44:", self.line44)
        print "{:<32}{:16.2f}".format("line  47:", line47)
        print "{:<32}{:16.2f}".format("line  55:", line55)
        print "{:<32}{:16.2f}".format("line  56: line47 - line55", line56)
        print "{:<32}{:16.2f}".format("line  63: total tax", line63)
        print "{:<32}{:16.2f}".format("line  64:", line64)
        print "{:<32}{:16.2f}".format("line  74: payments", line74)
        print "{:<32}{:16.2f}".format("line  75:", line75)


class Form_1040_Schedule_A(object):
    def fill(self, taxes):
        
        # medical and dental expenses
        self.line4 = 0
        
        # income taxes paid
        self.line5 = taxes.forms_W_2_box17()
        
        # real estate taxes
        self.line6 = taxes.forms_1098_box10()

        self.line9 = self.line5 + self.line6

        # interest paid
        self.line10 = taxes.forms_1098_box1() + taxes.forms_1098_box6()

        self.line13 = taxes.forms_1098_box5()
       
        self.line15 = self.line10 + self.line13



        self.line29 = self.line4 + self.line9 + self.line15


class Taxes(object):
    forms_input = []
    def load_input(self, folder):

        for root, dirs, files in os.walk(folder):
            #print root, dirs, files
            
            for fn in files:
                #print fn
                #print os.path.join(root, fn)

                with open(os.path.join(root, fn), "r") as f:
                    form = json.loads(f.read())

                #print form

                self.forms_input.append(form)

    def forms_W_2_box1(self):
        return sum([form["box1"] for form in self.forms_W_2()])

    def forms_W_2_box17(self):
        return sum([form["box17"] for form in self.forms_W_2()])
    
    def forms_1098_box1(self):
        return sum([form["box1"] for form in self.forms_1098()])

    def forms_1098_box5(self):
        return sum([form["box5"] for form in self.forms_1098()])

    def forms_1098_box6(self):
        return sum([form["box6"] for form in self.forms_1098()])

    def forms_1098_box10(self):
        return sum([form["box10"] for form in self.forms_1098()])
    
    def form_totals(self, form, box):
        y = 0
        for f in self.forms_input:
            if f["form"] == form:
                y += f[box]
        return y
    def forms_W_2(self):
        for f in self.forms_input:
            if f["form"] == "W-2":
                yield f

    def forms_1098(self):
        for f in self.forms_input:
            if f["form"] == "1098":
                yield f

    def form_1040_input(self):
        form = None
        for f in self.forms_input:
            if f["form"] == "1040":
                if form is None:
                    form = f
                else:
                    raise Exception()

        return form
        
    def form_1040(self):

        self.form_1040 = Form_1040()

        self.form_1040.fill(self)









