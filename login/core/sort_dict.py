new_list = list()
def make_linear_list(input_list):

    for  value in input_list:
        if isinstance(value,list):
            make_linear_list(value)
        else:
            new_list.append(value)
    return new_list



# print(make_linear_list([1,[2,3,4,[5,6,[7,8,9]]]]))
from itertools import groupby

def count_repeted_text():
    text = 'sadpopppa'
    s = groupby(text)
    result = [(label,sum(1 for _ in group )) for label, group in s]

    print(result)
    # new_text = ''
    # counter = 1
    # for i in range(len(text) - 1):
    #     if text[i] == text[i + 1]:
    #         counter = counter + 1
    #     else:
    #         new_text = new_text + str(counter) + text[i]
    #         counter = 1
    # new_text = new_text + str(counter) + text[-1]
    # print(new_text)


count_repeted_text()


# str1 = sorted("ART")
# str2 = sorted("RAT")
# if str1 == str2:
#     print("its anagram")
# else:
#     print("its not anagram")
#
# sort_orders = sorted({"c":100,"a":30,"b":50}.items(), key=lambda x: x[1], reverse=False)
# print(sort_orders)


