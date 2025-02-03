# 📚 Library Management System  || Python OOP's based Application

## 📝 Project Overview  
The **Library Management System** is an Object-Oriented Python application that allows users to manage books and members efficiently. The system supports:  
- Adding new books 📖  
- Registering members 🧑‍🎓  
- Borrowing and returning books ✅  
- Storing data in JSON files for persistence  

This project follows **OOP principles** and implements **inheritance**, where `Student` and `Professor` classes inherit from `Member`.  

---

## 📂 Project Structure  
```bash
Library-Management-System/
│── models/
│   │── book.py         # Defines the Book class
│   │── member.py       # Defines the Member class (base for Student & Professor)
│   │── library.py      # Handles book and member management
│── books.json          # Stores book data
│── members.json        # Stores member data
│── main.py             # Main script to run the system
│── Design.txt          # Project design notes
│── package.json        # Dependencies (if applicable)
│── package-lock.json   # Dependency lock file


## 🔹 Features
✔ Book Management: Add, remove, and update book availability
✔ Member Registration: Register students and professors with borrowing limits
✔ Borrowing System: Students can borrow up to 3 books, Professors up to 5 books
✔ Persistent Storage: Uses JSON for saving books and members data

### 🛠 Installation & Setup
Prerequisites
Python 3.x
pip install json (if not installed)

## Steps to Run
1️⃣ Clone the repository
git clone https://github.com/anjaiah01/Library-Management-System.git
2️⃣ Run the application
python main.py

🎮 Usage Guide
1️⃣ Add Books – Enter book title, author, and ISBN
2️⃣ Register Members – Provide name, ID, and borrowing limit
3️⃣ Borrow Books – Enter member ID and book ISBN
4️⃣ Return Books – Return borrowed books using ISBN
5️⃣ View Books and Members

👨‍💻 Technologies Used
 - Python 🐍
 - OOP Concepts (Encapsulation, Inheritance)
 - JSON Storage

📌 Future Enhancements
✅ Add a Graphical User Interface (GUI)
✅ Implement Database (SQL/NoSQL) storage
✅ Add Admin Dashboard

