#if single file contains multiple test cases it's not necassary to run fixture evrytime
#instead wrap it in the class and call the scope = class in fixture
import pytest


@pytest.mark.usefixtures("setup")
class Testexample:
    def test_firstfixture1(self): # first setup will run before this test case executes
        print("i'll be executing the methods in this method")


    def test_firstfixture2(self): #first setup will run before this test case executes
        print("i'll be executing the methods in this method")


    def test_firstfixture3(self): #first setup will run before this test case executes
        print("i'll be executing the methods in this method")