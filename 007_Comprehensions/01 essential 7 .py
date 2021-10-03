# Напишите комбинацию циклов чтобы проитерировать все элементы сложной структуры
# данных вида d = {“a”: {“1”: [...], “2”: [...], ...}, ...} (словарь словарей в которых лежат списки)

d = {'a':
         {'1': ['C #'],
          '2': ['Python'],
          '3': ['Java']
          },
     'b':
         {'1': ['John'],
          '2': ['Yurii'],
          '3': ['Jim']
          }
}
d_1 = []


def func():
    for key1, item in d.items():
        for key2, item2 in item.items():
            for element in item2:
                d_1.append(element)
    return d_1


print(func())
# почему-то когда перемещаю return появляеться ошибка

#def get_data(data_iter, keys):
   # data = data_iter
   # for key in keys:
      #  data = data[key]
       # return data
  # return data


#print(get_data(d, ['a', 'b']))

# print(get_data(d, ['b']))

