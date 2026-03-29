import requests

class FactFetcher:
    """Клас для отримання даних з публічного API за допомогою requests."""
    
    def __init__(self):
        # Використовуємо безкоштовне API з фактами про котів
        self.api_url = "https://catfact.ninja/fact"

    def get_random_fact(self) -> str:
        try:
            print(f"Відправляємо GET-запит до {self.api_url}...")
            # Робимо запит через встановлену нами бібліотеку requests
            response = requests.get(self.api_url)
            
            # Перевіряємо, чи успішно пройшов запит (статус 200)
            response.raise_for_status()
            
            # Перетворюємо JSON-відповідь у словник Python
            data = response.json()
            return data.get('fact', 'Факт не знайдено.')
            
        except requests.exceptions.RequestException as error:
            return f"Сталася помилка під час запиту: {error}"

if __name__ == "__main__":
    # Створюємо екземпляр класу та викликаємо метод
    fetcher = FactFetcher()
    
    print("\n--- Результат роботи програми ---")
    print(fetcher.get_random_fact())
    print("---------------------------------")