from prettytable import PrettyTable
import urllib.parse
import requests

#insert below your own api read token (v4 auth) from the The Movie Database
readtoken = ""
main_api = "https://api.themoviedb.org/3/search/movie?"


while True:
    
    #ask the user for a movie title, entering q wil quit the python program
    print("Search a movie")
    movie = input('Movie title: ')
    if movie =='q':
            exit()

    #if input field is left blank display error message and ask again for input
    while not movie:
        print("A movie title is needed to search for a movie or typ q to quit")
        movie = input('Movie title: ')
        if movie =='q':
            exit()

    #constructing the request URL and adding headers for authentication to the request
    my_headers = {'Authorization': 'Bearer ' + readtoken}
    url = main_api + urllib.parse.urlencode({"query":movie}) 
    json_data = requests.get(url, headers=my_headers).json()

    #uncomment the line below to print the constructed URL for testing or troubleshooting purposes 
    #print("URL: " + (url))

    #check if there are movies found else display an error message
    if json_data["total_results"] == 0:
        print("No movies with this title were found!")

    else:
        #print the total amount of movies found
        print("Total movies found: " + str(json_data["total_results"]))

        #constructing output table and adding column names
        table = PrettyTable()
        table.field_names = ["Movie title", "Release Date", "Popularity"]

        #loop through the found movies and add their title, release date and popularity into output table
        for movie in json_data["results"]:
            table.add_row([movie["title"], movie["release_date"], round(movie["popularity"])])
    
        #print output table
        print(table)
