import sys
import unittest

for path in ['./test/', './utils/']:
    sys.path.append(path)


def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'test':
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'DataRequestsSuite':
            from DataRequestsSuite import DataRequestsSuite
            getAndTest(DataRequestsSuite)
        elif argv[1] == 'ManagePoliciesSuite':
            from ManagePoliciesSuite import ManagePoliciesSuite
            getAndTest(ManagePoliciesSuite)
        else:
            printUsage()
    else:
        printUsage()


def getAndTest(cls): 
    suite = unittest.makeSuite(cls)
    test(suite)


def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())


def printUsage():
    print("py run.py test DataRequestsSuite")
    print("py run.py test ManagePoliciesSuite")


if __name__ == '__main__':
    main(sys.argv[1:])