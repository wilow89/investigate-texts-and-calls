"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


"""
I have several methods on this situation, and I decide use the last method that I think is more easier.
"""

"""
first method test:
firsttext = texts[0]
print("First record of texts, {} texts {} at time {}".format(firsttext[0],firsttext[1],firsttext[2]))
or
print("First record of texts, {} texts {} at time {}".format(texts[0][0],texts[0][1],texts[0][2]))
"""

"""
second method test:


def printtextbynumber(number):
    
    # print the infomation by the number of list(text)
    # :param number: the list number that you want to print
    # :return: no return just print the infomation
    
    if number > 0:
        number -= 1
    elif number == 0:
        print("no such data")
    print("First record of texts, {} texts {} at time {}"
          .format(texts[number][0], texts[number][1], texts[number][2]))

def printcallbynumber(number):
    
    # print the infomation by the number of list(call)
    # :param number: the list number
    # :return:
    
    if number > 0:
        number -= 1
    elif number == 0:
        print("no such data")
    print("Last record of calls, {} calls {} at time {}, lasting {}"
          .format(calls[number][0], calls[number][1], calls[number][2], calls[number][3]))

# main test:
printtextbynumber(1)
printcallbynumber(-1)
    
"""

# final answer:
print("First record of texts, {} texts {} at time {}"
      .format(texts[0][0],texts[0][1],texts[0][2]))
print("Last record of calls, {} calls {} at time {}, lasting {}"
      .format(calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]))