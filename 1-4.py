n=74853
i=0
while n > 0:
    last = n % 10
    print("последняя цифра", last)
    if last > i :
        i = last
        n = n //10
        print(i,"самая большая цифра")