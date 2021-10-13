from Bookshop_books.bookshop_books import BookshopBooks
from Bookshop_books.bookshop import BookShop
from Bookshop_books.book import Book


def print_books_from_each_bookshop(_books_records_list, _bookshop_records_list):
    for bookshop in _bookshop_records_list:
        print("Bookshop: ", bookshop.name)
        counter = 1
        for book in _books_records_list:
            if book.bookshop_record_id == bookshop.bookshop_record_id:
                print(counter, "Book: ", book.title, "by", book.author)
                counter += 1


def print_bookshops_with_book_count(_books_records_list, _bookshop_records_list):
    for bookshop in _bookshop_records_list:
        print("Bookshop: ", bookshop.name, end="")
        books_count = 0
        for book in _books_records_list:
            if book.bookshop_record_id == bookshop.bookshop_record_id:
                books_count += book.copies_count
        print(" books count: ", books_count)


def print_author_books_ending_with_y():
    pass


if __name__ == '__main__':
    book_records_list = [
        Book(1, "War and Peace", "Tolstoy", 1, 100),
        Book(2, "Dagon", "Lovecraft", 1, 400),
        Book(3, "Farewell Arms!", "Ernest Hammingway", 2, 300),
        Book(4, "Master and Margarita", "Bulgakov", 3, 120),
        Book(5, "Splinter Cell", "Tom Clansey", 3, 520)
    ]
    bookshop_records_list = [
        BookShop("Moscow Tverskaya st.", "Book Labirinth", 1),
        BookShop("Moscow Baumanskay st.", "Good Old Books", 2),
        BookShop("St. Petersburg Leninskay st.", "Peter I's Books", 3)
    ]
    bookshop_books_records_list = [
        BookshopBooks(1, 1),
        BookshopBooks(2, 1),
        BookshopBooks(3, 2),
        BookshopBooks(4, 3),
        BookshopBooks(5, 3),
        BookshopBooks(5, 2),
        BookshopBooks(5, 1)
    ]
    print("Books from each bookshop")
    print_books_from_each_bookshop(book_records_list, bookshop_records_list)
    print("\nBookshops with book count")
    print_bookshops_with_book_count(book_records_list, bookshop_records_list)