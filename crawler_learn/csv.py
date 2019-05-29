#-*- coding: utf-8 -*
import csv


#通过 writer类写入数据
#待写入的数据 注意到两个列表的元素个数不一样
test_writer_data_1 = ['Tom', 'Cody', 'Zack']
test_writer_data_2 = ['Mike', 'Bill']

#创建并打开文件
with open('test_writer.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #获得 writer对象 delimiter是分隔符 默认为 ","
    writer = csv.writer(csvfile, delimiter=' ')
    #调用 writer的 writerow方法将 test_writer_data写入 test_writer.csv文件
    writer.writerow(test_writer_data_1)
    writer.writerow(test_writer_data_2)


#通过 DictWriter类写入数据
#待写入的数据 注意到待写入的数据类型为 dict 且第二个字典没有 lastname
test_dict_writer_data_1 = {'firstname': 'Tom', 'lastname': 'Loya'}
test_dict_writer_data_2 = {'firstname': 'Tom', 'lastname': 'Loya'}

#创建并打开文件
with open('test_dict_writer.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #设置表头
    fieldnames=['firstname', 'lastname']
    # 获得 DictWriter对象 delimiter是分隔符 默认为 "," 表头为 'firstname' 'lastname'
    dict_writer = csv.DictWriter(csvfile, delimiter=' ', fieldnames=fieldnames)
    #第一次写入数据先写入表头
    dict_writer.writeheader()
    #调用 DictWriter的 writerow方法将 test_dict_writer_data写入 test_dict_writer.csv文件
    dict_writer.writerow(test_dict_writer_data_1)
    dict_writer.writerow(test_dict_writer_data_2)





# 前面讲到，csv没有统一的标准，通过上面的例子我们可以发现，csv对写入的数据不做任何检查，也就是说几乎没有任何标准可言。
# 我们发现 writerow方法不会对数据进行检查，即使前后两句 writerow语句写入的数据的格式不同也不会报错。
# 所以在用 csv写入数据时要特别注意数据的格式问题！！！
# 也可以用 writerows(list) 一次写入多行，例如：
with open('test_writer.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #获得 writer对象 delimiter是分隔符 默认为 ","
    writer = csv.writer(csvfile, delimiter=' ')
    #调用 writer的 writerows方法将 test_writer_data写入 test_writer.csv文件
    writer.writerows([test_writer_data_1, test_writer_data_2])

with open('test_dict_writer.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #设置表头
    fieldnames=['firstname', 'lastname']
    # 获得 DictWriter对象 delimiter是分隔符 默认为 "," 表头为 'firstname' 'lastname'
    dict_writer = csv.DictWriter(csvfile, delimiter=' ', fieldnames=fieldnames)
    #第一次写入数据先写入表头
    dict_writer.writeheader()
    #调用 DictWriter的 writerows方法将 test_dict_writer_data写入 test_dict_writer.csv文件
    dict_writer.writerows([test_dict_writer_data_1, test_dict_writer_data_2])
