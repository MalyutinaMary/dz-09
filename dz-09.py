import json
import os
import random
from datetime import datetime, timedelta

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================
# ЭТАП 1. Подготовка данных
# ==========================

FILE_NAME = "events.json"

# Если файл отсутствует — сгенерируем тестовые данные
if not os.path.exists(FILE_NAME):
    print("Файл events.json не найден. Генерация тестовых данных...")

    signatures = [
        "MALWARE-CNC Win.Trojan.Jadtre outbound connection",
        "ET SCAN Nmap Scripting Engine User-Agent Detected",
        "SQL Injection Attempt",
        "ET POLICY Suspicious inbound to MSSQL port 1433",
        "ET DOS Possible SYN Flood",
        "ET WEB_SERVER Possible CVE Exploit Attempt"
    ]

    events = []
    base_time = datetime.now()

    for i in range(300):  # количество событий
        event = {
            "timestamp": (base_time - timedelta(minutes=i)).isoformat(),
            "signature": random.choice(signatures)
        }
        events.append(event)

    data = {"events": events}

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Тестовые данные успешно сгенерированы.\n")


# ==========================
# ЭТАП 2. Анализ данных
# ==========================

# Загрузка JSON-файла
with open(FILE_NAME, "r", encoding="utf-8") as f:
    data = json.load(f)

# Преобразование в DataFrame
df = pd.DataFrame(data["events"])

# Проверка структуры данных
print("Первые 5 строк датасета:")
print(df.head(), "\n")

# Анализ распределения по типам событий
signature_counts = df["signature"].value_counts()

print("Распределение событий по типам:")
print(signature_counts, "\n")


# ==========================
# ЭТАП 3. Визуализация данных
# ==========================

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="signature", order=signature_counts.index)

plt.title("Распределение типов событий информационной безопасности")
plt.xlabel("Тип события (signature)")
plt.ylabel("Количество событий")

plt.xticks(rotation=60, ha="right")
plt.tight_layout()
plt.show()
