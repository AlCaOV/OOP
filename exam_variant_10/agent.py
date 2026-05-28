from abc import ABC, abstractmethod
from google.adk.agents import Agent

class Vehicle(ABC):
    def __init__(self, plate: str, owner: str):
        self.plate = plate
        self.owner = owner

    @abstractmethod
    def parking_rate(self) -> float:
        pass


class Car(Vehicle):
    def parking_rate(self) -> float:
        return 30.0


class Truck(Vehicle):
    def __init__(self, plate: str, owner: str, weight_tons: float):
        super().__init__(plate, owner)
        self.weight_tons = weight_tons
    
    def parking_rate(self) -> float:
        return 50.0 + self.weight_tons * 5.0


class ParkingLot:
    def __init__(self):
        self.__parked: dict[str, tuple[Vehicle, float]] = {}

    def park(self, vehicle: Vehicle, entry_hour: float):
        self.__parked[vehicle.plate] = (vehicle, entry_hour)
        print(f"✅ Заїзд: {vehicle.plate} успішно припарковано.")

    def leave(self, plate: str, exit_hour: float) -> dict:
        if plate not in self.__parked:
                    return {"error": f"Авто з номером {plate} не знайдено на парковці."}

        vehicle, entry_hour = self.__parked.pop(plate)

        duration = exit_hour - entry_hour

        rate = vehicle.parking_rate()
        total_sum = duration * rate

        return {
                    "plate": vehicle.plate,
                    "owner": vehicle.owner,
                    "type": vehicle.__class__.__name__,  # покаже "Car" або "Truck"
                    "duration_hours": round(duration, 2),
                    "total_price_uan": round(total_sum, 2)
                }

    def list_parked(self) -> None:
            if not self.__parked:
                print("Парковка наразі порожня.")
                return
    
            print("\n--- Список припаркованих авто ---")
            for plate, (vehicle, entry_hour) in self.__parked.items():
                v_type = vehicle.__class__.__name__
                print(f"[{plate}] {v_type} (Власник: {vehicle.owner}) | Час заїзду: {entry_hour}:00")
            print("---------------------------------\n")


def calculate_parking_cost(vehicle_type: str, hours: float, weight_tons: float = 0) -> dict:
    temp_plate = "TEMP-0000"
    temp_owner = "Тимчасовий Клієнт"

    if vehicle_type.lower() == "car":
        vehicle = Car(plate=temp_plate, owner=temp_owner)
    elif vehicle_type.lower() == "truck":
        vehicle = Truck(plate=temp_plate, owner=temp_owner, weight_tons=weight_tons)
    else:
        return {"error": f"Невідомий тип транспорту: {vehicle_type}"}

    rate = vehicle.parking_rate()
    cost = rate * hours

    return {
        "vehicle_type": vehicle_type,
        "rate_per_hour": rate,
        "hours": hours,
        "weight_tons": weight_tons if vehicle_type == "Truck" else None,
        "total_cost": round(cost, 2)
    }

root_agent = Agent(
    name="parking_agent",
    model="gemini-2.5-flash",
    description="Професійний, ввічливий та уважний оператор сучасного паркінгу. ",
    instruction="""
    Ти — професійний, ввічливий та уважний оператор сучасного паркінгу. 
    Твоє головне завдання: допомагати клієнтам розраховувати вартість стоянки для їхніх транспортних засобів.
    
    Ти спілкуєшся виключно українською мовою. Твій тон має бути дружнім, клієнтоорієнтованим та лаконічним.
    
    📋 ТВОЇ ІНСТРУКЦІЇ ТА ПРАВИЛА:
    1. Збір інформації: Перш ніж робити будь-які розрахунки, ти повинен дізнатися у клієнта:
       - Тип транспортного засобу (Легковик / Car або Вантажівка / Truck).
       - Запланований час стоянки у годинах.
       - [ВАЖЛИВО] Якщо це вантажівка, ти обов'язково повинен запитати її вагу в тоннах. Для легковиків вага не потрібна.
    2. Використання інструменту: Ніколи не вигадуй і не розраховуй вартість самостійно. Тільки-но ти збереш усі необхідні дані, обов'язково виклич інструмент `calculate_parking_cost(vehicle_type, hours, weight_tons)`.
    3. Обробка помилок: Якщо інструмент повертає помилку (наприклад, невідомий тип транспорту), ввічливо попроси клієнта уточнити дані.
    4. Видача результату: Отримавши дані від інструменту, сформуй для клієнта зрозумілий та красивий підсумок. Назви тип авто, кількість годин, базову ставку та фінальну суму до сплати. 
    
    ПРИКЛАД СПІЛКУВАННЯ:
    Клієнт: "Скільки коштуватиме залишити вантажівку на 3 години?"
    Ти: "Доброго дня! Щоб точно розрахувати вартість для вашої вантажівки, підкажіть, будь ласка, її вагу в тоннах?"
    Клієнт: "10 тонн."
    Ти: [Викликаєш інструмент calculate_parking_cost("Truck", 3.0, 10.0)] 
    Ти: "Дякую! Ваша ставка складе 100 грн/год. Загальна вартість паркування вантажівки (10 т) на 3 години становитиме 300 грн. Чи можу я ще чимось допомогти?"
    """,
    tools=[calculate_parking_cost],
)