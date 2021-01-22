def count_letters(text):
  result = {}

  for letter in text:
    letter = letter.lower()

    if letter.isalpha():
      if letter in result:
        result[letter] += 1
      else:
        result[letter] = 1

  return result
