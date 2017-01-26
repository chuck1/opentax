#!/usr/bin/env python

import argparse
import opentax

parser = argparse.ArgumentParser()
parser.add_argument("folder")
args = parser.parse_args()

taxes = opentax.Taxes()
taxes.load_input(args.folder)

