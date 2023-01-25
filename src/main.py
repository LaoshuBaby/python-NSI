import os

import requests

flag_data_exist = True


def download_data(
    root_path: str, version="latest", endpoint="jsdeliver"
) -> str:
    PACKAGE_NAME = "name-suggestion-index"
    FILE_PATH = "/dist/nsi.min.json"

    endpoint_list = {
        "jsdeliver": "https://cdn.jsdelivr.net/npm/",
        "unpkg": "https://unpkg.com/",
    }

    def url_gen(endpoint: str, version: str) -> str:
        return (
            endpoint_list[endpoint] + PACKAGE_NAME + "@" + version + FILE_PATH
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


def main():
    root_path = os.path.join(os.getcwd(), "..", "data", "nsi.min.json")
    if os.path.exists(root_path) != True:
        flag_data_exist = False
    if flag_data_exist != True:
        download_data(root_path)
    exit()


if __name__ == "__main__":
    main()
