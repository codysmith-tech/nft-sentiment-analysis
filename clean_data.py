"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def clean_data(data):
    """
    Tokenizes and cleans inputted data.

    Parameters
    ----------
    data : list
        A list of strings to tokenize.

    Returns
    -------
    data_clean : string
        One string containing all of the tokenized words.

    """
    
    #Instantiating list to append tokenized words to
    data_clean = []
    
    #Tokenizing
    for i in range(len(data)):
        data_clean.append(word_tokenize(data[i]))
    
    #Flattening list of lists
    data_clean = data_clean_list = sum(data_clean, [])
    
    #Getting rid of non words (i.e. punctuation)
    data_clean = [word for word in data_clean if word.isalnum()]
    
    #Converting list of words into one string
    data_clean = " ".join(i for i in data_clean)
    
    return data_clean, data_clean_list