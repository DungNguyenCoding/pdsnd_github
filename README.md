# Explore US Bikeshare Data

## Overview
In this project, Python is used for exploring data related to bike share systems for three major cities in the United States — Chicago, New York City, and Washington. The  source code is created to import the Bikeshare data and answer interesting questions about it by computing descriptive statistics as well as taking in raw input to create an interactive experience in the terminal to present these statistics.

## Required Software
To complete this project, the following software requirements apply:
* Anaconda with Python 3, NumPy, and Pandas. 
* Text editor, like [Sublime](https://www.sublimetext.com/) or [Atom](https://github.blog/2022-06-08-sunsetting-atom/).
* A terminal application (Terminal on Mac and Linux or Git Bash on Windows).

## US Bikeshare Datasets
There are three city dataset files by selecting randomly data for the first six months of 2017 provided for all three cities:
1. **chicago.csv**
2. **new_york_city.csv**
3. **washington.csv**

All three of the data files contain the same core **six (6)** columns:
* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

![](https://video.udacity-data.com/topher/2018/March/5aa771dc_nyc-data/nyc-data.png)
_Data for the first 10 rides in the new_york_city.csv file_

>The original files are much larger and messier, and you don't need to use them, but they can be accessed here if you'd like to see them [Chicago](https://divvybikes.com/system-data), [New York City](https://citibikenyc.com/system-data), [Washington](ohttps://capitalbikeshare.com/system-data). These files had more columns and they differed in format in many cases.

## Code Walkthrough

### Statistics computed

The project helps users learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics by provide the following information:

1. **Popular times of travel (i.e., occurs most often in the start time)**
   * Most common month
   * Most common day of week
   * Most common hour of day

2. **Popular stations and trip**
   * Most common start station
   * Most common end station
   * Most common trip from start to end (i.e., most frequent combination of start station and end station)

3. **Trip duration**
   * Total travel time
   * Average travel time

4. **User info**
   * Counts of each user type
   * Counts of each gender (only available for NYC and Chicago)
   * Earliest, most recent, most common year of birth (only available for NYC and Chicago)

### An interactive experience
The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are three questions that will change the answers:

1. **Between Chicago, New York City and Washington in which city do you want to display the data?**
2. **Which month do you want to see the data - January, February, March, April, May, June or All?**
3. **Which day of week do you want to see the data - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All?**

The answers to the questions above will determine the city and timeframe on which the data will be analyzed. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

Additionally, any time users are asked for input, there is a chance they may not enter the unexpected one. So the code needs to have the ability to handle unexpected input well without failing, such as anticipating raw input errors like using improper upper or lower case, typos, or users misunderstanding what the expected input is.

Moreover, the script also needs to prompt the user whether they would like to see the raw data. If the user answers 'yes' then the script should print 5 rows of the data at a time, then ask the user if they would like to see 5 more rows of the data. The script should continue prompting and printing the next 5 rows at a time until there is no more data to show or the user chooses 'no' if they do not want any more raw data to be displayed.

## Related Course

[Programming for Data Science with Python](https://learn.udacity.com/nanodegrees/nd104) provided by [Udacity](https://www.udacity.com/)