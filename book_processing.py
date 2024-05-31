# Нужные импорты
import csv
import re

# Cчитать файл
with open('1043.txt') as file:
    lines = [line.rstrip() for line in file]


# Переменная на случай разделителей с римскими цифрами
ROMANS =  [ "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
    "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"]

# Функция на случай если по формату файл считался не по абзацам
def strings2paragraphs(lines):
  new_lines = []
  paragraph = ""
  for line in lines:
    if line == '':
      if len(paragraph) != 0:
        new_lines.append(paragraph)
        paragraph = ''
      new_lines.append(line)
    else:
      if len(paragraph) != 0:
        paragraph += ' '
        paragraph += line
      else:
        paragraph = line
  return new_lines


# Процесс разделения книги на главы
# Тут приведен один из множества дизайнов
chapters = []
one_chapter = []
for i in range(len(lines[:-1])):
  # проверка на начало новой главы
  if 'CHAPTER ' in lines[i] and lines[i+1] == '' and lines[i+2] == '':
    chapters.append(one_chapter)
    one_chapter = []
  elif '§' in lines[i]:
    chapters.append(one_chapter)
    one_chapter = []
  elif lines[i] == '':
    pass
  elif lines[i] == '\ufeff':
    pass
  else:
    one_chapter.append(lines[i])


# Дальше главы делятся на чанки
all_csv = [['chunk', 'first', 'count']] # список списков по 3 элемента: чанк: str, первый ли: 0/1, кол-во слов:int
old = [] # список абзацев для сохранения
cnt = 0 # счетчик слов
for chapter in chapters:
  first = 1
  for i in range(len(chapter)):
    new = chapter[i]
    # если 1 абзац длиннее
    if len(new.split()) > 331:
      print('WARNING')
      # добавляем и предыдущее
      CHUNK = "/n".join(old)
      all_csv.append([CHUNK, first, cnt])
      # и текущее
      CHUNK = new
      all_csv.append([CHUNK, first, len(new.split())])
      old = []
      cnt = 0
      first = 0
    # если это конец главы, сохраняется всё, объем на следующем этапе
    elif i == len(chapter)-1:
      if cnt + len(new.split()) <= 331:
        old.append(new)
        cnt += len(new.split())
        CHUNK = "/n".join(old)
        all_csv.append([CHUNK, first, cnt])
        old = []
        cnt = 0
        first = 0
      else:
        CHUNK = "/n".join(old)
        all_csv.append([CHUNK, first, cnt])
        CHUNK = new
        all_csv.append([CHUNK, first, len(new.split())])
        old = []
        cnt = 0
        first = 0
    # если можно добавить ещё абзац
    elif cnt + len(new.split()) <= 331:
      old.append(new)
      cnt += len(new.split())
    # если следующий абзац не помещается
    else:
      CHUNK = "/n".join(old)
      old = []
      old.append(new)
      all_csv.append([CHUNK, first, cnt])
      cnt = len(new.split())
      first = 0

# Получаем количество элементов
print(len(all_csv))

# Сохраняем в CSV
with open('1043.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(all_csv)