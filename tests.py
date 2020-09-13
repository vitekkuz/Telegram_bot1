import exceptions
raw_message = '2 ывсм'

split_message = raw_message.strip().split(' ', 1)
if len(split_message) != 2:
    raise exceptions.NonCorrectMessage(
        'Некорректное сообщение. Напишите сообщение в формате: \n'
        '50 отжимания'
    )

if split_message[0].isdigit():
    amount = split_message[0].strip()
else:
    raise exceptions.NonCorrectMessage(
        'Некорректное сообщение. Напишите сообщение в формате: \n'
        '50 отжимания'
    )
category_name = split_message[1].strip()
print(amount, category_name)

exit()




amount = regexp_result.group(1).replace(" ", "")
category_name = regexp_result.group(2).strip().lower()

print(amount, category_name)
print(amount, 'sdf', '\n', category_name)
