
class Link:
    def __init__(self, **kwargs):
        self.provider = kwargs['provider']
        self.image = kwargs.get('image')
        self.link = kwargs.get('link')
        self.label = kwargs.get('label')
        self.status = kwargs.get('status')
        self.priority = kwargs.get('priority')