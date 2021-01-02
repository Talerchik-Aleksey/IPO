st = input()

NewSt = st[st.find(' ') + 1:]+ ' ' + st[:st.find(' ')]

print(NewSt)
