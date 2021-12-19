from bs4 import BeautifulSoup
import requests
web = requests.get("https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(web.text,"html.parser")
movies = soup.find_all(name="h3",class_="title")
with open('movies.txt',mode="a") as file:
    for movie in movies[::-1]:
        file.write(f"{movie.getText()}\n")