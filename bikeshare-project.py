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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #city_req = input('Choose between Chicago, New York City and Washington: ').lower()
    #cities = list(CITY_DATA.keys())
    #while city_req not in cities: 
        #city = input("Choose between Chicago, New York City and Washington: ").lower()
        #if city_req in cities:
           #print("Let's view data from {}".format(city_req.title()))
           #break
    cities = list(CITY_DATA.keys())
    while True:
        city = input('Choose between Chicago, New York City and Washington: ').lower().strip()
        #cities = list(CITY_DATA.keys())
        if city not in cities:
            print('Try again!')
            continue
        else:
            print("Let's view data from {}".format(city.title()))
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    #month_req = input("Choose a month(January, February, ... , June) or all: ").lower()
    #months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    #while month_req not in months:
        #month = input("Try again! Choose a month from January to June: ").lower()
        #if month_req in months:
            #print('You chose {}'.format(month_req.title()))
            #break
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']       
    while True:
      month = input('Choose a month(January, February, ... , June) or all: ').lower().strip()
      if month not in months:
          print('Try again!')
          continue
      else:
        print('You chose {}'.format(month.title()))
        break      
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #day_req = input("Choose a day(Monday, ... , Sunday) or all: ").lower()
    #days = ['all', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'sunday']
    #while day_req not in days:
        #day = input("Try again! Choose a day from Monday to Sunday: ").lower()
        #if day_req in days:
            #print('You chose {}'.format(day_req.title()))
            #break
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']      
    while True:
        day = input("Choose a day(Monday, ... , Sunday) or all: ").lower().strip()
        #days = ['all', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'sunday']
        if day not in days:
            print('Try again!')
            continue
        else:
            print('You chose {}'.format(day.title()))
            break
    
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('The most common month is:', most_common_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of the week is:', most_common_day_of_week)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('The most common start location is:', most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('The most common end location is:', most_common_start)

    # TO DO: display most frequent combination of start station and end station trip
    start_and_end = df['Start Station'] + ' ' + df['End Station']
    most_common_combo = start_and_end.mode()[0]
    print('The most common start and end is:', most_common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time is:', mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('There are {}.'.format(df['User Type'].value_counts()))
    
    # TO DO: Display counts of gender
    try:
        print('There are {}.'.format(df['Gender'].value_counts()))
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_birth = int(df['Birth Year'].min())
        print('The earliest user birth year is {}.'.format(earliest_year_birth))
    except KeyError:
        print("\nEarliest Birth Year:\nNo data available for this month.")
        
    try:
        latest_year_birth = int(df['Birth Year'].max())
        print('The latest user birth year is {}.'.format(latest_year_birth))
    except KeyError:
        print("\nLatest Birth Year:\nNo data available for this month.")
        
    try:
        most_common_year_birth = int(df['Birth Year'].mode()[0])
        print('The most common user birth year is {}.'.format(most_common_year_birth))
    except KeyError:
        print("\nEarliest Birth Year:\nNo data available for this month.")    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    data_view = input('Would you like to see individual trip data(yes/no)?: ').lower().strip()
    l = 0
    while True:
        if data_view == 'yes':
            print(df.iloc[l:(l + 5)])
            l += 5
            view_data = input('\n"Do you wish to continue? Enter yes or no\n').lower().strip()
            if view_data != 'yes':
                break
        else:
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
