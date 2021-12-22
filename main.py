"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

from get_data import get_data
from clean_data import clean_data
from plot_data import plot_data
from analyze_data import analyze_data

def main():
    """
    This is the controller script for all other scripts in this project.

    Returns
    -------
    None.

    """

    #Setting Reddit API info
    client_id = 'INSERT CLIENT ID HERE'
    client_secret = 'INSERT CLIENT SECRET CODE HERE'
    username = 'INSERT USERNAME HERE'
    password = 'INSERT PASSCODE HERE'
    user_agent = 'INSERT REDDIT PROJECT NAME HERE'
    
    #Setting working directory
    working_directory = r'C:\Users\crsmi\OneDrive\Documents\Projects\nft-sentiment-analysis'
    
    #Getting Reddit titles to use
    nft_titles = get_data('nft', client_id, client_secret, username, password, user_agent)
    
    all_titles = get_data('all', client_id, client_secret, username, password, user_agent)
    
    #Cleaning text from titles
    nft_titles, nft_titles_list = clean_data(nft_titles)
    
    all_titles, all_titles_list = clean_data(all_titles)
    
    #Plotting wordclouds
    plot_data(nft_titles, working_directory, 'nft')
    
    plot_data(all_titles, working_directory, 'all')
    
    #Analyzing sentiment
    analyze_data(nft_titles_list, working_directory, 'nft')
    
    analyze_data(all_titles_list, working_directory, 'all')
    

if __name__ == "__main__":
    main()
