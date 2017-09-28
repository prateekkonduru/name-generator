import string, random

vowels='aeiou'
consonants='bcdfghjklmnpqrstvwxyz'
letters=vowels+consonants

m=int(input("How many names do you need: "))
n=int(input("How many letters do you want in your name: "))

lst = []

def name():
    if letter_input == 'v':
        l1=random.choice(vowels)
        (lst.append(l1))
    elif letter_input == 'c':
        l1=random.choice(consonants)
        (lst.append(l1))
    elif letter_input == 'l':
        l1=random.choice(letters)
        (lst.append(l1))
    else:
        l1=letter_input
        lst.append(l1)

i=0
while i!=n:
    letter_input=input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
    name()
    i=i+1

name = "".join(lst)
print(name)
