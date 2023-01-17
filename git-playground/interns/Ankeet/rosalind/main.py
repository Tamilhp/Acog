import stronghold.stronghold_1 as soln

def main():
    f = open('file.txt', 'r')
    needed_str = f.read()
    for x in soln.__all__:
	    x(needed_str.rstrip())

if __name__ == "__main__":
    main()
