"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

import praw

def get_data(subreddit_name, client_id, client_secret, username, password, user_agent):
    """
    Getting title data from Reddit search

    Parameters
    ----------
    search_keyword : str
        A string containing which subreddit to be searched
        
    client_id : str
        ID given by Reddit for API tools
        
    client_secret : str
        Code given by reddit for API tools
        
    username : str
        Username associated with the API tool
        
    password : str
        Password associated with the username
        
    user_agent : str
        The API tool name

    Returns
    -------
    titles : list
        A list from the search containing all relevant titles 

    """
    
    #Creating an instance of reddit
    reddit = praw.Reddit(client_id = client_id,
                         client_secret = client_secret,
                         username = username,
                         password = password,
                         user_agent = password
                         )
    
    #Selecting which subreddit to search
    subreddit = reddit.subreddit(subreddit_name)
    
    #Instantiating list to hold titles
    titles=[]
    
    #Searching subreddit to find titles that contain "NFT"
    for search in subreddit.search('NFT', sort='top', time_filter='all',limit=None):
        if 'NFT' in search.title:
            titles.append(search.title)
            if len(titles) == 1000:
                break
    return titles
            