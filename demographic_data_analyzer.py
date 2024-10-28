import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leer el dataset desde un archivo CSV
    df = pd.read_csv('adult.data.csv')

    # 1. ¿Cuántas personas de cada raza están representadas en este dataset?
    race_count = df['race'].value_counts()

    # 2. ¿Cuál es la edad promedio de los hombres?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. ¿Cuál es el porcentaje de personas que tienen un título de Bachillerato?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. ¿Qué porcentaje de personas con educación avanzada (Bachelors, Masters, o Doctorado) gana más de 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] / higher_education.sum()) * 100, 1)

    # 5. ¿Qué porcentaje de personas sin educación avanzada gana más de 50K?
    lower_education_rich = round((df[~higher_education & (df['salary'] == '>50K')].shape[0] / (~higher_education).sum()) * 100, 1)

    # 6. ¿Cuál es el número mínimo de horas que trabaja una persona por semana?
    min_work_hours = df['hours-per-week'].min()

    # 7. ¿Qué porcentaje de las personas que trabajan el número mínimo de horas por semana tienen un salario de más de 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # 8. ¿Qué país tiene el mayor porcentaje de personas que ganan más de 50K?
    country_salary_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    highest_earning_country = (country_salary_counts / country_counts).idxmax()
    highest_earning_country_percentage = round((country_salary_counts / country_counts).max() * 100, 1)

    # 9. ¿Cuál es la ocupación más popular para las personas que ganan más de 50K en India?
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Si se solicita, imprimir los resultados
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
