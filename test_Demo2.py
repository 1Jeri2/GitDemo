import pytest

#you can mark (tag) tests with @pytest.mark.smoke and run with -m
#to skip test @pytest.mark.skip
@pytest.mark.smoke
@pytest.mark.skip #to skip testcases
def test_firstprogram():
    msg = "helo"
    assert msg == "hi","test failed"

#it will run but no reports will be shown wheter pas/fail
#used in cases where the info in this test case is required for other test cases
@pytest.mark.xfail
def test_CreditCardtprogram():
        a=4
        b=6
        assert a+2==6, "test failed"

#to run a single file inside the package
#-> C:\Users\hp\PycharmProjects\pythontesting\pytestsDemo>py.test test_Demo2.py -v -s

#To run test cases based on sepecific names for eg: all test cases related to credit card
#->C:\Users\hp\PycharmProjects\pythontesting\pytestsDemo>py.test -k creditcard -v -s
#-k stands for method names execution, -v for more info metadata, -s for logs


