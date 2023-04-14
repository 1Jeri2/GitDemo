#Any pytest file should start with test_ or end with test_
#should write the code in pytest standards i.e using functions
#test method names should always start with test_
#any codes should be wrapped in methods
#every method is treated as testcases
import pytest


def test_firstprogram():
    print("hello")

#to run the test file in pycharm
# ->edit configuration -> + -> python -> pytest -> give the script path C:\Users\hp\PycharmProjects\pythontesting\pythonbasics\demo.py

#to run in terminal
#pip install pytest
#-> C:\Users\hp\PycharmProjects\pythontesting\pytestsDemo ->py.test ->py.test -v (verbose) gives extra info
#run all the test files inside the pytestsDemo package
#-> C:\Users\hp\PycharmProjects\pythontesting\pytestsDemo>py.testpy -v -s - to print console logs

@pytest.mark.smoke
def test_secondCreditcard():
    print("hello world")

# in pytest method names should be different otherwise the second case overrides the first


def test_fixtureParametersTest(crossBrowser):
    print(crossBrowser[0])
    print(crossBrowser[1])
 #o/p picks the value of index of each brakctes
 #datadrivena and parameterization can be done by with return statements in tuple format