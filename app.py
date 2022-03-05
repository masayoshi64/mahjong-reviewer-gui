import os
import subprocess
import json

import eel


with open("setting.json", "r") as f:
    args = json.load(f)
PATH = args["haifu_path"]


@eel.expose
def analyze(file_name):
    subprocess.run(f"docker run -v {PATH}:/akochan-reviewer/haifu\
    akochan-reviewer:latest -i haifu/{file_name} -a 1 -k E1 --no-open \
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
