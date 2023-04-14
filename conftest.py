import pytest

#if multiple test files require same fixture setup operation we can define the method in conftest.py
@pytest.fixture(scope="class")
def setup():
    print("I'll be executing first")
    yield
    print("I'll be executing last") #executes after the testcases ran

@pytest.fixture(scope="class")
def dataLoad():
    print("datas")
    return["jerin","lincy"] #tupple

#@pytest.fixture(params =["Chrome","Firefox","IE"])
#def crossBrowser(request):
    #request.param

#passing multiple datas it should be wrapped inside bracket and seperated by comma
#here the test ran 3 times
@pytest.fixture(params=[("chrome", "AA", "BB"), ("firefox", "CC")])
def crossBrowser(request):
    return request.param
