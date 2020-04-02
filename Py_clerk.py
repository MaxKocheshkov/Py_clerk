documents = [
       {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
       {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
       {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }

# Task №1

# поиск имени по номеру доумента (p)
def search_by_number(number_doc):
  event_doc = input('введите номер документа: ')
  for event in number_doc:
    if event.get('number') == event_doc:
      print(event['name'])
      return
    else:
      print('Документа по данному номеру не обнаружено')

# вывод всех документов (l)  
def all_docs(scroll):
  for list_doc in scroll:
    folk_attach = list(list_doc.values())
    print(f'{folk_attach[0]} "{folk_attach[1]}" "{folk_attach[2]}"')

# поиск полки по номеру документа (s)
def act(shelf):
  documents_shelf = 0
  user_ordinal = input('Введите номер документа: ')
  for shelf in directories:
    documents_shelf += 1  
    if user_ordinal in directories.get(shelf):
      print('Документ на полке', shelf)
      return
    elif documents_shelf == len(directories):
      print('Документа по данному номеру не обнаружено')
      return

# Добавление нового документа в documents и directories (a)
def extension(new_doc, new_shelf):
  user_type = input('введите тип документа: ')
  user_number = input('введите номер документа: ')
  user_name = input('введите имя владельца: ')
  user_shelf = input('На какой полке будет храниться? ')

  # добавление в список documents
  new_items = [('type', user_type), ('number', user_number), ('name', user_name)]
  user_dict = dict(new_items)
  j = len(new_doc)
  new_doc.insert(j, user_dict)
  print(new_doc)
  print('###')

  # добавление в directories
  if new_shelf.get(user_shelf) != None:
    (new_shelf.get(user_shelf)).append(user_number)
    print(f"Номер документа добавлен на полку {user_shelf}: ")
    print(new_shelf)
  else:
    add_user_shelf = {user_shelf : []}
    new_shelf.update(add_user_shelf)
    (new_shelf.get(user_shelf)).append(user_number)
    print(f"Номер документа добавлен на новую полку {user_shelf}: ")
    print(new_shelf)

#Task №2 

# удаление документа из documents и directories (d)
def exterminate(delet_doc, delet_shelf):
  user_delet = input('введите номер документа для удаления: ')

  # удаление из documents
  for delet_value in delet_doc:
    if user_delet == delet_value["number"]:
      delet_doc.remove(delet_value)
      print(f'Документ с номером {user_delet} удален из documents')
      print(delet_doc)

 # удаление из directories
  for delet_ordinal in delet_shelf.values():
    for index_del in range(0, len(delet_ordinal)):
      if user_delet == delet_ordinal[index_del]:
        del delet_ordinal[index_del]
        print(f'Документ с номером {user_delet} удален из directories')
        print(delet_shelf)
        break

# Перемещение документа (m)
def transfer(doc_shelf):
  move_doc = input('Введите номер документа для перемещения: ')
  move_shelf = input('введите номер полки куда переместить: ')
  if move_shelf in doc_shelf.keys():
    for old_location, old_value in doc_shelf.items():
      for index_move in range(0, len(old_value)):
        if move_doc == old_value[index_move]:        
          (doc_shelf.get(move_shelf)).append(move_doc)
          old_value.pop(index_move)
          print(f'документ перемещен на полку {move_shelf}')
          print(doc_shelf)
          break 

# создание новой полки (as)
def supplement(add_shelf):
  new_user_shelf = input('введите номер полки для добавления: ') 
  for add_shelf_key in add_shelf.keys():
    if int(new_user_shelf) == int(add_shelf_key):
      print('Полка с таким номером уже существует')
      break
    else:
      add_shelf.setdefault(new_user_shelf, [])
      print(add_shelf)
      break

# Task №3 (Python exeption) (nd)

def displaying(all_shelf, doc_number):
  user_input_number =  input('введите номер документа: ')
  for all_doc_shelf in all_shelf.values():
    try:
        if user_input_number in all_doc_shelf:
          for output_number in doc_number:
              if user_input_number in output_number.get('number'):
                  print(output_number['name'])
                  return
              else:
                user_input_number not in output_number.get('number')
                print('У документа нет параметра "name"')
          return 
        else:
          user_input_number not in all_doc_shelf 
          raise ValueError 
    except ValueError:
      print('Документа с таким номером нет на полках')
        

def main():
  while True:
    user_input = input()
    if user_input == 'p':
      search_by_number(documents)
    elif user_input == 'l':
      all_docs(documents)
    elif user_input == 's':
      act(directories)
    elif user_input == 'a':
      extension(documents, directories)
    elif user_input == 'd':
      exterminate(documents, directories)
    elif user_input == 'm':
      transfer(directories)
    elif user_input == 'as':
      supplement(directories)
    elif user_input == 'nd':
      displaying(directories, documents)
    elif user_input == 'q':
      print('До свидания!')
      break

main()
