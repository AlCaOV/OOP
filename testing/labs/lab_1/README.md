# Звіт до роботи
**Дисципліна:** Тестування програмного забезпечення та комп'ютерних систем
**Виконав:** Середній Юрій, група КН-42

## Тема: _Загальне тестування та юніт-тести_
### Мета роботи: _Навчитись перевіряти вхідні дані за допомогою `assert` та `raise`, писати юніт-тести з модулем `unittest`, використовувати `setUp`/`tearDown`, `subTest` та `unittest.mock`._

---
### Виконання роботи
Файли роботи:
- [app.py](app.py) — клас `Figure` з прикладу + метод `get_angles`;
- [test.py](test.py) — тести для `Figure`;
- [functions.py](functions.py) — перевірка числа, підрахунок символів, ділення, підрахунок голосних, функція з `input()`;
- [test_functions.py](test_functions.py) — тести для функцій.

#### 1. Перевірка даних
Зробив власну перевірку введеного числа. Якщо введено не число — `ValueError`, якщо число не додатне — спрацьовує `assert`:
```python
def check_number(value):
    if not value.lstrip("-").isdigit():
        raise ValueError("Потрібно ввести ціле число")
    number = int(value)
    assert number > 0, "Число має бути більшим за нуль!"
    return number
```
Результат для правильного і неправильного введення:
```text
> python functions.py
Введіть число: 5
5

> python functions.py
Введіть число: abc
ValueError: Потрібно ввести ціле число

> python functions.py
Введіть число: -3
AssertionError: Число має бути більшим за нуль!
```

#### 2. Тестування функцій
Протестував `count_symbols` (звичайний і порожній рядок) та `divide` (звичайне ділення і `ZeroDivisionError`). Також написав функцію `count_vowels`, яка рахує голосні, і 6 тестів для неї: англійські літери, великі літери, рядок без голосних, порожній рядок, рядок з цифрами, рядок з українськими літерами.
```python
def count_vowels(text: str) -> int:
    count = 0
    for ch in text.lower():
        if ch in "aeiouаеєиіїоуюя":
            count += 1
    return count
```

**Тест, який спочатку не проходив.** Спочатку функція рахувала тільки англійські голосні (`"aeiou"`), і тест з українськими літерами впав:
```text
> python -m unittest test_functions.TestVowels -v
test_digits (test_functions.TestVowels.test_digits) ... ok
test_empty (test_functions.TestVowels.test_empty) ... ok
test_english (test_functions.TestVowels.test_english) ... ok
test_no_vowels (test_functions.TestVowels.test_no_vowels) ... ok
test_ukrainian (test_functions.TestVowels.test_ukrainian) ... FAIL
test_upper (test_functions.TestVowels.test_upper) ... ok

======================================================================
FAIL: test_ukrainian (test_functions.TestVowels.test_ukrainian)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "...\test_functions.py", line 42, in test_ukrainian
    self.assertEqual(4, count_vowels("Привіт, Юра"))
AssertionError: 4 != 0

----------------------------------------------------------------------
Ran 6 tests in 0.002s

FAILED (failures=1)
```
Після цього я додав українські голосні, але випадково дописав ще й `y`. Тепер впав інший тест — `test_no_vowels`, бо в слові `xyz` знайшлась одна «голосна»:
```text
FAIL: test_no_vowels (test_functions.TestVowels.test_no_vowels)
    self.assertEqual(0, count_vowels("xyz"))
AssertionError: 0 != 1
```
Прибрав `y` — і всі тести пройшли. Тут добре видно, навіщо потрібні тести: виправляючи одну помилку, я зробив іншу, і тест одразу її показав.

#### 3. Перший приклад (клас Figure)
Створив кілька об'єктів і перевірив властивості вручну:
```text
> python app.py
квадрат 5 4
трикутник 3 3
```
Тест довжини `test_figure_length` у поточній версії прикладу вже був розкоментований і проходив — помилки в `get_figure_length` немає, вона повертає `self.length`.

Додав метод `get_angles` (через словник кількості кутів) і тести для квадрата, прямокутника і трикутника:
```python
ANGLES = {"квадрат": 4, "прямокутник": 4, "трикутник": 3}

@property
def get_angles(self) -> int:
    return self.ANGLES[self.type]
```
Додав тести для нульової довжини (`test_invalid_length`), від'ємної довжини (`test_negative_length`) і невідомого типу фігури (`test_invalid_figure`) — у всіх трьох випадках очікується `AssertionError`.

