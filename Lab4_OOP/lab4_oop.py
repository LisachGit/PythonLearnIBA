from datetime import datetime


class Book:

    book_counter = 0
    current_year = datetime.now().year
    def __init__(self, id, title, authors, publisher, year, pages, price, binding_type):
        self.id = id
        self.title = title
        self.author = authors
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.price = price
        self.binding_type = binding_type
        Book.book_counter += 1

    @property
    def price(self):
       return self._price

    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("Отрицательная цена")
        self._price = value
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value < 0 or value > Book.current_year + 1:
            raise ValueError("Неверная дата издания")
        self._year = value

    @staticmethod
    def valid_year(year, current_year):
        return 0 < year < current_year + 1

    @classmethod
    def get_all_books(cls):
        return cls.book_counter

    def show_book_info(self):
        return f"{self.title} написана {self.author}. Издатель: {self.publisher}. Год издания: {self.year}, кол-во страниц: {self.pages}. Стоимость: {self.price}BYN. Имеет {self.binding_type} переплёт"


if __name__ == "__main__":
    book1 = Book(1,"Декларация Смерти", "Джемма Мелли", "Астрель", 2009, 320, 40, "твёрдый")
    book2 = Book(2, "Метро 2033", "Дмитрий Глуховский", "Литрес", 2005, 651, 55, "твёрдый")
    book3 = Book(3, "Топи", "Дмитрий Глуховский", "Литрес", 2024, 260, 60, "мягкий")

    print(book1.show_book_info())
    print(book2.show_book_info())
    print(book3.show_book_info())

    print("Всего книг в базе: ", Book.get_all_books())

    books = [book1, book2, book3]

    #Список книг заданного автора
    author = "Дмитрий Глуховский"
    book_by_author = [book for book in books if book.author == author]
    print(f"Книги {author}: {[book.show_book_info() for book in book_by_author]}")

    #Список книг, выпущенных после заданного года
    year = 2008
    book_after_year = [book for book in books if book.year > year]
    print(f"Книги, выпущенные после {year}: {[book.show_book_info() for book in book_after_year]}")

