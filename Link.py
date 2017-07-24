class Link:
    def __init__(self, **kwargs):
        self.provider = kwargs.get('provider')
        self.song = kwargs.get('song')
        self.artist = kwargs.get('artist')