tup = (1,2,3,4,5,6,7,8,9)
tup_2 = (1,3,11,12,3,5)

# def tup_to_str(tup):
#     string = ""
#     for i in range(len(tup)):
#         string+=str(tup[i])
#     return string

# print(tup_to_str(tup))

# tup_1 = (("abcd"),("efgh"))

# def str_tup_to_sin_str(tup):
#     string = ""
#     for i in range(len(tup)):
#         string += tup[i]
#     return string

# print(str_tup_to_sin_str(tup_1))

# def rem_element_tup(tup,element):
#     new_tup = []
#     for i in range(len(tup)):
#         if tup[i] != element:
#             new_tup.append(tup[i])
#     return tuple(new_tup)

# print(rem_element_tup(tup,1))

# def common_ele_tup(tup_1,tup_2):
#     common = []
#     for i in range(len(tup_1)):
#         if tup_1[i] in tup_2:
#             common.append(tup[i])
#     return list(set(common))

# print(common_ele_tup(tup,tup_2))

# def sort_tuple(tup):
#     sorted = list(tup)
#     sorted.sort()
#     return tuple(sorted)

# print(sort_tuple(tup_2))

# def sum_ele_tup(tup):
#     sum = 0
#     for i in range(len(tup)):
#         sum += tup[i]
#     return sum

# print(sum_ele_tup(tup))  

def merge_tup(tup_1,tup_2):
    return set(tup_1+tup_2)

print(merge_tup(tup,tup_2))
