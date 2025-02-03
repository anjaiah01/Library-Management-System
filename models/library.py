from models.book import Book  # Import the Book class
from models.member import Member  # Import the Member class if needed
import json


class Library:
    def __init__(self, books_file="books.json", members_file="members.json"):
        """Initialize library with JSON storage."""
        self.books_file = books_file
        self.members_file = members_file
        self.books = []  # List of Book objects
        self.members = {}  # Dictionary {member_id: Member object}
        self.load_data()  # Load data from JSON on startup

    def add_book(self, book):
        """Adds a book and saves to JSON."""
        self.books.append(book)
        self.save_books()

    def remove_book(self, ISBN):
        """Removes a book and updates JSON."""
        self.books = [book for book in self.books if book.ISBN != ISBN]
        self.save_books()

    def register_member(self, member):
        """Registers a member and saves to JSON."""
        if member.member_id in self.members:
            print(f"Member with ID {member.member_id} already exists!")
        else:
            self.members[member.member_id] = member
            self.save_members()

    def borrow_book(self, member_id, ISBN):
        """Handles book borrowing and updates JSON."""
        if member_id not in self.members:
            print("Member not found!")
            return

        member = self.members[member_id]
        for book in self.books:
            if book.ISBN == ISBN and book.availability:
                if len(member.borrowed_books) < member.borrow_limit:
                    book.mark_borrowed()
                    member.borrow_book(ISBN)
                    self.save_books()
                    self.save_members()
                    print(f"'{book.title}' borrowed by {member.name}.")
                    return
                else:
                    print(f"{member.name} has reached the borrowing limit!")
                    return
        
        print("Book not available or does not exist.")

    def return_book(self, member_id, ISBN):
        """Handles book returning and updates JSON."""
        if member_id not in self.members:
            print("Member not found!")
            return

        member = self.members[member_id]
        for book in self.books:
            if book.ISBN == ISBN:
                if ISBN in member.borrowed_books:
                    book.mark_returned()
                    member.return_book(ISBN)
                    self.save_books()
                    self.save_members()
                    print(f"'{book.title}' returned by {member.name}.")
                    return
                else:
                    print(f"{member.name} did not borrow this book.")
                    return
        
        print("Book not found in the library.")

    def save_books(self):
        """Saves books to JSON file."""
        with open(self.books_file, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def save_members(self):
        """Saves members to JSON file."""
        with open(self.members_file, "w") as f:
            json.dump({mid: member.to_dict() for mid, member in self.members.items()}, f, indent=4)

    def load_data(self):
        """Loads books and members from JSON."""
        try:
            with open(self.books_file, "r") as f:
                book_data = json.load(f)
                self.books = [Book.from_dict(b) for b in book_data]
        except FileNotFoundError:
            self.books = []

        try:
            with open(self.members_file, "r") as f:
                member_data = json.load(f)
                self.members = {mid: Member.from_dict(m) for mid, m in member_data.items()}
        except FileNotFoundError:
            self.members = {}
