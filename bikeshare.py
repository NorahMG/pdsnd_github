import time
import pandas as pd
import numpy as np

# This project you will be working with 3 types of city data and analyze them.

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('witch city you want to exolore, Chicago, New York, or Washington?\n').title()
        if city not in CITY_DATA.keys():
            print('\n Invalid Input, please try again')
            continue
        else:
            break
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']  
    while True:
        month = input('Would you like to filter the data for specific month or all?\n').lower()
        if month not in months:
            print('\n Invalid Input, please try again')
            continue
        else:
            break
    days = ['all' ,'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]     
    while True:
        day = input('Would you like to filter the data for specific day of week or all?\n').lower()
        if day not in days:
            print('\n Invalid Input, try again')
            continue
        else:
            break
 HEAD
      
    print('-'*40)
refactoring
    
    return city, month, day

def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("Would you like to see the whole data or only 5 rows? yes or no\n").lower() 
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[0:6]) 
            raw = input("Would you like to see 5 more data?\n").lower() 
            
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

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
    df = pd.read_csv(CITY_DATA[city])

   
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]

    common_day = df['day_of_week'].mode()[0]

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print('the most common month: {}, the most common day: {}, the most common hour: {}'.format(common_month, common_day, common_hour))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    frequent_stations = df.groupby(['Start Station'])['End Station'].value_counts().mode

    print('\nThe most comminly used start station: {}, the most commonly used end station: {}, the most frequent combination: {}'.format(start_station, end_station, frequent_stations))
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()

    print('\nTotal travel time: {}, mean travel time: {}'.format(total_travel, mean_travel))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    try:
            user_types = df['User Type'].value_counts()
            print('User type:', user_types)            
    except:
            print('There is no data available here')
  
    try:
          gender = df['Gender'].value_counts()
          print('Gender type:', gender)
    except:
            print('There is no data available here')

    try:
          earliest_year = df['Birth Year'].min()
          print('Earliest year:', earliest_year)
    except:
            print('There is no data available here')

    try:
          most_recent_year = df['Birth Year'].max()
          print('most recent year:', most_recent_year)
    except:
            print('There is no data available here')      

    try:
          most_common_year = df['Birth Year'].mode()
          print('most common year:', most_common_year)
    except:
            print('There is no data available here')  
            
    # TO DO: Display counts of user types
            
    # TO DO: Display counts of gender

    # TO DO: Display earliest, most recent, and most common year of birth

 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
