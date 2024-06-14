# Question: Given a list nums, find the sum of all elements in the list.
# a = [1,2,3,4]

# def list_sum(list):
#     return sum(list)

# print("The sum od elements of lists is:", list_sum(a))


# Question: Write a function to find the maximum element in a list.
# a = [2,4,5,3,1]

# def list_max(list):
#     return max(list)

# print("The maximum element of the list is: ", list_max(a))

# Question: Remove all duplicates from a list.
# a = [1,2,4,1,3,1,5]

# def remove_dup(list):
#     return set(list)

# print("List with removed duplicates: ", list(remove_dup(a)))

# Question: Count the occurrences of an element in a list.
# a = [1,2,4,1,3,1,5]

# def count_occ(list,char):
#     return list.count(char)

# print("Number of occurrences of 1 in list are:", count_occ(a,1))

a = [1,2,4,1,3,1,5]
b = []

# Question: Check if a list is empty.
# def check_list(list):
#     if len(list)==0:
#         print("List is empty")
#     else:
#         print("List is not empty")
    
# check_list(a)
# check_list(b)


# Question: Find the index of the first occurrence of an element in a list.
# a = [1,2,4,1,3,1,2,5]

# def check_1st_occ(list,char):
#     for i in range(len(list)):
#         if list[i] == char:
#             return i
        
# print("First occurrence of input element in list is: ", check_1st_occ(a,2))

# Question: Create a new list containing only the even numbers from the original list.
# a = [1,2,3,4,5,6,7,8,9,10]
# b = []

# def create_even_no_list(list_1, list_2):
#     for i in range(len(list_1)):
#         if list_1[i] %2 == 0:
#             list_2.append(list_1[i])

# create_even_no_list(a,b)
# print(b)

# Question: Create a new list with the squares of each element in the original list.
# a = [1,2,3,4,5,6,7,8,9,10]
# b = []

# def create_sq_of_no_list(list_1, list_2):
#     for i in range(len(list_1)):
#         list_2.append(list_1[i]**2)
    
# create_sq_of_no_list(a,b)
# print(b)

# Question: Find the second-largest element in a list.
# a = [1,2,3,4,5,6,7,8,9,10]

# def sec_max(list):
#     return sorted(a)[-2]

# print(sec_max(a))

# Question: Remove all occurrences of a specific element from the list.
# a = [1,2,4,1,3,1,5]

# def remove_occ_element(list, char):
#     return [num for num in list if num!=char]

# print(remove_occ_element(a,1))

# Question: Find the common elements between two lists.
# a = [1,2,2,4,1,3,1,9,9,5]
# b = [2,6,1,1,1,3,4,7,3,1,9]
# c = []

# def find_common_element(list_1,list_2,common):
#     for i in range(len(list_1)):
#         for j in range(len(list_2)):
#             if list_1[i] == list_2[j]:
#                 common.append(list_1[i])
#     return list(set(common))

# print(find_common_element(a,b,c))

# Question: Check if a list is a palindrome (reads the same forward and backward).
# a = [1,2,3,2,1]
# b = [1,1,2,3,1,1,1]

# def check_palindrome(list):
#     for i in range(len(list)//2):
#         if list[i] != list[len(list)-1-i]:
#             print("It is not a palindrome")
#             return
#     print("It is a palindrome")
# check_palindrome(a)
# check_palindrome(b)

# Question: Flatten a list of lists into a single list.
# a = [[1,2,3,4],[5,6,7],[8,9]]
# b = []

# def flatten_list(list_1,list_2):
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             list_2.append(list_1[i][j])

# flatten_list(a,b)
# print(b)

# Question: Calculate the product of all elements in the list.
# a = [1,2,3,4]

# def calc_prod_list(list):
#     prod = 1
#     for i in range(len(list)):
#         prod = prod*list[i]
#     return prod

# print(calc_prod_list(a))

a = [1,2,3,4]
b = [5,6,7]

# def remove_1st_last(list):
#     list.pop(0)
#     list.pop(-1)
#     return list

# print(remove_1st_last(a))

# Question: Find the longest sublist in a list of lists.
# a = [[1,2,3,4],[5,6,7],[8,9]]

# def longest_sublist(list):
#     lengths = []
#     for i in range(len(list)):
#         lengths.append(len(list[i]))
    
#     for j in range(len(list)):
#         if len(list[j]) == max(lengths):
#             return list[j]

# print(longest_sublist(a))

# Question: Count the number of odd and even numbers in a list.
# a = [1,2,3,4,5,6,7,8,9,10,1,1,1,2]

# def count_odd_even(list):
#     c_odd = 0
#     c_even = 0
#     for i in range(len(list)):
#         if list[i] %2!=0:
#             c_odd +=1
#         else:
#             c_even+=1
#     print("No of odd numbers in list are: ", c_odd)
#     print("No of even numbers in list are: ", c_even)

# count_odd_even(a)

a = [1,2,3,4,5,6,7,8,9,10,1,1,1,2]

def rotate_list_left(list,rotation_no):
    modulated_r_no = rotation_no%len(list)
    list_1 = list[:modulated_r_no]
    list_2 = list[modulated_r_no:len(list)]
    return list_2 + list_1

print(rotate_list_left(a,1))

def rotate_list_right(list,rotation_no):
    modulated_r_no = rotation_no%len(list)
    list_1 = list[:(len(list) - modulated_r_no)]
    list_2 = list[(len(list) - modulated_r_no):len(list)]
    return list_2 + list_1

print(rotate_list_right(a,1))