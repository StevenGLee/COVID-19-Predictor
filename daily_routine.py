import csv
import os
import shutil
from urllib.request import urlretrieve

import numpy

if os.path.exists("./data") :
    shutil.rmtree("./data")
os.mkdir("./data",0o777)
urlretrieve("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv", './data/confirmed.csv')
urlretrieve("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv", './data/deaths.csv')
urlretrieve("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv", './data/recovered.csv')

cases = [
    ("./data/confirmed.csv", "./data/confirmed_60_days_china_detailed.csv", "./data/confirmed_60_days_china_total.csv"),
    ("./data/deaths.csv", "./data/deaths_60_days_china_detailed.csv", "./data/deaths_60_days_china_total.csv"),
    ("./data/recovered.csv", "./data/recovered_60_days_china_detailed.csv", "./data/recovered_60_days_china_total.csv"),
]
for files in cases:
    input_csv = csv.reader(open(files[0], 'r'))
    output_csv = csv.writer(open(files[1],'w'))
    data_total=numpy.array([0]*60)
    for row in input_csv:
        if row[1] == "China" or row[1] == "Country/Region":
            data_line=list()
            start_col = len(row) - 60
            data_line[0:2] = row[0:2]
            data_line[2:62] = row[start_col:start_col+60]
            output_csv.writerow(data_line)
            if row[1] == "China":
                data_total += numpy.array([int(x) for x in row[start_col:start_col+60]])
                print(data_total)
    output_csv = csv.writer(open(files[2],'w'))
    output_csv.writerow(data_total)
