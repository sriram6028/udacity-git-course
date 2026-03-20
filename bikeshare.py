import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington)
    while True:
        city = input('\nWhich city would you like to explore? '
                     'Chicago, New York City, or Washington?\n').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid input. Please enter Chicago, New York City, or Washington.')

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('\nWhich month would you like to filter by? '
                      'January, February, March, April, May, June, or "all"?\n').lower()
        if month in months:
            break
        else:
            print('Invalid input. Please enter a valid month or "all".')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('\nWhich day would you like to filter by? '
                    'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or "all"?\n').lower()
        if day in days:
            break
        else:
            print('Invalid input. Please enter a valid day or "all".')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time into new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = months[df['month'].mode()[0] - 1].title()
    print(f'Most Common Month: {most_common_month}')

    # Display the most common day of week
    most_common_day = df['day_of_week'].mode()[0].title()
    print(f'Most Common Day of Week: {most_common_day}')

    # Display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print(f'Most Common Start Hour: {most_common_hour}:00')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print(f'Most Common Start Station: {most_common_start}')

    # Display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print(f'Most Common End Station: {most_common_end}')

    # Display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' --> ' + df['End Station']
    most_common_trip = df['trip'].mode()[0]
    print(f'Most Common Trip: {most_common_trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time (in hours, minutes, seconds)
    total_seconds = int(df['Trip Duration'].sum())
    total_hours = total_seconds // 3600
    total_minutes = (total_seconds % 3600) // 60
    total_secs = total_seconds % 60
    print(f'Total Travel Time: {total_hours}h {total_minutes}m {total_secs}s')

    # Display mean travel time (in minutes and seconds)
    mean_seconds = int(df['Trip Duration'].mean())
    mean_minutes = mean_seconds // 60
    mean_secs = mean_seconds % 60
    print(f'Mean Travel Time: {mean_minutes}m {mean_secs}s')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type Counts:')
    print(user_types.to_string())

    # Display counts of gender (only available for Chicago and New York City)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nGender Counts:')
        print(gender_counts.to_string())
    else:
        print('\nGender data not available for this city.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f'\nEarliest Birth Year:    {earliest_year}')
        print(f'Most Recent Birth Year: {most_recent_year}')
        print(f'Most Common Birth Year: {most_common_year}')
    else:
        print('\nBirth year data not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
