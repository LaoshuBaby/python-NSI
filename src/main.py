import json
import os

import requests


class NSI:
    def __init__(self):
        root_path = os.path.join(os.getcwd(), "..", "data", "nsi.min.json")
        flag_data_exist = True
        if os.path.exists(root_path) != True:
            flag_data_exist = False
        if flag_data_exist != True:
            self.download_data(root_path)
        min_json = json.loads(open(root_path, "r", encoding="utf-8").read())
        self.meta = min_json["_meta"]
        self.nsi = min_json["nsi"]

    def download_data(
        self, root_path: str, version="latest", endpoint="jsdeliver"
    ) -> str:
        PACKAGE_NAME = "name-suggestion-index"
        FILE_PATH = "/dist/nsi.min.json"

        endpoint_list = {
            "jsdeliver": "https://cdn.jsdelivr.net/npm/",
            "unpkg": "https://unpkg.com/",
        }

        def url_gen(endpoint: str, version: str) -> str:
            return (
                endpoint_list[endpoint]
                + PACKAGE_NAME
                + "@"
                + version
                + FILE_PATH
            )

        if os.path.exists(os.path.join(os.getcwd(), "..", "data")) != True:
            os.mkdir(os.path.join(os.getcwd(), "..", "data"))
            min_json_file = open(
                file=root_path,
                mode="w",
                encoding="utf-8",
            )
            min_json_file.write(
                requests.get(
                    url=url_gen(endpoint=endpoint, version=version),
                    headers={"User-Agent": "python-NSI/0.0.1"},
                ).text
            )
            min_json_file.close()
        return root_path

    def get_meta(self, output=True):
        if output==True:
            from pprint import pprint
            pprint(self.meta)
        return self.meta

    def get_catagory(self, output=True):
        catagory_list=[]
        for key in self.nsi:
            catagory_len=len(self.nsi[key])
            catagory_list.append((key,catagory_len))
        if output==True:
            from pprint import pprint
            pprint(catagory_list)
        return catagory_list

    def get_catagory_key(self, output=True):
        catagory_key_list=[]
        for key in self.nsi:
            catagory_key_list.append(key)
        if output == True:
            from pprint import pprint
            pprint(catagory_key_list)
        return catagory_key_list



    def get_catagory_num(self, output=False):
        catagory_num=len(self.get_catagory_key(output=False))
        if output==True:
            print(catagory_num)
        return catagory_num


if __name__ == "__main__":
    data = NSI()
    data.get_meta()
    data.get_catagory()
    print(data.get_catagory_num())