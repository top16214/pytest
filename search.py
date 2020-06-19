import re 
# 　　正则表达式是极其强大的，利用正则表达式来提取想要的内容是很方便的事。 
# 下面演示了在python里，通过正则表达式来提取符合要求的内容。有几个要注意 
# 的地方就是： 
# [1] 要用()将需要的内容包含起来 
# [2] 编号为0的group是整个符合正则表达式的内容，编号为1的是第一个(及对应 
#   的)包含的内容 
# @param regex: regular expression, use () to group the result 
#   正则表达式，用()将要提取的内容包含起来 
# @param content:  
# @param index: start from 1, depends on the \p regex's () 
#   从1开始，可以通过数(来得到，其中0是全部匹配 
# @return: the first match of the \p regex 
#   只返回第一次匹配的内容 
def extractData(regex, content, index=1): 
  r = '0'
  p = re.compile(regex) 
  m = p.search(content) 
  if m: 
    r = m.group(index) 
  return r 
  
regex = r'第(.*)场雪'
content = '2002年的第一场雪'
index = 1
print(extractData(regex, content, index))
