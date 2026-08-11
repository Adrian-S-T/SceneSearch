class Scene:
    def __init__(self, anime, episode, timestamp, description,title_words, desc_words):
        self.anime = anime
        self.episode = episode
        self.timestamp = timestamp
        self.description = description
        self.name_words=title_words
        self.description_words=desc_words
    def to_dict(self):
        newdict={
        "anime":self.anime,
        "episode":self.episode,
        "timestamp":self.timestamp,
        "description":self.description
        }
        return newdict