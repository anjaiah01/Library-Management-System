class Member:
    def __init__(self, name, member_id, borrow_limit):
        self.name = name
        self.member_id = member_id
        self.borrow_limit = borrow_limit
        self.borrowed_books = []

    def borrow_book(self, ISBN):
        """Adds book to borrowed list."""
        self.borrowed_books.append(ISBN)

    def return_book(self, ISBN):
        """Removes book from borrowed list."""
        self.borrowed_books.remove(ISBN)

    def to_dict(self):
        """Converts Member object to dictionary for JSON storage."""
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrow_limit": self.borrow_limit,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        """Creates Member object from dictionary."""
        member = cls(data["name"], data["member_id"], data["borrow_limit"])
        member.borrowed_books = data["borrowed_books"]
        return member
