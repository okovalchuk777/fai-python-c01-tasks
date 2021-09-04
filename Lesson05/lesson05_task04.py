"""
Read from file and write to another python
https://stackoverflow.com/questions/50435295/read-from-file-and-write-to-another-python/50435495
7 Efficient Ways to Replace Item in List in Python
https://www.pythonpool.com/replace-item-in-list-python/
Delete Lines From a File in Python
https://pynative.com/python-delete-lines-from-file/
Remove the last empty line from each text file
https://stackoverflow.com/questions/44166748/remove-the-last-empty-line-from-each-text-file
“how to clear file python” Code Answer’s
https://www.codegrepper.com/code-examples/python/how+to+clear+file+python
"""
input_file = "text_4.txt"
output_file = "lesson05_04.txt"
with open(input_file, mode="r", encoding="utf-8") as input_f_obj, \
     open(output_file, mode="w+", encoding="utf-8") as output_f_obj:
    line_count = 0
    numbers_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    for line in input_f_obj:
        input_string = line.split()
        input_string[0] = numbers_dict.get(input_string[0])
        output_f_obj.write(f'{" ".join(input_string)}\n')

with open(output_file, mode="r", encoding="utf-8") as output_f_obj:
    data = output_f_obj.read().rstrip('\n')
    print(data)
    
with open(output_file, mode="w+", encoding="utf-8") as output_f_obj:
    output_f_obj.write(data)
    content = output_f_obj.read()
    print(content)
