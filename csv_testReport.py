import csv
import sys

def csv_File():
    with open('test_report.scv', 'w') as csvfile:
        test_writer = csv.DictWriter(csvfile, delimiter = ',')
        test_writer.writerow(['Test Case'] + ['Result'])
