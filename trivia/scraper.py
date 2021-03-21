import requests

BASE_URL = "https://opentdb.com/api.php"


def _get_json(params: dict) -> requests.Response:
    if params["difficulty"] == "any":
        params.pop("difficulty")

    request = requests.get(BASE_URL, params=params).json()
    return request
