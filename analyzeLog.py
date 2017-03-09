#coding=utf-8
import os;
import sys;
import re;

argvs = sys.argv;

if len(argvs) >= 2:
    filename = argvs[1];
    print(filename)
else:
    print("请设置需要分析的文件");
    os._exit(1);

if not os.path.isfile(filename):
    print("文件不存在，请重新设置");
    os._exit(1);

if os.stat(filename).st_size == 0:
    print("文件内容为空，请重新设置");
    os._exit(1);

totalLine = 0;
ips = {};
handle = open(filename, 'r');
while True:
    line = handle.readline();
    if not line:
        break;
    # lineContent = line.split(" ");
    # if lineContent[0] not in ips.keys():
    #     ips[lineContent[0]] = 0;
    # else:
    #     ips[lineContent[0]] += 1;
    # print(lineContent);
    regexResult = re.search(r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) (.*?) (.*?) (\[.*\]) (.*) ([0-9]+) ([0-9]+)", line, re.MULTILINE);
    if regexResult:
        print(regexResult.group(1), regexResult.group(4), regexResult.group(5), regexResult.group(6), regexResult.group(7));
    totalLine+=1;

print(totalLine, ips);