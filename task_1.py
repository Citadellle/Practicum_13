import re

def number_vowels_and_consonants(text: str) -> None:
    text = re.sub(r'[аеёиоуыэюя]', 'а', text, flags = re.IGNORECASE)                #re.IGNORECASE - игнорирование регистра
    text = re.sub(r'[бвгджзйклмнпрстфхцчшщ]', 'б', text, flags = re.IGNORECASE)     #re.IGNORECASE - игнорирование регистра
    
    print(f'Количество гласных букв: {text.count('а')}', 
          f'Количество согласных букв: {text.count('б')}', 
          sep = '\n'
          )

number_vowels_and_consonants(input())