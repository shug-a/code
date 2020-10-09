#!/usr/bin/env python
# coding: utf-8

# # Задание 1

# In[1]:


input_data = [1, 3, 2, 1, 5, 3, 5, 1, 4]


# In[2]:


def remove_duplicates(data):
    seen = []
    for x in data:
        if x not in seen:
            seen.append(x)
    return seen


# In[3]:


print(remove_duplicates(input_data))


# Асимптотическая сложность является линейной O(n), тк по каждому элементу  массива нужно пройтись только один раз (проверить условие -> добавить)

# # Задание 2
SELECT a.department
FROM (
SELECT department,
position,
COUNT(full_name) ppl_count
FROM table
GROUP BY department, position
HAVING position = 'Software Developer' and ppl_count < 5) a
# # Задание 3

# In[ ]:




