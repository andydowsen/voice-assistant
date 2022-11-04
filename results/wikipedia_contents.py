import wikipedia


def search_content(topic_to_search):
    """
    @ It will search the topic according to the user
      wants. 
    """
    result_wikipedia_search = wikipedia.search(topic_to_search, result=3)
    print(result_wikipedia_search)
