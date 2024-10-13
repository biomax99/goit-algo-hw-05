# Порівняння алгоритмів пошуку підрядка: Boyer-Moore, Knuth-Morris-Pratt та Rabin-Karp

## Опис завдання

У цьому завданні ми порівнюємо ефективність трьох класичних алгоритмів пошуку підрядка:

- **Boyer-Moore**
- **Knuth-Morris-Pratt (KMP)**
- **Rabin-Karp**

### Мета:

1. Дослідити швидкість роботи кожного з алгоритмів на різних типах текстів.
2. Знайти найшвидший алгоритм для пошуку існуючих та неіснуючих підрядків у тексті.
3. Зробити висновок про найкращий алгоритм для різних типів задач.

## Використані алгоритми

- **Boyer-Moore**: Ефективний для великих текстів і довгих підрядків завдяки використанню евристик для пропуску непотрібних порівнянь.
- **Knuth-Morris-Pratt**: Ефективний для регулярних шаблонів і текстів середнього розміру. Алгоритм будує таблицю для оптимізації процесу пошуку.
- **Rabin-Karp**: Добре працює для пошуку декількох підрядків одночасно за допомогою хешування, але може бути менш ефективним при одиночному пошуку підрядка.

## Результати вимірювання

Для кожного алгоритму ми виміряли час виконання на двох підрядках:

1. **Існуючий підрядок** в тексті.
2. **Вигаданий підрядок**, який відсутній у тексті.

### Час виконання для існуючого підрядка:

- **Boyer-Moore**: `1.370` секунд
- **Knuth-Morris-Pratt**: `1.029` секунд
- **Rabin-Karp**: `1.095` секунд

### Час виконання для неіснуючого підрядка:

- **Boyer-Moore**: `8.417` секунд
- **Knuth-Morris-Pratt**: `4.708` секунд
- **Rabin-Karp**: `1.033` секунд

## Висновки

1. **Boyer-Moore**:

   - Найшвидший алгоритм для великих текстів з довгими підрядками завдяки можливості пропуску великих ділянок тексту.
   - Показує високу ефективність як для існуючих, так і для неіснуючих підрядків.

2. **Knuth-Morris-Pratt (KMP)**:

   - Має стабільний час виконання незалежно від того, чи існує підрядок в тексті.
   - Найкраще підходить для коротших підрядків або текстів, де потрібна регулярна перевірка підрядків.

3. **Rabin-Karp**:
   - Добре підходить для одночасного пошуку кількох підрядків, але на одиночному пошуку він менш ефективний.
   - Важливо використовувати цей алгоритм в умовах, де потрібно здійснювати перевірку на збіги багатьох підрядків, а не одного.

### Рекомендації:

- Якщо шукаєте **довгий підрядок у великому тексті** — використовуйте **Boyer-Moore**.
- Для **пошуку коротких підрядків** і регулярних виразів — **KMP** є стабільним вибором.
- Якщо є потреба перевіряти **багато підрядків** у тексті одночасно — алгоритм **Rabin-Karp** може бути корисним, але для одиночних пошуків він менш ефективний.

---

## Як запустити код

1. Завантажте або клонуйте цей репозиторій.
2. Запустіть файл hw03.py, в якому виконано порівняння трьох алгоритмів: