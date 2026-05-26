import random
import string
from google.adk.agents.llm_agent import Agent

# 1. Якісний інструмент з докладним docstring та типізацією
def generate_secure_password(length: int, use_special_chars: bool = True) -> dict:
    """
    Генерує випадковий безпечний пароль.
    
    Args:
        length: Бажана довжина пароля (має бути від 8 до 32).
        use_special_chars: Чи додавати спеціальні символи (!@#$%^&*).
        
    Returns:
        dict: Результат генерації або помилка валідації.
    """
    # 2. Валідація вводу
    if length < 8 or length > 32:
        return {
            "status": "error", 
            "message": "Помилка: Довжина пароля має бути від 8 до 32 символів.", 
            "password": None
        }
        
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += "!@#$%^&*"
        
    password = ''.join(random.choice(chars) for _ in range(length))
    
    # 3. Повернення структурованих даних
    return {
        "status": "success",
        "message": "Пароль успішно створено",
        "password": password
    }

# 4. Чіткі системні інструкції
root_agent = Agent(
    model='gemini-2.5-flash',
    name='cybersecurity_agent',
    description="Агент для генерації безпечних паролів.",
    instruction="""
    Ти експерт з кібербезпеки. Допомагай користувачам створювати надійні паролі за допомогою інструменту generate_secure_password.
    
    Твої правила:
    1. Якщо користувач не вказав довжину пароля, попроси його уточнити (від 8 до 32 символів).
    2. Виводь згенерований пароль у блоці коду Markdown для зручного копіювання.
    3. Завжди відповідай українською мовою.
    4. Після видачі пароля дай одну коротку пораду щодо його безпечного зберігання.
    """,
    tools=[generate_secure_password],
)