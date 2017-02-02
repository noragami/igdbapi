IGDB API
========
## What's this?
It's a Python library/wrapper for accessing [IGDB API](https://www.igdb.com/api). And easy to use!

## How do I use this?
Clone the repository & run `python setup.py develop`. (Or [download](/noragami/igdbapi/archive/master.zip) it & run `python setup.py install`, which copies the code to your local Python packages folder)

Find and install it using pip:
```python
pip install igdbapi
```

You should start with:
```python
[yato@noragami igdbapi]$ python
Python 3.5.2 (default, Nov  7 2016, 11:31:36) 
[GCC 6.2.1 20160830] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

Import and client initialization (with your api key):
```python
>>> import igdbapi
>>> igdbapi.core.APIClient(api_key='your_api_key')
<igdbapi.core.APIClient object at 0x7f2a71166fd0>
```

Then, you can use it like this:
```python
>>> igdbapi.games.Games().meta()
['name', 'slug', 'url', 'created_at', 'updated_at', 'summary', 'storyline', 'regions', 'parent', 'collection', 'franchise', 'hypes', 'rating', 'popularity', 'aggregated_rating', 'rating_count', 'game', 'developers', 'publishers', 'game_engines', 'category', 'time_to_beat', 'time_to_beat.hastly', 'time_to_beat.normally', 'time_to_beat.completely', 'player_perspectives', 'game_modes', 'keywords', 'themes', 'genres', 'first_release_date', 'status', 'release_dates', 'release_dates.category', 'release_dates.platform', 'release_dates.date', 'release_dates.region', 'release_dates.human', 'release_dates.y', 'release_dates.m', 'alternative_names', 'alternative_names.name', 'alternative_names.comment', 'screenshots', 'screenshots.url', 'screenshots.cloudinary_id', 'screenshots.width', 'screenshots.height', 'videos', 'videos.name', 'videos.video_id', 'cover', 'cover.url', 'cover.cloudinary_id', 'cover.width', 'cover.height', 'esrb', 'esrb.synopsis', 'esrb.rating', 'pegi', 'pegi.synopsis', 'pegi.rating']
```

Or maybe even like this:
```python
>>> igdbapi.games.Games().find(16129)
>>> game = _
>>> game.name
'GRANADO ESPADA'
>>> game.summary
'Granado Espada is about discovering new continents during Europe\'s Age of Exploration era between the 1500s and 1700\'s. The Multi character control (MCC) is the most unique feature [...]'
>>> for i in game.alternative_names: print(i.name)
... 
Sword of the New World
Sword of the New World: Granado Espada
Sword 2
```

