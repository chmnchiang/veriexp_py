#!/usr/bin/env python3

from os import listdir
from os.path import join as pjoin, isdir, isfile
import subprocess
from termcolor import colored

tests_path = 'tests'
def run_test(tc):
    path = pjoin(tests_path, tc)

    def file_ends_with(f, s):
        return f.endswith(s) and isfile(f)

    vers = [v for v in listdir(path)
            if file_ends_with(pjoin(path, v), '.ver')]

    for v in vers:
        with open(pjoin(path, v[:-2]), 'w') as fw:
            subprocess.run(['./veriexp.py', pjoin(path, v)],
                           stdout=fw, check=True)

    verilogs = [pjoin(path, v) for v in listdir(path)
            if v[-2:] == '.v' and isfile(pjoin(path, v))]
    subprocess.run(['iverilog', '-o', pjoin(path, 'tb'), *verilogs], check=True)
    res = subprocess.run(['vvp', pjoin(path, 'tb')],
                         stdout=subprocess.PIPE, check=True)
    return 'err' not in res.stdout.decode().lower()

def run_all_test():
    all_tests = [t for t in listdir(tests_path)
                 if isdir(pjoin(tests_path, t))]

    T = 0
    P = 0
    for tc in all_tests:
        res = run_test(tc)
        T += 1
        print('Test #%d, %s:' % (T, tc), end=' ')
        if res:
            print(colored('[PASSED]', 'green'))
            P += 1
        else:
            print(colored('[FAILED]', 'red'))
    print('Total = %d, Passed = %d' % (T, P))




if __name__ == '__main__':
    run_all_test()
