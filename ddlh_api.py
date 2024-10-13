import os, pathlib, requests, yaml, json, pprint
from requests.auth import AuthBase
from yaml import Loader

configFile = os.path.join(pathlib.Path(__file__).resolve().parent, "config.yaml")

with open(file = configFile, mode="r") as file:
    config = yaml.load(stream=file, Loader=Loader)

print(config)

class BearerAuth(AuthBase):
    
    def __init__(self, access_token = None):
        self.access_token = access_token if access_token else None

    def __call__(self, request):
        request.headers["Authorization"] = "Bearer " + self.access_token
        return request


class ApiClient(object):

    def __init__(self, config = config):

        self.config = config
        self.baseUrl = fr'https://{config["ddlhHost"]}/rest/v1'
        self.tokenUrl = fr'https://{config["ddlhHost"]}/auth/realms/ddae/protocol/openid-connect/token'
        self.session = requests.Session()
        self.session.verify = False

    def get_token(self):

        _headers = {"Content-Type": "application/x-www-form-urlencoded"}

        _data = {
            "client_id": self.config["client_id"],
            "client_secret": self.config["client_secret"],
            "grant_type": "password",
            "scope": "openid",
            "username": self.config["username"],
            "password": self.config["password"]
        }

        try:
            _response = self.session.post(url = self.tokenUrl, data = _data, headers = _headers)
            _response.raise_for_status()
        except Exception as err:
            print(err)

        if _response.ok:
            _responseJson = json.loads(_response.content)
            self.accessToken = _responseJson["access_token"]
            print(f"Access token for user {self.config["username"]} has been acquired.")

        else:
            print(f"Access token for user {self.config["username"]} could not been acquired!")
            self.accessToken = None

    def get_catalogs(self):

        _url = self.baseUrl + "/catalogs"
        print(_url)

        try:
            _response = self.session.get(url = _url, auth = BearerAuth(self.accessToken))
            _response.raise_for_status()

        except Exception as err:
            print("Exception occured!")
            print(err)

        if _response.ok:
            _responseJson = json.loads(_response.content)
            pprint.pprint(_responseJson, indent=1)
        else:
            print(f"Catalog list could not been acquired!")


if __name__ == "__main__":

    apiClient = ApiClient(config = config)
    apiClient.get_token()
    apiClient.get_catalogs()


