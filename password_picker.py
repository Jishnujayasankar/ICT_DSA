import random
import string

adjectives=['fat','good','bad','awsome','nicer','indian','favorite','taller','worse']
nouns=['Man','Women','Skate','Cuckoo','Elephant','Shirt','Dog','Rat','Red',
        'Book','Cap','Key','Cricket','Hair','Calculator','Diary','Fan','Box',
        'Basket','Tile','Mask','Phone','Computer']

adj=random.choice(adjectives)
noun=random.choice(nouns)
dig=random.randrange(0,101)
pun=random.choice(string.punctuation)

password=adj+noun+str(dig)+pun
print("Your Password is:",password)