import sys

def get_traps(filename):
    arch = open(filename, "r")
    for line in arch:
        line = line.strip().split(" ")
        if len(line) == 2:
            n = line[0]
            s = line[1]
        else:
            tup = (s,line)
            return tup

def main():
    s, array = get_traps(sys.argv[1])

if __name__=="__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("=== ERROR ===")
        print("Argumentos de programa insuficientes.")
        print("Programa finalizado.")
