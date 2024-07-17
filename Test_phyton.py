#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re


# ### Задание 1.
# 
# Особенный номер – строка формата [2-4 цифры]\[2-5 цифр]. Хороший номер - строка формата [4 цифры]\[5 цифр]. Хороший номер можно получить из особенного дополнением нулей слева к обоим числам.
# Пример:
# 17\234 => 0017\00234 
# 
# Напишите функцию, которая принимает на вход строку и для каждого особенного номера, встречающегося в строке, выводит соответствующий хороший номер.
# 

# In[2]:


def good_number(special_number):
    pattern = r'(\d{2,4})\\(\d{2,5})'
    result = re.findall(pattern, special_number)
    transformed_numbers = [f"{match[0].zfill(4)}\\{match[1].zfill(5)}" for match in result]
    return transformed_numbers

# Пример использования функции
special_number = "Адрес 5467\\456. Номер 405\\549"
result = good_number(special_number)
for number in result:
    print(number)


# ### Задание 2.
# На прямой дороге расположено n банкоматов. Было решено построить ещё k банкоматов для того, чтобы уменьшить расстояние между соседними банкоматами. 
# На вход подаются натуральные числа n и k, а также n-1 расстояний L, где L_i  – расстояние между банкоматами i и  i+1. 
# 
# Напишите функцию, которая добавляет k банкоматов таким образом, чтобы максимальное расстояние между соседними банкоматами являлось минимально возможным, и возвращает список новых расстояний между банкоматами.

# In[3]:


def add_atms(n, k, distances):
    distances.sort(reverse=True)  # Сортируем расстояния в порядке убывания
    new_distances = []
    
    for i in range(n-1):
        new_distances.append(distances[i])
        for j in range(k):
            if len(distances) == i+1:
                break
            new_distance = round((distances[i] - distances[i+1]) / (k+1), 1) # Равномерно распределяем новые банкоматы
            new_distances.extend([distances[i+1] + new_distance*(j+1) for j in range(k)])  # Добавляем новые расстояния
    
    new_distances.append(distances[-1])  # Добавляем последнее расстояние
    
    return new_distances

# Пример использования функции
n = 3
k = 2
distances = [5, 10]
new_distances = add_atms(n, k, distances)
print(new_distances)


# ### Задание 3.
# Напишите функцию, которая принимает на вход список строк, состоящих из цифр, и возвращает максимальное возможное число, которое может получиться в результате конкатенации всех строк из этого списка.

# In[4]:


def max_concatenated_number(strings):
    sorted_strings = sorted(strings, key=lambda x: x, reverse=True)  # Сортировка строк по убыванию
    concatenated_number = ''.join(sorted_strings)  # Конкатенация отсортированных строк
    return concatenated_number

# Пример использования функции
strings = ["41", "4", "005", "89"]
result = max_concatenated_number(strings)
print(result)  # Вывод: 89441005


# In[ ]:




