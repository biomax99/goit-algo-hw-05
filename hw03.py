import timeit

text = "Це приклад тексту для пошуку підрядка в тексті."

# Алгоритми пошуку
def boyer_moore(text, pattern):
    def preprocess_bad_character(pattern):
        bad_char_shift = {}
        length = len(pattern)
        for i in range(length):
            bad_char_shift[pattern[i]] = length - i - 1
        return bad_char_shift

    bad_char_shift = preprocess_bad_character(pattern)
    m = len(pattern)
    n = len(text)

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        else:
            i += max(1, j - bad_char_shift.get(text[i + j], m))
    return -1

def knuth_morris_pratt(text, pattern):
    def preprocess_pattern(pattern):
        lsp = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lsp[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lsp[i] = j
        return lsp

    lsp = preprocess_pattern(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lsp[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                return i - j + 1
        else:
            j = 0
    return -1

def rabin_karp(text, pattern):
    d = 256  # кількість символів в алфавіті
    q = 101  # просте число для уникнення колізій
    m = len(pattern)
    n = len(text)
    h = 1
    p = 0
    t = 0

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Функція для вимірювання часу виконання
def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=1)

# Пошуковий підрядок
pattern = "підрядка"
non_existent_pattern = "вигаданий"

# Вимірювання для існуючого підрядка
bm_time = measure_time(boyer_moore, text, pattern)
kmp_time = measure_time(knuth_morris_pratt, text, pattern)
rk_time = measure_time(rabin_karp, text, pattern)

# Вимірювання для неіснуючого підрядка
bm_time_nonexistent = measure_time(boyer_moore, text, non_existent_pattern)
kmp_time_nonexistent = measure_time(knuth_morris_pratt, text, non_existent_pattern)
rk_time_nonexistent = measure_time(rabin_karp, text, non_existent_pattern)

# Виведення результатів
print(f"Boyer-Moore (існує): {bm_time} секунд")
print(f"KMP (існує): {kmp_time} секунд")
print(f"Rabin-Karp (існує): {rk_time} секунд")

print(f"Boyer-Moore (не існує): {bm_time_nonexistent} секунд")
print(f"KMP (не існує): {kmp_time_nonexistent} секунд")
print(f"Rabin-Karp (не існує): {rk_time_nonexistent} секунд")
