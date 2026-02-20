import json
import os
import random
from datetime import datetime, timedelta

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =========================
# ЭТАП 1. Подготовка данных
# =========================

FILE_NAME = "events.json"

def generate_test_data(filename: str, n: int = 500):
    """
    Генерация тестового JSON-файла с событиями информационной безопасности.
    """
    signatures = [
        "SQL Injection",
        "XSS Attempt",
        "Brute Force",
        "Port Scan",
        "Malware Activity",
        "Privilege Escalation",
        "DDoS Attempt"
    ]

    base_time = datetime.now()

    events = []
    for i in range(n):
        event = {
            "event_id": i + 1,
            "timestamp": (base_time - timedelta(minutes=random.randint(0, 10000))).isoformat(),
            "source_ip": f"192.168.1.{random.randint(1, 254)}",
            "destination_ip": f"10.0.0.{random.randint(1, 254)}",
            "signature": random.choice(signatures),
            "severity": random.choice(["Low", "Medium", "High", "Critical"])
        }
        events.append(event)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=4)

    print(f"Файл {filename} успешно сгенерирован.")


# Если файл отсутствует — создаём
if not os.path.exists(FILE_NAME):
    generate_test_data(FILE_NAME)


# =========================
# ЭТАП 2. Анализ данных
# =========================

# Загрузка JSON в DataFrame
df = pd.read_json(FILE_NAME)

# Проверка структуры данных
print("Первые 5 строк данных:")
print(df.head())
print("\nИнформация о датафрейме:")
print(df.info())

# Подсчёт распределения по типам событий (signature)
signature_counts = df["signature"].value_counts()

print("\nРаспределение событий по типам:")
print(signature_counts)


# =========================
# ЭТАП 3. Визуализация данных
# =========================

plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    y="signature",
    order=signature_counts.index
)

plt.title("Распределение типов событий информационной безопасности")
plt.xlabel("Количество событий")
plt.ylabel("Тип события")
plt.tight_layout()

plt.show()