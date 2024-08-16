import pytest
import requests

class TestFlask:
    
    
    def test_if_flask_is_installed(self):


        request = requests.get('https://localhost:5000/ping', verify=False)
        print(request)


    def test_if_sql_alchemy_extension_is_installed(self):
        pass





if __name__ == "__main__":
    test = TestFlask()
    test.test_if_flask_is_installed()