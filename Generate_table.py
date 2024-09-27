import csv
from faker import Faker
fake = Faker(locale='uk_UA')
import random

total_records = 2000

male_percentage = 0.60
female_percentage = 0.40

num_males = int(total_records * male_percentage)
num_females = total_records - num_males

records = []

def generate_male_record():
    first_name = fake.first_name_male()
    return {
        'Прізвище': fake.last_name_male(),
        'Ім’я': first_name,
        'По батькові': (fake.first_name_male() + 'ович'),
        'Стать': 'Чоловіча',
        'Дата народження': fake.date_of_birth(minimum_age=16, maximum_age=85),
        'Посада': fake.job(),
        'Місто проживання': fake.city(),
        'Адреса проживання': fake.address(),
        'Телефон': fake.phone_number(),
        'Email': fake.email()
    }

def generate_female_record():
    first_name = fake.first_name_female()
    return {
        'Прізвище': fake.last_name_female(),
        'Ім’я': first_name,
        'По батькові': (fake.first_name_female() + 'івна'),
        'Стать': 'Жіноча',
        'Дата народження': fake.date_of_birth(minimum_age=16, maximum_age=85),
        'Посада': fake.job(),
        'Місто проживання': fake.city(),
        'Адреса проживання': fake.address(),
        'Телефон': fake.phone_number(),
        'Email': fake.email()
    }


for _ in range(num_males):
    records.append(generate_male_record())

for _ in range(num_females):
    records.append(generate_female_record())

random.shuffle(records)

# Запис у файл CSV
with open('people_data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання',
                  'Адреса проживання', 'Телефон', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()
    writer.writerows(records)

print("Файл успішно створено: people_data.csv")