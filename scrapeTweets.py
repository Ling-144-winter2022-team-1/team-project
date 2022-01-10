# Contributors: Kelsey Kraus

# To run this file, type the following into the Shell:
#   python3 scrapeTweets.py

# In order to use this script, you need to first install snscrape and the pandas packages. In your bash Shell (not the python interpreter), run:
#   pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
#   pip install pandas


# Imports
import os
import pandas



# Query by text search
# Setting variables to be used to format the command below
tweet_count = 1000
proList = ['he', 'she', 'it', 'him', 'her', 'they', 'them', 'we', 'us', 'you']
search_string = ' who'
start_date = "2021-09-22"
end_date = "2021-09-23"

# You can also filter your searches by username, hashtag, or List names.
# To do this, you can uncomment these lines, and change search_string on line 36 or 40 to the kind of search you'd like:
# 
#username = 'from:' + search_string
#hashtag = '#' + search_string
#listname = 'list:' + search_string

# There are 10 pronoun + who combinations I want to try. Instead of running this program 10 times, changing the pronoun in line 19 each time, I instead loop through a list of pronouns I've initialized on line 18, and automate this process. I use the OS (operating system) library to make a  command-line call with my Python script.

for pronoun in proList:
  search_string2 = '\"' + pronoun + search_string + '\"'
  os.system("snscrape --jsonl --max-results {} --since {} twitter-search '{} until:{}'> pro-who-tweets.json".format(tweet_count, start_date, search_string2, end_date))

# If you don't need to loop through a list, you can use the following command, which relies on the search_string variable set on line 19:
#
#os.system("snscrape --jsonl --max-results {} --since {} twitter-search '{} until:{}'> pro-who-tweets.json".format(tweet_count, start_date, search_string, end_date))  

# Still in the for loop (note the indentation!), I read the .json file into a dataframe so that I can further manipulate it. I use the pandas package, which is a data analysis library, to do this
  tweets_dataframe = pandas.read_json('pro-who-tweets.json', lines=True)

# Uncomment if you want to show the first 5 entries from dataframe in the shell window
# tweets_dataframe.head()

# (Still in the for loop!) Export newly scraped data into a csv file, and print to the screen how many utterances were collected at each step. 
  if len(tweets_dataframe) == 0 :
    print("Tweet Count of ", search_string2, " : 0")
  else:
    tweets_dataframe.to_csv('pro-who-tweets.csv', sep=',', index=False, columns=['date', 'content', 'id', 'url'])
    print("Tweet Count of ", search_string2, " : ", str(len(tweets_dataframe)))