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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

def setupcallloglist(callhistory):
    """
    set up  a dictionary list that store the phone number and call time
    :param callhistory: all history of call
    :return: the dictionay list
    """
    call_log = {}
    for callinfo in callhistory:
        if (callinfo[0] not in call_log) and (callinfo[1] not in call_log):
            call_log[callinfo[0]] = int(callinfo[3])
            call_log[callinfo[1]] = int(callinfo[3])
        elif callinfo[0] in call_log:
            call_log[callinfo[0]] += int(callinfo[3])
            call_log[callinfo[1]] = int(callinfo[3])
        else:
            call_log[callinfo[0]] = int(callinfo[3])
            call_log[callinfo[1]] += int(callinfo[3])

    return call_log


def findmaxcall(call_log):
    """
    find max calls inset the dictionary list(maxnumber)
    :param call_log: call log dictionary list that have all phone number and call time
    :return: the dictionary have the max call time and with its phone number
    """
    maxtime = 0
    maxnumber = {}
    for number in call_log:
        if call_log[number] > maxtime:
            maxtime = call_log[number]
            maxnumber.clear()
            maxnumber[number] = call_log[number]
        elif call_log[number] == maxtime:
            maxnumber[number] = call_log[number]
    return maxnumber

"""
test:
callsall = [[1,2,333,1],[2,1,333,2],[2,3,333,5],[3,4,333,3]]
print(setupcallloglist(callsall))
print(findmaxcall(setupcallloglist(callsall)))
print(findmaxcall(setupcallloglist(calls)))
"""

# main test:
maxcalltimedic = findmaxcall(setupcallloglist(calls))
for item in maxcalltimedic:
    print("{} spent the longest time, {} seconds, on the phone during September 2016."
          .format(item, maxcalltimedic[item]))