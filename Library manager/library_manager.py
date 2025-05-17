import json
import os
LIBRARY_FILE = "library.txt"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            return json.load(f)
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)

def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Book not added.")
        return
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_input == 'yes'
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    })
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_books(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the search keyword: ").strip().lower()
    found_books = []
    for book in library:
        if choice == '1' and keyword in book["title"].lower():
            found_books.append(book)
        elif choice == '2' and keyword in book["author"].lower():
            found_books.append(book)

    if found_books:
        print("Matching Books:")
        display_books(found_books)
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.")
        return
    for idx, book in enumerate(library, start=1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    total = len(library)
    if total == 0:
        print("No books in the library.")
        return
    read_books = sum(1 for book in library if book["read"])
    percentage = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%")

def main():
    library = load_library()
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
