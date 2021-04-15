class Radio:
    def __init__(self, id, title, url):
        self.id = id
        self.title = title
        self.url = url

    @staticmethod
    def from_dictionary(dictionary):
        return Radio(dictionary['id'], dictionary['title'], dictionary['url'])