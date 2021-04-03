import os
import hashlib
import requests

def verify():
    baseUrl = "https://download.jetbrains.com/"
    testFilePath = input("输入要计算的文件路径")
    testFileName = os.path.split(testFilePath)[1]
    print(testFileName)

    def ub1():
        return baseUrl + "webstorm" + "/" + testFileName + ".sha256"

    def ub2():
        return baseUrl + "idea" + "/" + testFileName + ".sha256"

    def ub3():
        return baseUrl + "python" + "/" + testFileName + ".sha256"

    def ub4():
        return baseUrl + "cpp" + "/" + testFileName + ".sha256"

    IDENameList = {"w": ub1,
                   "i": ub2,
                   "p": ub3,
                   "c": ub4,
                   }
    localsha256Code = hashlib.sha256(open(testFilePath, 'rb').read()).hexdigest()
    print(localsha256Code)
    # url = "https://download.jetbrains.com/webstorm/WebStorm-2020.3.3.tar.gz.sha256"
    url = IDENameList.get(testFileName[0:1].lower())()
    print(url)
    res = requests.get(url)
    resultContent = res.text
    # print(resultContent)
    sha256Code = resultContent.split(" ")[0]
    print(sha256Code)
    if localsha256Code == sha256Code:
        print("文件一致")

if __name__ == '__main__':
    verify()