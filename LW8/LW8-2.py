from collections import Counter # https://pythonworld.ru/moduli/modul-collections.html
 
words = []
for i in range(int(input())):
    words.extend(input().split())
 
counter = Counter(words) # Counter({'dfd': 2, 'dsf': 2, 'wer': 2, 'yuthn': 1, 'dfg': 1, 'ewrgu': 1, 'wqert': 1})
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()] # [(-2, 'dfd'), (-2, 'dsf'), (-2, 'wer'), (-1, 'yuthn'), (-1, 'dfg'), (-1, 'ewrgu'), (-1, 'wqert')]
words = [pair[1] for pair in sorted(pairs)]
print(words)
print('\n'.join(words))

"""

                    dfd
                    dsf
                    wer
words ==>           dfg
                    ewrgu
                    wqert
                    yuthn

"""