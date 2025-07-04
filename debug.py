import datetime
s = "2023年8月4日"
print(datetime.datetime.strptime(s, "%Y年%m月%d日"))