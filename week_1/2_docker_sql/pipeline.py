import sys
import pandas as pd

def main():
    print("start func main")
    print("---------------")
    print("print arguments")
    print(sys.argv)
    print("read 2nd argument")
    day = sys.argv[1]
    print(f'the 2nd argument from a command line: {day}')
    print('script succesfully executed')

if __name__ == '__main__':
    main()

