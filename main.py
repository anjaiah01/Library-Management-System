from models.library import Library
from models.book import Book
from models.member import Member

def main():
    lib = Library()  # Load library data from JSON (if exists)

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show Books")
        print("6. Show Members")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            lib.add_book(book)
            print(f"Book '{title}' added successfully!")

        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter Member ID: ")
            max_books = int(input("Enter max books allowed: "))
            member = Member(name, member_id, max_books)
            lib.register_member(member)
            print(f"Member '{name}' registered successfully!")

        elif choice == "3":
            member_id = input("Enter Member ID: ")
            isbn = input("Enter Book ISBN: ")
            lib.borrow_book(member_id, isbn)

        elif choice == "4":
            member_id = input("Enter Member ID: ")
            isbn = input("Enter Book ISBN: ")
            lib.return_book(member_id, isbn)

        elif choice == "5":
            lib.show_books()

        elif choice == "6":
            lib.show_members()

        elif choice == "7":
            lib.save_books()
            lib.save_members()
            print("Exiting... Data saved successfully.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
