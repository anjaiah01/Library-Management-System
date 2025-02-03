class Book:
    def __init__(self, title, author, ISBN, availability=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability

    def mark_borrowed(self):
        """Marks book as borrowed."""
        self.availability = False

    def mark_returned(self):
        """Marks book as available."""
        self.availability = True

    def to_dict(self):
        """Converts Book object to dictionary for JSON storage."""
        return {
            "title": self.title,
            "author": self.author,
            "ISBN": self.ISBN,
            "availability": self.availability
        }

    @classmethod
    def from_dict(cls, data):
        """Creates Book object from dictionary."""
        return cls(data["title"], data["author"], data["ISBN"], data["availability"])
