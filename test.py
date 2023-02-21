
# Дано: список dict-объектов вида вида {"key": "value"}, например [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}].
# Напишите функцию, которая удаляет дубликаты из этого списка. Для примера выше возвращаемое значение может быть равно [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}].
# Обязательное условие: функция не должна иметь сложность O(n^2).


#
# def my_set(my_list):
#     my_list_copy = my_list.copy()
#     for i in my_list:
#         n = 0
#         for j in my_list_copy:
#             if i == j:
#                 n +=1
#             if i == j and n == 2:
#                 my_list_copy.remove(j)
#     return my_list_copy
#
# my_list = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
#
# print(my_set(my_list))
#
# def my_set(my_list):
#     my_list_keys = []
#
#     for i in my_list:
#
#         my_list_keys.append(i.keys())
#     print (my_list_keys)
#     return set((my_list_keys))
#


my_list = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]

# 1.Вариант
def my_set(my_list):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(my_set(my_list))

# 2.Вариант
print(list({frozenset(item.items()):item for item in my_list}.values()))