#### 4. Життєвий цикл тесту
У `TestFigure` використав:
- `setUpClass` / `tearDownClass` — виводять повідомлення один раз перед і після всіх тестів класу;
- `setUp` — перед кожним тестом створює новий об'єкт `Figure("квадрат", 5)`;
- `tearDown` — після кожного тесту обнуляє об'єкт, щоб тести були незалежні.

#### 5. subTest і mock
**subTest** — перевіряю всі типи фігур в одному тесті:
```python
def test_all_figures(self):
    for figure_type in Figure.FIGURES:
        with self.subTest(figure_type=figure_type):
            f = Figure(figure_type, 3)
            self.assertEqual(figure_type, f.get_figure_type)
            self.assertEqual(3, f.get_figure_length)
```
Навіщо: якщо одна фігура не пройде, тест не зупиниться на ній, а перевірить решту, і в результаті буде видно, на якому саме `figure_type` помилка. Без `subTest` цикл зупинився б на першій помилці.

**mock** — функція `ask_number()` читає число через `input()`. Щоб не вводити його руками під час тестів, я підміняю `input` через `patch`:
```python
@patch("builtins.input", return_value="5")
def test_ask_number(self, mock_input):
    self.assertEqual(5, ask_number())
    mock_input.assert_called_once()

@patch("builtins.input", return_value="abc")
def test_ask_number_wrong(self, mock_input):
    with self.assertRaises(ValueError):
        ask_number()
```
Навіщо: тест проходить автоматично без участі користувача, а я можу «ввести» і правильне, і неправильне значення. `assert_called_once()` перевіряє, що `input` справді викликався один раз.

#### 6. Команди запуску та результат
```bash
cd testing/labs/lab_1
python test.py
python test_functions.py
python -m unittest -v
```
Результат `python -m unittest -v`:
```text
test_all_figures (test.TestFigure.test_all_figures) ... ok
test_angles (test.TestFigure.test_angles) ... ok
test_figure_length (test.TestFigure.test_figure_length) ... ok
test_figure_lengths (test.TestFigure.test_figure_lengths) ... ok
test_figure_type (test.TestFigure.test_figure_type) ... ok
test_invalid_figure (test.TestFigure.test_invalid_figure) ... ok
test_invalid_length (test.TestFigure.test_invalid_length) ... ok
test_negative_length (test.TestFigure.test_negative_length) ... ok
test_check_number (test_functions.TestFunctions.test_check_number) ... ok
test_count_symbols (test_functions.TestFunctions.test_count_symbols) ... ok
test_divide (test_functions.TestFunctions.test_divide) ... ok
test_ask_number (test_functions.TestInput.test_ask_number) ... ok
test_ask_number_wrong (test_functions.TestInput.test_ask_number_wrong) ... ok
test_digits (test_functions.TestVowels.test_digits) ... ok
test_empty (test_functions.TestVowels.test_empty) ... ok
test_english (test_functions.TestVowels.test_english) ... ok
test_no_vowels (test_functions.TestVowels.test_no_vowels) ... ok
test_ukrainian (test_functions.TestVowels.test_ukrainian) ... ok
test_upper (test_functions.TestVowels.test_upper) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.002s

OK

початок тестів Figure

кінець тестів Figure
```

---
### Висновок:
- **Що зроблено:** написав перевірку введеного числа через `assert` і `ValueError`, функцію підрахунку голосних з тестами, доповнив клас `Figure` методом `get_angles` і тестами для граничних випадків, використав `setUp`/`tearDown`, `subTest` і `mock.patch`. Всього 19 тестів, усі проходять.
- **Чи досягнуто мети:** так.
- **Нові знання:** різниця між `assert` і `raise ValueError`, як працює `unittest.TestCase` і його методи (`assertEqual`, `assertRaises`), життєвий цикл тесту, навіщо `subTest` і як підмінити `input()` через `patch`.
- **Чи вдалось відповісти на всі питання:** так.
- **Чи вдалося виконати всі завдання:** так, усі завдання з :star: і :fire:.
- **Складності:** тест з українськими літерами спочатку не проходив, а під час виправлення я зробив нову помилку (додав `y`), яку теж знайшов тест. Тест довжини в прикладі вже проходив, тому помилки в ньому шукати не довелось.
- **Feedback:** формат зручний — код і звіт в одному репозиторії.
- **Suggestions:** немає.
