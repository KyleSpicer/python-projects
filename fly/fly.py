#!/usr/bin/env python3

'''Function prints through list of animals and phrases to create poem'''

import sys


def poetic(person):

    animals = ['fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse']

    phrases = ["I don't know why she swallowed a fly - Perhaps she'll die!",
               'That wriggled and jiggled and tickled inside her!',
               'How absurd to swallow a bird!',
               'Imagine that! She swallowed a cat!',
               'She was a hog, to swallow a dog!',
               'She just opened her throat and swallowed a goat!',
               "I don't know how she swallowed a cow!",
               "...She's dead, of course!"]

    sentence = []  # list to store unique sentences from each loop

    for index, animal in enumerate(animals):
        print(f'There was an old {person} who swallowed a {animal};')
        if index > 0:
            print(phrases[index])

        if index in range(1, 7):
            sentence.append(f'She swallowed the {animal} to catch \
the {animals[index-1]}.')
            print("\n".join(sentence[index::-1]))

        if index < 7:
            print(phrases[0])

        print()


def main(person='lady'):
    poetic(person)

if __name__ == '__main__':
    if len(sys.argv) > 1:
       main(sys.argv[1])
    else:
        main()
