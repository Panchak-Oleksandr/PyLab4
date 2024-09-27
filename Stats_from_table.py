import pandas as pd
import datetime
import matplotlib.pyplot as plt

def calculate_age(birthdate):
    today = datetime.date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Обробка CSV файлу
def process_csv(file_path):
    try:
        # Читання CSV файлу
        df = pd.read_csv(file_path, delimiter=';', encoding='utf-8')
        print("Ok")
    except FileNotFoundError:
        print("Помилка: файл CSV не знайдено.")
        return
    except pd.errors.ParserError:
        print("Помилка: проблема при відкритті CSV файлу.")
        return

    # Додавання колонки з віком
    df['Дата народження'] = pd.to_datetime(df['Дата народження'], errors='coerce')
    df['Вік'] = df['Дата народження'].apply(lambda x: calculate_age(x) if pd.notnull(x) else None)

    # Кількість чоловіків і жінок
    gender_counts = df['Стать'].value_counts()
    print(f"Чоловіків: {gender_counts.get('Чоловіча', 0)}, Жінок: {gender_counts.get('Жіноча', 0)}")

    # Побудова діаграми для статі
    gender_counts.plot(kind='bar', color=['blue', 'pink'], title="Кількість співробітників за статтю")
    plt.xlabel('Стать')
    plt.ylabel('Кількість')
    plt.xticks(rotation=0)
    plt.show()

    # Визначення вікових категорій
    categories = {
        'younger_18': df[df['Вік'] < 18],
        '18_45': df[(df['Вік'] >= 18) & (df['Вік'] < 45)],
        '45_70': df[(df['Вік'] >= 45) & (df['Вік'] < 70)],
        'older_70': df[df['Вік'] >= 70]
    }

    # Кількість співробітників у кожній віковій категорії
    age_group_counts = {key: len(value) for key, value in categories.items()}
    print("Кількість співробітників по вікових категоріях:")
    for category, count in age_group_counts.items():
        print(f"{category}: {count}")

    # Побудова діаграми для вікових категорій
    plt.bar(age_group_counts.keys(), age_group_counts.values(), color=['red', 'green', 'blue', 'orange'])
    plt.title("Кількість співробітників по вікових категоріях")
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.show()

    # Кількість чоловіків і жінок у кожній віковій категорії
    for category, group in categories.items():
        gender_in_age_group = group['Стать'].value_counts()
        print(f"{category}: Чоловіків: {gender_in_age_group.get('Чоловіча', 0)}, Жінок: {gender_in_age_group.get('Жіноча', 0)}")

        # Побудова діаграми для кожної вікової категорії за статтю
        gender_in_age_group.plot(kind='bar', color=['blue', 'pink'], title=f"Кількість за статтю у {category}")
        plt.xlabel('Стать')
        plt.ylabel('Кількість')
        plt.xticks(rotation=0)
        plt.show()

# Виклик функції
process_csv('people_data.csv')