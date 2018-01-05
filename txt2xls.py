import glob
import csv
import xlwt
import locale
import re

lang_code, encoding = locale.getdefaultlocale()

for filename in glob.glob("*.txt"):
    reader = csv.reader((open(filename, 'rb')), delimiter=' ', skipinitialspace=True, quotechar='"')
    wb = xlwt.Workbook(encoding=encoding)
    #sheet = xlwt.Workbook()
    sheet = wb.add_sheet('sheet_1')
    for rowx, row in enumerate(reader):
        for colx, value in enumerate(row):
            #print value, '\n'
            m = re.match(r"(-?\d+.?\d*)e[+-](\d+)", value)
            if m != None:
                exponent = int(m.group(2))
                number = float(m.group(1))
                value = number * (10 ** exponent)
            sheet.write(rowx, colx, value)
    wb.save(filename[:-4] + ".xls")
