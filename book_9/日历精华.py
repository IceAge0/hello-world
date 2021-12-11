from datetime import date,datetime
evevt_date=datetime.strptime('01/02/20','%d/%m/%y').date()
print(evevt_date)
#用来把字符串转化为日期类型
line='abcdefg'
line=line.rstrip('g')
print(line)
#用来删除，    '\n'用来删除换行符
