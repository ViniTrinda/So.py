def fat(n):
    if n > 1:
        return n*fat(n-1)
    else:
        return n

def div(x):
    res = 1
    
    for i in range(x):
        res = res + 1/(fat(i+1))
        
    return res

def main():
    num = int(input())
    
    res = div(num)
    
    # print(fat(num))
    print(f"Aproximadamente: {res:.2f}")


if __name__ == '__main__':
    main()