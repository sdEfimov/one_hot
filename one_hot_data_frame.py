import pandas as pd

# -----------------Исходный код-------------
import random
lst = ['robot'] * 10
lst += ['human'] * 10
# lst += ['cat'] * 10 # для эксперимента, отсутствует в исходном коде (работает)
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
#data.head() # строчка закомментирована 
# ------------Конец исходного кода----------

data_uniq = "".join(list(set(data))) # получаем название столбца

list1 = list(data[data_uniq]) # получаем список данных = lst

data_uniq1 = set(list1)
data_uniq1 = list(data_uniq1) # получаем список уникальных значений

for who_AmI in data_uniq1: # добавляем и заполняем новые столбцы значениями 0 и 1 
    data.loc[data[data_uniq] == who_AmI, who_AmI] = 1
    data.loc[data[data_uniq] != who_AmI, who_AmI] = 0

onehot_data = data[data_uniq1] # Создаём one hot DataFrame

print(onehot_data)
# print(data)  # для проверки