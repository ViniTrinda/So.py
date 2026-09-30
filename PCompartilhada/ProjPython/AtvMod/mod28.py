def calc(venM, precA):
    if (venM < 500) and (precA < 30):
        perc = 10
    elif (venM >= 500 and venM < 1000) and (precA >= 30 and precA < 80 ):
        perc = 15
    else:
        perc = -5
        
    precN = precA * ((perc + 100)/100)
    print(f"{precN:.2f}")
    
def main():
    venm = int(input())
    precA = int(input())
    
    calc(venm, precA)
    
    
if __name__ == '__main__':
    main()