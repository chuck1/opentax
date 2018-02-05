#!/usr/bin/env python3

import argparse
import opentax

parser = argparse.ArgumentParser()
parser.add_argument("folder")
args = parser.parse_args()

taxes = opentax.Taxes()
taxes.load_input(args.folder)

taxes.form_1040().fill(taxes)

taxes.form_OR_40()

