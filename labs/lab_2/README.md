# Звіт до роботи
## Тема: Основи програмування на Python
### Мета роботи: Навчитись застосовувати основні конструкції мови Python, виконати всі приклади та з використанням AI створити власні приклади які демонструють особливості кодових конструкцій Pyhton

---
### Виконання роботи
* Результати виконання завдання:
    1. Основні типи даних:
    ```python
    a = "Yurii"
    b = 17 # числова Змінна
    b1 = 22.8
    c = ["Середній", 5, 11.9, "Word", b] # List
    d = {"a": "Words", "b": 5, a: b1} # Dict
    e = ("b", a) # Tuple
    f = {"ss", b + b1} # Set
    print(c[4] + d[a],"=",d[a],"+",b) 
    ```
    2. Вбудовані константи:
    ```python
    print("Перша константа: ", True)
    print("Друга константа: ", False)
    print("Третя константа: ", None)
    ```
    3. Вбудовані функції:
    ```python
    print(hex(2))
    print(oct(8))
    print(bin(5))
    ```
    4. Цикли:
    ```python
    leng = [1, 'nothing', 3.14, True, None, 'something', 42, False]
    string_leng = []
    for i in range(len(leng)):
        if isinstance(leng[i], str):
            string_leng.append(leng[i])
    print(string_leng)


    numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(numb)):
        if numb[i] % 2 == 0:
            print("Число", numb[i], "є парним")
    ```
    5. Розгалуження:
    ```python
    from random import randint
        c = randint(1, 100)
        if c < 50:
            print("Загадане число менше за 50")
            print("Загадане число:", c)
        elif c > 50:
            print("Загадане число більше за 50")
            print("Загадане число:", c)
        else:
            print("Загадане число дорівнює 50")
            print("Загадане число:", c)

        score = randint(0, 100)
        if score >= 90:
            grade = "A"
        elif score >= 75:
            grade = "B"
        elif score >= 60:
            grade = "C"
        else:
            grade = "D"
        print(f"score = {score} → grade = {grade}")
    ```
    6. Конструкція try->except->finally:
     ```python
     # Навмисно провокуємо помилку перетворення типу
    raw = "not_a_number"

    try:
        print("Пробую перетворити на int і поділити 10 на число…")
        n = int(raw)          # ValueError тут
        print(10 / n)         # ZeroDivisionError, якщо n == 0
    except ValueError as e:
        print("Це точно помилка перетворення:", e)
    except ZeroDivisionError as e:
        print("Ділення на нуль недопустиме:", e)
    except Exception as e:
        print("Інша неочікувана помилка:", e)
    finally:
        print("Блок finally виконується завжди — прибираємо ресурси, логи тощо.")
     ```
    7. Контекст-менеджер:
    ```python
    lines = ["Перша лінія\n", "Друга лінія\n", "Третя лінія\n"]
    with open("demo.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)
    ```
    8. Лямбди:
    ```python
    sum = lambda x, y: x + y
    print(sum(5, 3))
    ```
---
### Висновок:

- Що зроблено в роботі;
`ознайомленно з базовим Python`
- Чи досягнуто мети роботи;
`так, усі завдання в меті досягнуто`
- Які нові знання отримано;
`Ознайомлення з контекст менеджером`
- Чи вдалось відповісти на всі питання задані в ході роботи;
`так, вдалось`
- Чи вдалося виконати всі завдання;
`усі завдання успішно виконані`
- Чи виникли складності у виконанні завдання;
`жодних складностей у виконанні завдання не виникло`
---