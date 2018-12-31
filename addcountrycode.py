import csv

"""
Convert phone number data to international format.
"""

# Should: Read csv with 2 colums data (country code & phone number)
with open('input.csv') as inf:
    reader = csv.reader(inf.readlines())

# Should: Check phone number start with '0' and save it somewhere.

# Should: Check phone number not start with '0' and save it somewhere.

# Should: Check if phone number not start with '0' is less then X character and save it somewhere.

# Should: add country code.

# Should: write formated data to new file.
with open('output.csv', 'w', newline='') as outf:
    writer = csv.writer(outf)
    for line in reader:
        # replace '0' with  '62' / !!! Perlu cara skip raw kosong !!!
        if line[0][0] == '0':
            nomor_reseller = list(line[0])
            nomor_reseller[0] = '62'
            nomor_reseller = ''.join(nomor_reseller)
            writer.writerow([nomor_reseller])
            print(nomor_reseller)
                
        else:
            nomor_luar = line[0]
            writer.writerow([nomor_luar])
            print(nomor_luar)
