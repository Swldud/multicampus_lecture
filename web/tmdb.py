import requests

API_KEY = '4f60f93631ac7d86713964c854e2c6aa'

URL = 'https://api.themoviedb.org/3/movie/popular'
URL += f'api_key={API_KEY}&language=ko-kr'

res = requests.get(URL).json()

popular_movies = res['results']

print(res)
