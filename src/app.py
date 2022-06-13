import sys
import os


def prime(s):
    
    for num in range(2, s//2):
        if s > 1:
            if s == 2:
                print(f"{s} is a prime number")
                return True
            elif s % num == 0:
                print(f"{s} is not a prime number")
                return False
            else:
                print(f"{s} is a prime number")
                return True
        print(f"{s} is not a prime number")

def solution(s):
    return prime(s)



if __name__ == "__main__":
    if len(sys.argv) < 1:
        sys.exit(os.error("Argument required"))

    print(solution(int(sys.argv[1])))
