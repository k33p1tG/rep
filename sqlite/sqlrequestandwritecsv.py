import sqlite3
import csv

# Подключение к базе данных SQLite
conn = sqlite3.connect(r'C:\Users\Acer\Desktop\Ортем\selfwork\zapchasti\Evroavtoopt\repmain\OptEA.db')
cursor = conn.cursor()

# Выполнение SQL-запроса для выборки данных
cursor.execute("SELECT Info FROM eanona WHERE Info LIKE '%10W40%'")

# Получение результатов запроса
rows = cursor.fetchall()

# Запись результатов в CSV файл
with open(r'C:\Users\Acer\Desktop\Ортем\selfwork\zapchasti\Evroavtoopt\repmain\SAE.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in rows:
        csvwriter.writerow(row)

# Закрытие соединения с базой данных
conn.close()






