import pandas as pd


def calculate_demographic_data(print_data=True):
    # Load the dataset
    df = pd.read_csv('adult.data.csv')

    # Q1: How many people of each race are represented?
    race_count = df['race'].value_counts()

    # Q2: Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Q3: Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1
    )

    # Q4 & Q5: Advanced education = Bachelors, Masters, or Doctorate
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Percentage with advanced education earning >50K
    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').sum() /
        higher_education.sum() * 100, 1
    )

    # Percentage without advanced education earning >50K
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').sum() /
        lower_education.sum() * 100, 1
    )

    # Q6: Minimum hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # Q7: Percentage of people working minimum hours who earn >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').sum() /
        len(num_min_workers) * 100, 1
    )

    # Q8: Country with highest percentage of people earning >50K
    # Count total people per country
    country_counts = df['native-country'].value_counts()

    # Count >50K earners per country
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()

    # Divide to get percentage, round to 1 decimal
    country_rich_percentage = round(rich_country_counts / country_counts * 100, 1)

    # Get the country with the highest percentage
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = country_rich_percentage.max()

    # Q9: Most popular occupation for >50K earners in India
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

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