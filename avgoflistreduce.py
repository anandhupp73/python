from functools import reduce

inp_lst = [12, 45, 78, 36, 45, 237.11, -1, 88]
lst_len = len(inp_lst)
lst_avg = reduce(lambda x, y: x + y, inp_lst) / lst_len
print("Average value of the list:")
print(lst_avg)   