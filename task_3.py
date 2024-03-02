import gdown
import timeit
import boyer_moor_search
import kmp_search
import rabin_karp_search

# Функція для завантаження файлу з Google Drive
def download_file_from_google_drive(id, destination):
    url = f'https://drive.google.com/uc?id={id}'
    gdown.download(url, destination, quiet=False)
    

# Завантажуємо файли
file1_id = '18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh'
file2_id = '13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ'
file1_path = 'file1.txt'
file2_path = 'file2.txt'
text1 = download_file_from_google_drive(file1_id, file1_path)
text2 = download_file_from_google_drive(file2_id, file2_path)


# Підрядки
existing_substring = "recommendation"
nonexistent_substring = "Blablabal"

# Функція для вимірювання часу
def measure_time(func, text, substring):
    return timeit.timeit(lambda: func(text, substring), number=100)

# Алгоритм Боєра-Мура
print("*** Алгоритм Боєра-Мура ***")
for text_file, substring in [(file1_path, existing_substring), (file1_path, nonexistent_substring),
                             (file2_path, existing_substring), (file2_path, nonexistent_substring)]:
    with open(text_file, "r", encoding='ISO-8859-1') as f:
        text = f.read()
    time_elapsed = measure_time(boyer_moor_search.boyer_moor_search, text, substring)
    print(f"Файл: {text_file}, підрядок: {substring}, час: {time_elapsed:.5f} сек")
    position = boyer_moor_search.boyer_moor_search(text, substring)
    if position != -1:
        print(f"Substring found at index {position}")
    else:
        print("Substring not found")

# Алгоритм Кнута-Морріса-Пратта
print("*** Алгоритм Кнута-Морріса-Пратта ***")
for text_file, substring in [(file1_path, existing_substring), (file1_path, nonexistent_substring),
                             (file2_path, existing_substring), (file2_path, nonexistent_substring)]:
    with open(text_file, "r", encoding='ISO-8859-1') as f:
        text = f.read()
    time_elapsed = measure_time(kmp_search.kmp_search, text, substring)
    print(f"Файл: {text_file}, підрядок: {substring}, час: {time_elapsed:.5f} сек")
    position = kmp_search.kmp_search(text, substring)
    if position != -1:
        print(f"Substring found at index {position}")
    else:
        print("Substring not found")

# Алгоритм Рабіна-Карпа
print("*** Алгоритм Рабіна-Карпа ***")
for text_file, substring in [(file1_path, existing_substring), (file1_path, nonexistent_substring),
                             (file2_path, existing_substring), (file2_path, nonexistent_substring)]:
    with open(text_file, "r", encoding='ISO-8859-1') as f:
        text = f.read()
    time_elapsed = measure_time(rabin_karp_search.rabin_karp_search, text, substring)
    print(f"Файл: {text_file}, підрядок: {substring}, час: {time_elapsed:.5f} сек")
    position = rabin_karp_search.rabin_karp_search(text, substring)
    if position != -1:
        print(f"Substring found at index {position}")
    else:
        print("Substring not found")
