if __name__ == '__main__':
    N = int(input())

    lis = []

    for i in range(N):
        a = []
        b = input().split()
        a.append(b)
        if a[0] == 'insert':
            lis.insert(a[2], a[1])
        
        elif a[0] == 'print':
            print(lis)
        
        elif a[0] == 'remove':
            lis.remove(a[1])

        elif a[0] == 'append':
            lis.append(a[1])

        elif a[0] == 'sort':
            lis.sort()

        elif a[0] == 'pop':
            lis.pop()

        else:
            lis.reverse()