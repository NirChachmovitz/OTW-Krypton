from __future__ import division
import sys

if __name__ == '__main__':
    letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    frequencies = []
    with open(sys.argv[1], 'r') as file:
        content = file.read()
        file_size = len(content)
        frequencies = [(content.count(letter) / file_size) for letter in letters]
    hist = list(zip(letters, frequencies))
    result = sorted(hist, key=lambda x: x[1])[::-1]
    for letter_frequency in result:
        print(letter_frequency[0] + ' - ' + "{:.2%}".format(letter_frequency[1]))



