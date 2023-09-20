import requests
import json
from flask import Flask


class MoviesApi:
    def __init__(self, app:Flask):
        API_KEY = app.config["TMDB_API_KEY"]
        self.HEADERS = {
            "accept": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        
        self.url_get_image = self.get_config_api_images()
        
        
    
    def get_movies_less_high_votes(self):
        vote_avg_start = 7
        vote_avg_end = 10
        vote_count_start = 50
        vote_count_final = 400
        
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&\
            vote_average.gte={vote_avg_start}&vote_average.lte={vote_avg_end}&vote_count.gte={vote_count_start}&vote_count.lte={vote_count_final}"
            
        data_movies = self.get_data_in_dict(url)
        
        return data_movies


    def get_image_movie_selected(self):
        pass

        
    def get_config_api_images(self):
        url = "https://api.themoviedb.org/3/configuration"
        api_config = self.get_data_in_dict(url)
        print(api_config)
        url_get_image = api_config["images"]["secure_base_url"]
        
        return url_get_image
        

    def get_data_in_dict(self, url):
        response = requests.get(url, headers=self.HEADERS)
        response_json = response.json()
        
        return response_json
    
def get_memory(pid, mem_start):
    process = psutil.Process(pid)
    memory = process.memory_info().vms
    print("Memory: ", (memory-mem_start)/1024**2)
    
if __name__ == "__main__":
    import os
    import psutil
    pid = os.getpid()
    process = psutil.Process(pid)
    mem_start = process.memory_info().vms
    print("Memory:", mem_start)
        
    mv = MoviesApi()
    get_memory(pid, mem_start)
    list_movies = mv.get_movies_less_high_votes()
    print(list_movies)
    get_memory(pid, mem_start)

    