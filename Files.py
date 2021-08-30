names_list = ['shira', 'chevi', 'efriam', 'naftoly', 'breindy', 'rosa', 'elisheva', 'aviva', 'rut', 'sarina', 'refael']

# write to file
file_name = input('enter file name: ')
handler = open(file_name + '.txt', 'w')
for i in range(len(names_list)):
    handler.write(names_list[i] + '\n')
handler.close()

# read from file
file_name = input('enter file name: ')
handler = open(file_name + '.txt', 'rt')
count = 0
for line in handler:
    count = count + 1
    if count % 2 == 0:
        continue
    else:
        print(line, end='')
handler.close()
