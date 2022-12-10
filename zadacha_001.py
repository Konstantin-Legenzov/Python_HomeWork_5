# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

with open('work_text.txt', 'r', encoding='utf-8') as data:

    loaded_text = data.read()
    print(loaded_text)
    loaded_text =loaded_text.split(' ')
print(loaded_text)
delete_word = 'пугай'
for i in loaded_text:
    if delete_word in i:
        loaded_text.remove(i)
new_list = ' '.join(loaded_text)
print(new_list)
    



# new_text = [i for i in loaded_text(len(loaded_text)) lambda remove: if loaded_text['{пугай}']]
# print(new_text)