fruit = {'orange':'sweet and citrus fruit',
          'apple': 'sweet and good for making cider',
          'lemon': 'a sour and citrus fruit',
          'grape': 'a small and sweet fruit groping in bunches',
          'lime':  'a sour green citrus',
          'mango': 'sweet and king of fruits'}


while True:
    dict_key = input("enter the fruit name: ")
    if dict_key == 'quit':
        break

    description = fruit.get(dict_key)    
    print(description)