from random import randint

def generate(n):
    sequence = list()
    i        = 0
    while i < n:
        number = randint(1,30)
        sequence.append(number)
        i += 1
    return sequence        

def main():
    i = randint(1,10)
    j = 0
    arch = open("input.txt","w")
    while j < i: 
        n    = randint(1,10)
        arch.write(str(n))
        arr  = generate(n)
        for number in arr:
            arch.write(" "+str(number))
        arch.write("\n")
        j += 1
    arch.close()        

if __name__=="__main__":
    main()
