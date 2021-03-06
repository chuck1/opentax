import argparse
import opentax
import opentax.tables

parser = argparse.ArgumentParser()
parser.add_argument("folder")
args = parser.parse_args()

taxes = opentax.Taxes()
taxes.tax_table = opentax.tables.TaxTable2017()

taxes.load_input(args.folder)

taxes.form_1040().fill(taxes)

taxes.form_OR_40()

for f in taxes.forms_W_2.forms:
    print()
    print(f.filename)
    print('--------------------------------------------------------------------')
    f.print_lines(["1", "2", "17"])

