# CREATE THE WEBSCRAPER HERE!
from bs4 import BeautifulSoup
import requests

# pokemon = "pikachu"
# URL = f"https://www.pokemon.com/us/pokedex/{pokemon}"

def get_info(pokemon="pikachu"):
    pokemon = pokemon.lower()

    URL = f"https://pokemondb.net/pokedex/{pokemon}"
    res = requests.get(URL) # GET request to the URL

    soup = BeautifulSoup(res.text, "html.parser") # Parsing the HTML 
    # print(soup.text)
    # print(soup.prettify())
    image = soup.find_all("img")[1]

    basic_info = soup.find_all("p")[0].text
    basic_info1 = soup.find_all("p")[1].text
    basic_info += basic_info1 # merging so we have only one string

    pokedex_data = soup.find("div", class_= "grid-col span-md-6 span-lg-4") # type, species, height, weights?

    base_stats = soup.find("div", class_= "resp-scroll") # hp, attack, defense points?

   
    all_info = {
        "image": image,
        "basic_info": basic_info,
        "pokedex_data": pokedex_data,
        "base_stats": base_stats
    }
    
    return all_info

