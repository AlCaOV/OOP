import logging
from google.adk.agents.llm_agent import Agent

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Повертаємо str замість dict, щоб термінал не лаявся на NoneType
def logging_tool(param: str) -> str:
    """Інструмент з логуванням подій"""
    logger.info(f"==== ВИКЛИК ІНСТРУМЕНТУ ЛОГУВАННЯ: {param} ====")
    return f"Лог успішно збережено: {param}"

# Створюємо ЄДИНОГО агента у файлі
root_agent = Agent(
    model='gemini-2.5-flash',  # Використовуємо основну модель
    name='logging_agent',
    description="Агент з логуванням.",
    instruction="Використовуй інструмент logging_tool та логуй всі дії.",
    tools=[logging_tool],
)