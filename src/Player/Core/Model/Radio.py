class Radio:
    def __init__(self, id, title, url, image):
        self.id = id
        self.title = title
        self.url = url
        self.image = image

    @staticmethod
    def from_dictionary(dictionary):
        return Radio(dictionary['id'], dictionary['title'], dictionary['url'], dictionary['image'])