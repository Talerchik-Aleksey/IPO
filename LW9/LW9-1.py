def main():    
    for i in range(int(input('Enter step: ')) + 1):
        print(i, ':', shift([1, 2, 3, 4, 5], i))
def shift(s, n):
    n = n % len(s)
    # 10 % 5 = 0
    # 6 % 5 = 1
    # 3 % 5 = 3
    
    return s[n:] + s[:n]

main()

