import os
import time

'''
def gcd(x, y):
    x, y = y, x if x > y else x, y
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)
'''

'''
show running lights
'''


def main():
    content = "welcome to beijing..."
    while True:
        os.system('clear')
        print(content)
        time.sleep(200)
        content = content[1:] + content[0]


if __name__ == "__main__":
    main()
