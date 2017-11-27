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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字母顺序输出。
"""

def listofnumbers(history, i):
    """
    restore the i column to a list
    :param history: calls or texts history
    :param i: the column of history, maybe it's the caller numbers, the answered numbers and so on.
    :return: the list that we requested
    """
    numlist = []
    for number in history:
        numlist.append(number[i])
    return numlist
"""
test:
call0 = [[1,2],[1,3],[1,4],[2,3],[4,5],[5,6],[9,10]]
text0 = [[6,5], [9,10]]
"""
# main test
callernum = listofnumbers(calls, 0)
answercallnum = listofnumbers(calls, 1)
sendernum = listofnumbers(texts, 0)
receivetextnum = listofnumbers(texts, 1)

marketingnum = sorted(list(set(callernum) - set(answercallnum) - set(sendernum) - set(receivetextnum)))
print("These numbers could be telemarketers: ")
for number in marketingnum:
    print(number)