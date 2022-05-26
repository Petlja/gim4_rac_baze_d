import sys
import random
import datetime

def random_date(start, end):
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

with open('muska_imena.txt') as f:
    muska_imena = f.readlines()
muska_imena = [ime.strip() for ime in muska_imena]

with open('zenska_imena.txt') as f:
    zenska_imena = f.readlines()
zenska_imena = [ime.strip() for ime in zenska_imena]

with open('prezimena.txt') as f:
    prezimena = f.readlines()
prezimena = [prezime.strip() for prezime in prezimena]

for i in range(random.randint(25, 30)):
    if random.randint(0, 1) == 0:
        pol = 'м'
        ime = random.choice(muska_imena)
    else:
        pol = 'ж'
        ime = random.choice(zenska_imena)
        
    print("INSERT INTO ucenik (ime, prezime, pol, datum_rodjenja, razred, odeljenje) VALUES ('{}', '{}', '{}', '{}', 4, 3);".format(ime, random.choice(prezimena), pol, random_date(datetime.date(2003, 3, 1), datetime.date(2004, 3, 1))))
