#!/usr/bin/env python
"""
Run all files in Test, and indicate if the output is correct (0 expected)
"""
import subprocess as sp
import os
import os.path as osp
import Colors
TEST_PATH = "Tests/testSource/"
OK =  b'0\n'

def getTestFiles():
    testFiles = [TEST_PATH+f for f in os.listdir(TEST_PATH) if osp.isfile(osp.join(TEST_PATH, f))]
    res = []
    for file in testFiles:
        if len(file) > 4 and file[-1] == 'y' and file[-2] == 'p' and file[-3] == '.' and file != "Tests/testSource/__init__.py":
            res.append(file)
    return res

def setSpace(fileName):
    space = ""
    for _ in range(50 - len(fileName)):
        space += " "
    return space

def testRunner():
    testFiles = getTestFiles()
    allgood = True
    # run python files
    for testFile in testFiles:
        print(Colors.Colors.BOLD + 'Tested file : "' + Colors.Colors.ENDC + testFile +Colors.Colors.BOLD + '"' + Colors.Colors.ENDC+ setSpace(testFile), end='')
        result = sp.check_output(
            ['python', testFile],  # program and arguments
        )
        if result == OK:
            print(Colors.Colors.OKGREEN + "SUCCESSFULL RESULT" + Colors.Colors.ENDC)
        else:
            print(Colors.Colors.FAIL + "FAILURE" + Colors.Colors.ENDC)
            allgood = False
    if allgood:
        print(Colors.Colors.OKBLUE + "All php tests passed" + Colors.Colors.ENDC)
    else:
        print(Colors.Colors.FAIL + "Go fix the code" + Colors.Colors.ENDC)
    # run python test
    #for file in getTestPython():
    #   res = os.system("python3 " + file)


testRunner()