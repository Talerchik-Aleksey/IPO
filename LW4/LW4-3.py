st = input('Enter st: ')

print(st[:st.find('h')] + st[st.rfind('h') + 1:])
