from stats import get_num_characters, print_report, get_num_words
import sys

def get_book_text(filepath):
  content = ''

  with open(filepath) as f:
    content = f.read()

  return content


def main():
  if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
  result = get_book_text(sys.argv[1])
  word_count = get_num_words(result)
  char_count = get_num_characters(result)
  sorted_chars = print_report(char_count)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")

  for dict_item in sorted_chars:
    for char, count in dict_item.items():
      print(f"{char}: {count}")
  
  print("============= END ===============")

main()