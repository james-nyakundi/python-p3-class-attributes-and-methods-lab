class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls):
        if cls.genre_count.get(self.genre):
            cls.genre_count[self.genre] += 1
        else:
            cls.genre_count[self.genre] = 1

# Test the class
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)  # "99 Problems"
print(ninety_nine_problems.artist)  # "Jay-Z"
print(ninety_nine_problems.genre)  # "Rap"
print(Song.count)  # 1
print(Song.genres)  # ["Rap"]
print(Song.artists)  # ["Jay-Z"]
print(Song.genre_count)  # {"Rap": 1}

