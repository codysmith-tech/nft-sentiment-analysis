"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def plot_data(data_clean, working_directory, data_type):
    """
    Plots the wordcloud of the inputted data.

    Parameters
    ----------
    data_clean : str
        One string containing all of the tokenized words..
        
    working_directory : str
        The working directory in which this project is located..
        
    data_type : str
        Either 'all' or 'nft'. For name when writing to file.

    Returns
    -------
    None.

    """
    #Turning off anaconda plots
    # plt.ioff()
    
    #Making directories
    if os.path.isdir(working_directory + '\\wordclouds\\') == False:
        os.mkdir(working_directory + '\\wordclouds')
    
    #Setting words to be eliminated
    stopwords = set(STOPWORDS)
    
    #Generating wordcloud
    wordcloud = WordCloud(width=1600, height=800, stopwords=stopwords, background_color="black").generate(data_clean)
    
    #Plotting wordcloud
    plt.figure(figsize=(20,10),dpi=300,facecolor='k')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(working_directory + f'\\wordclouds\\{data_type}_wordcloud', dpi=300)