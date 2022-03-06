import os
import subprocess
import json

import eel

ESWN = "ESWN"
with open("setting.json", "r") as f:
    args = json.load(f)
PATH = args["haifu_path"]
USER_NAME = args["user_name"]


@eel.expose
def get_kyoku_names(file_name):
    with open(PATH + "/" + file_name, "r") as f:
        data = json.load(f)

    kyoku_names = []
    for kyoku in data["log"]:
        kaze = ESWN[(kyoku[0][0] + 1) // 4]
        kyokusu = (kyoku[0][0]) % 4 + 1
        honba = kyoku[0][1]
        kyoku_names.append(f"{kaze}{kyokusu}.{honba}")
    return kyoku_names


# todo: 南場に対応
@eel.expose
def analyze(file_name, kyoku_idx):
    with open(PATH + "/" + file_name, "r") as f:
        data = json.load(f)
    names = data["name"]
    try:
        user_idx = names.index(USER_NAME)
    except ValueError:
        user_idx = 0
    kyoku_name = get_kyoku_names(file_name)[kyoku_idx]

    subprocess.run(f"docker run -v {PATH}:/akochan-reviewer/haifu\
    akochan-reviewer:latest -i haifu/{file_name}\
    -a {user_idx} -k {kyoku_name} -n 0.1 --no-open \
    -o - > web/html/report.html", shell=True)

    eel.show("html/report.html")


@eel.expose
def get_file_names():
    file_names = [f for f in os.listdir(PATH)
                  if len(f) > 4 and f[-4:] == "json"]
    return file_names


def main():
    eel.init("web")
    eel.start("html/index.html")


if __name__ == "__main__":
    main()
