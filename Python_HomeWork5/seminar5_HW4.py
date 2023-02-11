with open('algorithm_RLE.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('algorithm_RLE.txt', 'r') as file:
    my_txt = file.readline()
    txt_compr = my_txt.split()

print(my_txt)

def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


txt_compr = file_encod(my_txt)

with open('algorithm_RLE_encod.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compr}')
print(txt_compr)