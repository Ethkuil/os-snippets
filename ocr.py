#!/usr/bin/env python

import sys
import tomllib
from pathlib import Path

from aip import AipOcr

# Overview: https://console.bce.baidu.com/ai/#/ai/ocr/overview/index
# SDK doc: https://ai.baidu.com/ai-doc/OCR/7kibizyfm
def create_client(config_file_path):
    script_dir = Path(__file__).resolve().parent
    abs_config_file_path = Path(config_file_path) if Path(config_file_path).is_absolute() else script_dir / config_file_path

    with open(abs_config_file_path, "rb") as f:
        data = tomllib.load(f)
    client = AipOcr(data["APP_ID"], data["API_KEY"], data["SECRET_KEY"])
    return client

def get_file_content(filePath):
  with open(filePath, "rb") as fp:
    return fp.read()

def extract_ans(ret):
    words_result = ret["words_result"]
    words_list = [result["words"] for result in words_result]
    words_string = "\n".join(words_list)
    return words_string

if __name__ == '__main__':
    client = create_client("ocr.toml")
    image = get_file_content(str(sys.argv[1]))
    options = {
        "language_type": "auto_detect"
    }

    ret = client.basicAccurate(image, options)

    print(extract_ans(ret))

