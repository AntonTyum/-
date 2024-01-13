files = ['1.txt', '2.txt', '3.txt']
file_contents = []

for file_name in files:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        num_lines = content.count('\n') + 1
        file_contents.append((file_name, num_lines, content))

file_contents.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_info in file_contents:
        result_file.write(f"{file_info[0]}\n{file_info[1]}\n")
        result_file.write(file_info[2] + '\n')
