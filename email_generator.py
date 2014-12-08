__author__ = 'dmitryb'

'''
1. make a loop
2. generate a local-part (use binascii)= name
3. add "@" simbol and domain. exmpl: '@blahblah.ks'
4. save it in csv file
'''

import os, binascii
import csv
import traceback

name = binascii.b2a_hex(os.urandom(6))
e_domain = name + '@blahblah.ks'

def main():

    emailGenerator = email()
    emailGenerator.e_generator()
    print('Done!')

class email():

    def e_generator(self):
        try:
            with open('//Users/dmitryboyko/Documents/workspace/Python/emails.csv', 'w') as f:
                a = csv.writer(f, delimiter=';')
                for name_index in range(0, 101):
                    e_mail = [ str(name_index) + e_domain]
                    #e_mail = [str(name_index+1), str(name_index) + e_domain] # generate with line numbers if need
                    a.writerow(e_mail)
        except:
            traceback.print_exc()

if __name__ == "__main__":
    main()
