#!/usr/bin/python3
import psutil as ps
from sys import argv
if __name__ == '__main__':
        while argv[1:]:
            try:
                print(ps.Process(int(argv[1])).get_cpu_percent(interval=1), end='\r')
            except KeyboardInterrupt:
                print('\n')
                break
