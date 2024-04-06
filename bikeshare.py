import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['all', 'january', 'february', 'march', 'arpil', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
enter = '-> Type here: '

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city (chicago, new york city, washington).
    city = input("Between Chicago, New York City and Washington in which city do you want to display the data?\n{}".format(enter)).lower()
    while city not in cities:
        city = input("Please chooose between Chicago, New York City, Washington\n{}".format(enter)).lower()
        
    # Get user input for month (all, january, february, ... , june).
    month = input("So, which month do you want to see the data in {}?\n{}".format(city.title(),enter)).lower()
    while month not in months:
       month = input("Please chooose either [from January to June] or [All for no month filtering]\n{}".format(enter)).lower()
    
    # Get user input for day of week (all, monday, tuesday, ... sunday).
    day = input("So, which day of week do you want to see the data in {}?\n{}".format(city.title(),enter)).lower()
    while day not in days:
        day = input("Please chooose either [from Monday to Sunday] or [All for no day of week filtering]\n{}".format(enter)).lower()

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
    # Load data file into a dataframe.
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert data in the Start Time column to datetime format.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month data from Start Time column to new column.
    df['month'] = df['Start Time'].dt.month
    
    # Extract day of week data from Start Time column to new column.
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Month filtering.
    if month != 'all':
        # Get integer value of the month variable using the index of the months list.
        month = months.index(month)
        # Filter by month to create the new dataframe.
        df = df[df['month'] == month]
        
    # Day of week filtering.
    if day != 'all':
        # Filter by day of week to create the new dataframe.
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month.
    print("Month with the highest usage is: ", months[df['month'].mode()[0]].title())

    # Display the most common day of week.
    print("Day of week with the highest usage is: ", df['day_of_week'].mode()[0])

    # Display the most common start hour.
    print("The most popular start hour is: ", df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station.
    print("The most popular start station is: ", df ['Start Station'].mode()[0])

    # Display most commonly used end station.
    print("The most popular end station is: ", df ['End Station'].mode()[0])

    # Display most frequent combination of start station and end station trip.
    df['Start & End Station'] = df['Start Station'] + ' and ' + df['End Station']
    print("The most popular combination of start and end station is: ", df ['Start & End Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time.
    print("Total travel time is: ", df['Trip Duration'].sum(),"(seconds) or about", round(df['Trip Duration'].sum()/3600,2),"(hours)")
    
    # Display mean travel time.
    print("Mean travel time is: about", round(df['Trip Duration'].mean(),2),"(seconds) or about", round(df['Trip Duration'].mean()/3600,2),"(hours)")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types.
    print(df['User Type'].value_counts(),"\n")
    
    if ('Gender' in df.columns):
        # Display counts of gender.
        print(df['Gender'].value_counts(),"\n")
        
    if ('Birth Year' in df.columns):
        # Display earliest, most recent, and most common year of birth.
        print("The oldest subscriber or dependent was born in: ", int(df['Birth Year'].min()))
        print("The youngest subscriber or dependent was born in: ", int(df['Birth Year'].max()))
        print("The most popular birth year among subscribers and dependents is: ", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw selected US bikeshare data."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Get user input for displaying raw data.
    display = input('\nWould you like to open the detail data? Enter yes or no.\n{}'.format(enter)).lower()
    
    while display not in ['yes','no']:
        display = input("Please enter yes or no.\n{}".format(enter)).lower()
    
    if display == 'yes':
        start_idx = 0
        end_idx = 5
        display_next = 'yes'
        
        while start_idx < len(df):
            # Display 5 rows of raw data.
            print('\nDetail data from row {} to {}\n'.format(start_idx, end_idx-1))
            print(df.iloc[start_idx:end_idx])
            
            # Get user input for displaying next 5 rows of raw data.
            display_next = input('\nWould you like to open the next data? Enter yes or no.\n{}'.format(enter)).lower()
            
            while display_next not in ['yes','no']:
                display_next = input("Please enter yes or no.\n{}".format(enter)).lower()
                
            if display_next == 'yes':
                # Update start and end index.
                start_idx += 5
                end_idx += 5
                if end_idx > len(df):
                    end_idx = len(df)
            else:
                break
                
        if display_next == 'yes':
            print('\There is no more data to show!\n')

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

        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n{}'.format(enter)).lower()
        # Handle unexpected input for restarting the process.
        while restart not in ['yes','no']:
                restart = input("Please enter yes or no.\n{}".format(enter)).lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
