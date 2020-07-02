import os

import pytest
import requests
import yaml

from utils.commonlib import get_test_data

cases, list_params = get_test_data("data/test_in_theaters.yaml")
# list_params=list(parameters)

class TestInTheaters(object):
    @pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
    def test_in_theaters(self,case,env,http,expected):
        r = requests.request(http["method"],
                             url=env["host"]["douban"] + http["path"],
                             headers=http["headers"],
                             params=http["params"])
        response = r.json()
        assert response["count"] == expected['response']["count"]
        assert response["start"] == expected['response']["start"]
        assert response["title"] == expected['response']["title"], "实际的标题是：{}".format(response["title"])