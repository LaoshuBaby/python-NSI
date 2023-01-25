flag_data_exist=False

import os

def download_data(version:str)->str:
    root_path=os.getcwd() # should be path of `index.mjs`

    version="latest"
    endpoint="npmjs" # npmjs/jsdeliver/unpkg/etc.

    server=""
    url="" # should be gen by server and package name

    url="https://registry.npmjs.org/name-suggestion-index/-/name-suggestion-index-6.0.20230123.tgz"
    # unzip this tgz file should use which lib?
    

    return root_path

def main():
    if flag_data_exist != True:
        download_data("latest")
    exit()

if __name__ == "__main__":
    main()