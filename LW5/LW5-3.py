def main():
    count,index,su,mi = 0, 0, 0, lst[0]
    for i in lst:
        if i < 0:
            su += i
            count += 1
            if i < mi:
                mi = i
                mini = index
        index += 1
    arithmetic(su, count, mini)
    
def arithmetic(su, count, mini):
    arifm = su / count
    lst[mini] = arifm
    print(lst)

lst = [-10, -20, -30, -40, 1, -5, 5]
main()