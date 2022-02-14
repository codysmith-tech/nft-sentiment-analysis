# nft-sentiment-analysis

@author: Cody Smith | codysmith.contact@gmail.com

https://github.com/codysmith-data

https://www.linkedin.com/in/codysmithprofile/

------------------------
***OVERVIEW***

This is a Python project on sentiment analysis on NFT's based on Reddit post titles.

The goal of this project is to find the overall sentiment on NFT's from all Reddit users.
To create a comparison for the average Reddit user, the overall sentiment was also found from the specific NFT subreddit.

To achieve this sentiment analysis, I created a script to access the Reddit API, searched for titles that contained "NFT",
and scored each word in each title based on its positivity and negativity.

To also give insight on what words are commonly paired with "NFT", I created word clouds that show words that are highly
associated with that.

------------------------
***GETTING STARTED***

This project was made in a Windows OS.
This project was made in Python 3.8.8.
This project was made in the Anaconda environment.

*Download Anaconda here*

https://www.anaconda.com/products/individual

Please use this setup for best results.

You will also need access to the Reddit API.
This video starts with a great how to on this:

https://www.youtube.com/watch?v=NRgfgtzIhBQ
(Credit to Sentdex / pythonprogramming.net)

Modules needed for this project:

    praw

    nltk

    os

    matplotlib

    wordcloud

Once setup is complete, open main.py in Anaconda.

This is the master for the whole project, and the only file that needs to be opened (specifcally for running the project)

Before running, please set the Reddit API info (lines 25-29) and the working directory (line 32).
This should be the directory that main.py is contained in.

To run the project, press Run (green arrow at the top) or F5.

Wait for the running for the process to complete!

Now check wordclouds and results folders!

------------------------
**Files:**

main.py - master file for running all other files

get_data.py - obtains the data from Reddit

clean_data.py - drops unnecessary data and tokenizes data

analyze_data.py - scores the sentiment of each word and saves the results to a file

plot_data.py - creates wordclouds based around "NFT"


**Folders:**

wordclouds: holds the output wordclouds

results: holds the .txt file containing the results

------------------------
**RESULTS DISCUSSION**

For a create context for how the average Reddit population feels about NFT's, data was pulled from two places: the "all" section of Reddit,
which is like a "front page" of sorts. This was chosen because this place on Reddit covers everything that's popular from all of Reddit.

The second place chose was the specific NFT subreddit. This was chosen to give context on how a smaller population with an interest
in the topic can have wildly different sentiment than the average population.

To give a visual representation of how each location on Reddit feels about the topic, word clouds were created to see which words are commonly
associated with "NFT".

Here is the wordcloud for the NFT subreddit:
![nft_wordcloud](https://user-images.githubusercontent.com/58944210/147141834-fc1fcad1-43d5-41c2-95de-6281cdaeae35.png)
Here we can see words like "cool", "valuable", and "rare".
This can give us an idea of what we can expect for the sentiment in the NFT subreddit.

Here is the wordcloud for all of Reddit:
![all_wordcloud](https://user-images.githubusercontent.com/58944210/147142204-35747fb5-a4f0-4ae8-bdc5-07c2d2321cdf.png)
Now, we can see words like "worthless", "scam", and "bad".
This is quite the contrast from the NFT subreddit.

Now, let's do the sentiment analysis.

The output for the NFT subreddit is:

    Overall Positive

    Positive: 71.0

    Negative: 31.0
  
Here we can see that there's a heavy positive sentiment towards NFT's in the NFT subreddit, which is expected.

The output for all of Reddit is:

    Overall Positive

    Positive: 73.0

    Negative: 72.0

 So, this isn't as negative biased as we might have expected, but looking at the values, it is neck and neck between positive and negative.
 And, there's way more negative sentiment than just in the NFT subreddit.
 
 NFT's are relatively new topic for many people (as of now in Decemeber 2021), and there's bound to be mixed opinions as people are introduced to the topic.
 I think this is shown in the sentiment for all of Reddit.
 
 I am interested in revisiting this topic in the future to see how sentiment changes over time.
