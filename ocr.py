#!/usr/bin/env python
import sys
import tomllib

from aip import AipOcr

# Overview: https://console.bce.baidu.com/ai/#/ai/ocr/overview/index
# SDK doc: https://ai.baidu.com/ai-doc/OCR/7kibizyfm
with open("ocr.toml", "rb") as f:
    data = tomllib.load(f)
client = AipOcr(data["APP_ID"], data["API_KEY"], data["SECRET_KEY"])

def get_file_content(filePath):
  with open(filePath, "rb") as fp:
    return fp.read()
image = get_file_content(str(sys.argv[1]))

options = {
    "language_type": "auto_detect"
}
ret = client.basicAccurate(image, options)

words_result = ret["words_result"]
words_list = [result["words"] for result in words_result]
words_string = "\n".join(words_list)
print(words_string)

