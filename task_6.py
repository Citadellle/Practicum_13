def checking_message_length(string: str) -> str:
    if len(string) < 160:
        return string
    return string[:160]


print(checking_message_length('Введите сообщение: '))