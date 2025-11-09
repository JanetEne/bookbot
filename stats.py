def get_num_words(text):
  count = len(text.split())
  return count

def get_num_characters(text):
  char_list = ' '.join(text.split()).lower()
  char_obj = {}


  for i in range(0, len(char_list)):
    if(char_list[i] in char_obj):
      char_obj[char_list[i]] += 1
    else:
      char_obj[char_list[i]] = 1

  return char_obj


def print_report(dict_of_characters):
  sorted_list = []

  for item in dict_of_characters:
    if item.isalpha():
      dict_char = {}

      dict_char[item] = dict_of_characters[item]
      sorted_list.append(dict_char)
    else:
      continue

  sorted_list.sort(key=helper_func, reverse=True)

  return sorted_list


def helper_func(dictionary_items):
   num_key_list = []
   for key, value in dictionary_items.items():
      num_key_list.append(value)
   
   return num_key_list[0]