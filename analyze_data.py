"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

import os
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def sentiment_score(a, b):
    """
    Scoring the overall sentiment of a list of words.
    
    Parameters
    ----------
    a : int
        A summation of the positive scoring of words in a list.
        
    b : int
        A summation of the negative scoring of words in a list.

    Returns
    -------
    overall : string
              The overall sentiment of the words in a list.

    """
    
    if (a>b):
        overall = 'Overall Positive'
    elif (b>a):
        overall = 'Overall Negative'
        
    return overall
        

def analyze_data(data_list, working_directory, data_type):
    """
    Finding the overall sentiment of the words in data_list.

    Parameters
    ----------
    data_list : list
        A list of words to find overall sentiment of.
        
    working_directory : str
        The working directory in which this project is located.

    Returns
    -------
    None.

    """
    
    #Making directories
    if os.path.isdir(working_directory + '\\results\\') == False:
        os.mkdir(working_directory + '\\results')
        
    sentiments = SentimentIntensityAnalyzer()
    
    #Rating each word's sentiment
    positive = [sentiments.polarity_scores(i)['pos'] for i in data_list]
    negative = [sentiments.polarity_scores(i)['neg'] for i in data_list]
    
    #Summing up the sentiment of each type
    x = sum(positive)
    y = sum(negative)
    
    #Scoring overall sentiment based on type's weight 
    overall = sentiment_score(x, y)
    
    #Writing results to text file
    with open(working_directory + f'\\results\\{data_type}_results.txt', 'w') as results:
        results.write(f'{overall}\n')
        results.write(f'Positive: {x}\n')
        results.write(f'Negative: {y}\n')