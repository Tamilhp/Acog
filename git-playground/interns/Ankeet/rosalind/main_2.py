import stronghold.stronghold_8 as soln
import sys

def main():
    n, k = int(sys.argv[1]), int(sys.argv[2])
    for x in soln.__all__:
	    print(x(n, k))

if __name__ == "__main__":
    main()
