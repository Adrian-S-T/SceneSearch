class Scene:
    def __init__(self, anime, episode, timestamp, description):
        self.anime = anime
        self.episode = episode
        self.timestamp = timestamp
        self.description = description
    def to_dict(self):
        newdict={
        "anime":self.anime,
        "episode":self.episode,
        "timestamp":self.timestamp,
        "description":self.description
        }
        return newdict