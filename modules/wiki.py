import wikipedia
import pyttsx3
import speech_recognition as speech

engine_speecher = pyttsx3.init("sapi5")
voices_engine = engine_speecher.getProperty("voices")
print(voices_engine)
engine_speecher.setProperty("voice", voices_engine[0])


def __speak__something(audio):
    engine_speecher.say(audio)
    engine_speecher.runAndWait()


__speak__something("Lullaby")


def search_content(topic_to_search):
    """
    @ It will search the topic according to the user
      wants. the topic will pull up from the voice 
      assistant from the user and fetched into this function
          """
    result_wikipedia_search = wikipedia.search(topic_to_search, results=6)
    wikipedia_summary = wikipedia.summary(topic_to_search, sentences=3)
    print(result_wikipedia_search)
    print(wikipedia_summary)
    __speak__something(wikipedia_summary)


search_topic_wiki = str(input("Enter your topic to search > "))
search_content(search_topic_wiki)
