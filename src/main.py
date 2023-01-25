flag_data_exist=False

import os
import requests

def download_data(version:str,endpoint="jsdeliver")->str:
    PACKAGE_NAME="name-suggestion-index"
    FILE_PATH="/dist/nsi.min.json"
    root_path=""

    endpoint_list={
        "jsdeliver":"https://cdn.jsdelivr.net/npm/",
        "unpkg":"https://unpkg.com/"
    }
    
    def url_gen(endpoint:str, version:str)->str:
        return endpoint_list[endpoint]+PACKAGE_NAME+"@"+version+FILE_PATH
    
    min_json_file=open("nsi.min.json","w",encoding="utf-8")
    min_json_file.write(requests.get(url=url_gen(endpoint=endpoint,version=version)).text)

    return root_path

def main():
    if flag_data_exist != True:
        download_data("latest")
    exit()

if __name__ == "__main__":
    main()