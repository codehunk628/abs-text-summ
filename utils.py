from bs4 import BeautifulSoup
import re
def text_cleaner(text,contractions,stop_words,isSummary=False):
    """
    Cleans the text/summary by removing hyperlinks, blank spaces,stop_words etc
    
    Parameters:
        Expects text(str), contraction_mapping(dict), stop_words(set/list),isSummary(bool)

    Returns:
        A Cleaned Text String  


    """
    text = text.lower() #lower everything
    text = BeautifulSoup(text,'lxml').text  #remove hyperlinks
    text = ' '.join([contractions[t] if t in contractions else t for t in text.split(' ')]) #expanding contractions
    text = re.sub('"','',text) #remove double quotes
    text = re.sub("'","",text) #remove single quotes
    text = re.sub("^[a-zA-Z]"," ",text) #keeping only alpha numeric characters
    tokens = list()
    if not isSummary:
        tokens = [words for words in text.split(" ") if words not in stop_words] #remove stop_words
    else:
        tokens = [words for words in text.split(" ")]

    cleaned_text = list()
    for token in tokens:
        if len(token)>1:
            cleaned_text.append(token)
    cleaned_text = (" ".join(cleaned_text)).strip()
    return cleaned_text

