import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0]) #these logs are generated in reports
        log.info(dataLoad[1])
        print(dataLoad[1]) #these logs are not generated in reports
#if we are returning any data from fixtures then the argument of the fixture should be passed to the method
#if no data is returning argument need not be returned



#params are data, request is a object,instance of fixture to get param
