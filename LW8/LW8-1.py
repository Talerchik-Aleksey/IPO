text = {}
for i in range(int(input('Enter number of line: '))):
    line = input().split()
    for word in line:
        text[word] = text.get(word, 0) + 1

max_count = max(text.values())
most_frequent = [k for k, v in text.items() if v == max_count]
print(min(most_frequent))
