# Звіт до роботи
## Тема: _Основні парадигми ООП_
### Мета роботи: _Ознайомитись з ключовими поняттями об’єктно-орієнтованого програмування (ООП) у Python та навчитися реалізовувати їх у власних класах на прикладі ігрової симуляції._

---
### Виконання роботи
* Результати виконання завдання:

    1. **Інкапсуляція**
        - Додано генерацію випадкових транзакцій за допомогою модуля random.
        - Результат: Програма успішно виконала серію випадкових операцій поповнення та зняття коштів, виводячи  поточний стан рахунку в консоль.
    2. **Наслідування**
        - Створено ще один метод у класі Vehicle та викликано його з обєкта класу Car;
        - Результат:
        ```python
        class Vehicle:
            def __init__(self, brand, model):
                self.brand = brand
                self.model = model

            def display_info(self):
                return f"{self.brand} {self.model}"

            def drive(self):
                return f"{self.display_info()} is driving."
        class Car(Vehicle):
            def __init__(self, brand, model, seats ):
                super().__init__(brand, model)  # виклик конструктора базового класу
                self.seats = seats

            def display_info(self):
                return f"{super().display_info()}, Seats: {self.seats}"
            
            def drive(self):
                return f"{self.display_info()} is driving on the road."

        car = Car("Toyota", "Camry", 5)
        print(car.display_info())
        print(car.drive())
        ```
        
    3. **Поліморфізм**
        - створити клас Fish у якого немає метода speak
        - Результат: 
        ```python
        class Fish(Animal):
            pass
        ```
        ```
        Dog: Woof!
        Cat: Meow!
        Fish: None
        ```
    4. **Третій тип зброї**
        - Додано третій тип зброї — Bow (лук) з параметром дальності та методом перезарядки.

        - Реалізовано випадковий вибір зброї.

        - Зроблена покрокова гра з можливістю вибору дій (Атака або Підсилення).

        - Результат:
        ```python
        def get_random_weapon(owner_name):
            weapon_type = choice(['sword', 'axe', 'bow'])
            if weapon_type == 'sword':
                return Sword(f"{owner_name}_Blade", randint(20, 30))
            elif weapon_type == 'axe':
                return Axe(f"{owner_name}_Chopper", randint(25, 35))
            elif weapon_type == 'bow':
                return Bow(f"{owner_name}_Bow", randint(15, 25), range_power=10)
            
        print("Обираємо зброю...")
        player = get_random_weapon("Hero")
        computer = get_random_weapon("Enemy")

        print(f"\nВи отримали: {player.name} ({type(player).__name__}) | HP: {player.health}")
        print(f"Супротивник: {computer.name} ({type(computer).__name__}) | HP: {computer.health}")
        print("-" * 50)



        turn = 1
        while player.health > 0 and computer.health > 0:
            print(f"\n--- Хід {turn} ---")
            
            print(f"Ваше HP: {player.health} | HP Ворога: {computer.health}")
            print("Дії: [1] Атака  [2] Підсилення (Заточка/Приціл)")
            
            choice_action = input("Ваш вибір: ")
            
            if choice_action == "1":
                print(f"Ви: {player.attack(computer)}")
            elif choice_action == "2":
                print(f"Ви: {player.power_up()}")
            else:
                print("Невірний вибір, ви пропускаєте хід!")


            if computer.health <= 0:
                print(f"\n ПЕРЕМОГА! {computer.name} знищено.")
                break

            time.sleep(1) 

            if randint(1, 100) <= 30:
                print(f"Бот: {computer.power_up()}")
            else:
                print(f"Бот: {computer.attack(player)}")


            if player.health <= 0:
                print(f"\n ПОРАЗКА! {player.name} знищено.")
                break
                
            turn += 1
            print("-" * 50)
        ```
        ```
                Обираємо зброю...

        Ви отримали: Hero_Bow (Bow) | HP: 500
        Супротивник: Enemy_Bow (Bow) | HP: 500
        --------------------------------------------------

        --- Хід 1 ---
        Ваше HP: 500 | HP Ворога: 500
        Дії: [1] Атака  [2] Підсилення (Заточка/Приціл)
        Ви: Постріл з лука Hero_Bow на 47 шкоди (Дальність: 10).
        Бот: Постріл з лука Enemy_Bow на 38 шкоди (Дальність: 10).
        --------------------------------------------------

        --- Хід 2 ---
        Ваше HP: 462 | HP Ворога: 453
        Дії: [1] Атака  [2] Підсилення (Заточка/Приціл)
        Ви:  Лук Hero_Bow натягнуто сильніше! (Дальність збільшено)
        Бот: Постріл з лука Enemy_Bow на 37 шкоди (Дальність: 10).
        --------------------------------------------------
        ```

---
### Висновок:
- :question: **Що зроблено в роботі:** Ми ознайомилися з основними принципами ООП. Реалізували класи для банківського рахунку та рольової гри. Створили ієрархію класів зброї, використовуючи абстрактний базовий клас.
- :question: **Чи досягнуто мети роботи:** Так, мету досягнуто. Ми навчилися застосовувати інкапсуляцію (приватні атрибути), спадкування (створення підкласів зброї) та поліморфізм (різна реалізація методу attack).
- :question: **Які нові знання отримано:** Як використовувати модуль abc для створення абстрактних методів.
Як працює super() для ініціалізації батьківських класів.
Як реалізувати взаємодію об'єктів у циклі.
- :question: **Чи вдалось відповісти на всі питання задані в ході роботи:** Так
- :question: **Чи вдалося виконати всі завдання:** Так, всі завдання реалізовані в коді.
- :question: **Чи виникли складності у виконанні завдання:** Завдання виконано успішно
