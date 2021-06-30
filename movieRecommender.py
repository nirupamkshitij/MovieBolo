
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP


def scrapAndProcess(emotion):           # Function for scraping and processing

    url = ""

    
    if(emotion == "sad"):
        url = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "disgust"):
        url = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "anger"):
        url = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "anticipation"):
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "fear"):
        url = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "enjoyment"):
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "trust"):
        url = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "surprise"):
        url = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

    movies = []

    # Try catch block to prevent abrupt termination of code if IMDb server is down
    try:
        # If entered emotion is not from one of the above, return empty movies list
        if not url:
            return movies

        # HTTP request to get the data of the whole page
        response = HTTP.get(url)

        # Accessing the text property of the response object
        data = response.text

        # Parsing the data using BeautifulSoup
        soup = SOUP(data, "lxml")

        flags = ["None", "X", "\n"]

        # Extract movie titles from the data using regex
        for movieName in soup.findAll('a', attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}):

            movieName = str(movieName.string)

            if movieName not in flags:
                movies.append(movieName)

    # Catch exceptions - they might occur if the IMDb server is down
    except Exception as e:
        print(e)

    return movies

if __name__ == '__main__':

    emotion = input("Enter Your emotion: ").lower()

    movies = scrapAndProcess(emotion)

    if not movies:
        print("Please enter from one of the available emotions")

    for count, movie in enumerate(movies):
        if count == 10:
            break
        print(movie)
