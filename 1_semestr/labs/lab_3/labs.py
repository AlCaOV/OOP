
class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу
        """
        self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
        #================= Пера літера велика ==================
        self.name = self.name.capitalize()

        #================= Перевірка на літери ==================
        if not self.name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")

        MyName.total_names += 1 #modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self) -> str: 
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()
    #================= лічильник букв ==================
    def count_letters(self) -> int:
        return len(self.name)
    
    #================= Заміна домену ==================
    def create_email(self, domain="itcollege.lviv.ua") -> str:
        return f"{self.name}@{domain}"

    #================= Повне імя ==================
    @property
    def full_name(self) -> str:
        return f"User #{self.my_id}: {self.name} ({self.my_email})"
    
    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!(вже замінена частина)") -> str:
        """Static method
        """
        return f"You say: {message}"
    
    #================= Збереження у файл ==================
    def save_to_file(self, filename="users.txt"):
        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(self.full_name + "\n")
            print(f"Дані користувача {self.name} успішно збережено у {filename}")
        except IOError as e:
            print(f"Помилка при записі у файл: {e}")


print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", "yura", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.full_name}
This is property {type(me.whoami)} call: {me.whoami}
This is method {type(me.count_letters)} call: {me.count_letters()} letters
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")
    
    me.save_to_file()

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")
