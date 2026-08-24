import random

##arpoo kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9
kolmenumeroisen_koodi = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))

##arpoo nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6
nelinumeroisen_koodi = str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6))


##tulostaa kolmenumeroisen koodin ja nelinumeroisen koodin
print(f"Kolmenumeroisen koodin on: {kolmenumeroisen_koodi}")
print(f"Nelinumeroisen koodin on: {nelinumeroisen_koodi}")
