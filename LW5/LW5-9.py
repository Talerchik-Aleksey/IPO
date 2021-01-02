def remove_space(text):
    for i in text: #remove space
        if i == ' ':
            text.remove(i)
    main(text)
        
def main(text):
    if text[:int((len(text)/2))] == list(reversed(text[int((len(text)/2)):])):
        print('Yes')
    else:
        print('No')

text = list(input('Enter list: '))
remove_space(text)
