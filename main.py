from Bookshop_books.bookshop_books import BookshopBooks
from Bookshop_books.bookshop import BookShop
from Bookshop_books.book import Book


def print_books_from_each_bookshop(_books_records_list, _bookshop_records_list):
    for bookshop in _bookshop_records_list:
        print("Bookshop: ", bookshop.name)
        for book in sorted(_books_records_list, key=lambda x: x.title):
            if book.bookshop_record_id == bookshop.bookshop_record_id:
                print(book.title, "by", book.author)
        print("-" * 50)


def print_bookshops_by_book_count(_books_records_list, _bookshop_records_list):
    bookshop_books = list()
    for bookshop in _bookshop_records_list:
        counter = 0
        books = list()
        for book in _books_records_list:
            if book.bookshop_record_id == bookshop.bookshop_record_id:
                books.append(book)
                counter += 1
        bookshop_books.append((counter, bookshop.name, books))
    for bookshop in sorted(bookshop_books, key=lambda x: x[0]):
        print("Bookshop: ", bookshop[1])
        for book in bookshop[2]:
            print(book.title, "by", book.author)
        print("Book count:", bookshop[0])
        print("-" * 50)


def print_bookshops_ending_with_books(_bookshop_books_records_list,
                                      _books_records_list, _bookshop_records_list):
    bookshops = [bookshop for bookshop in _bookshop_records_list if bookshop.name[-5:] == "Books"]
    for bookshop in bookshops:
        print("Bookshop:", bookshop.name)
        for bookshops_book_record in _bookshop_books_records_list:
            if bookshop.bookshop_record_id == bookshops_book_record.bookshop_record_id:
                book = _books_records_list[bookshops_book_record.book_record_id - 1]
                print(book.title, "by", book.author)
        print("-" * 50)


def main():
    book_records_list = [
        Book(1, "War and Peace", "Tolstoy", 1),
        Book(2, "Dagon", "Lovecraft", 1),
        Book(3, "Farewell Arms!", "Ernest Hammingw", 2),
        Book(4, "Master and Margarita", "Bulgakov", 3),
        Book(5, "Splinter Cell", "Tom Clansey", 3),
        Book(6, "Wildlands", "Tom Clansey", 3),
        Book(7, "Morphium", "Bulgakov", 4),
    ]
    bookshop_records_list = [
        BookShop("Moscow Tverskaya st.", "Book Labirinth", 1),
        BookShop("Moscow Baumanskay st.", "Good Old Books", 2),
        BookShop("St. Petersburg Leninskay st.", "Peter I's Books", 3)
    ]
    bookshop_books_records_list = [
        BookshopBooks(1, 1),
        BookshopBooks(2, 2),
        BookshopBooks(3, 2),
        BookshopBooks(7, 2),
        BookshopBooks(4, 3),
        BookshopBooks(5, 3),
        BookshopBooks(5, 2),
        BookshopBooks(5, 1)
    ]
    print("---Books from each bookshop-----")
    print_books_from_each_bookshop(book_records_list, bookshop_records_list)
    print("\n---Bookshops sorted by book count---")
    print_bookshops_by_book_count(book_records_list, bookshop_records_list)
    print("\n---Bookshops names ending with 'books'---")
    print_bookshops_ending_with_books(bookshop_books_records_list, book_records_list, bookshop_records_list)


if __name__ == '__main__':
    main()