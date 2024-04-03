from pydantic import BaseModel, ValidationError, constr

# task 1
class BookModel(BaseModel):
    name: constr(min_length=3, max_length=30)
    author: str
    year: int


class Book:
    def __init__(self, book_model: BookModel):
        self.book_model = book_model

    def book_info(self):
        return f"Book: {self.book_model.name}, Author: {self.book_model.author}, Year: {self.book_model.year}"

    def __str__(self):
        return self.book_info()

try:
    book_data = {"name": "Dune", "author": "Frank Herbert", "year": 1965}
    book_model = BookModel(**book_data)
    book = Book(book_model)
    print(book.book_info())

except ValidationError as e:
    print("Validation error:", e)


# Ітератор, який дозволяє проходитися по всіх книгах у бібліотеці.
class Library:
    def __init__(self, list_of_books: list[Book]):
        self.list_of_books = list_of_books

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.list_of_books):
            raise StopIteration
        prev_index = self.index
        self.index += 1
        return self.list_of_books[prev_index]



list_of_books = [
    Book(BookModel(name="name 1", author="author 1", year=2022)),
    Book(BookModel(name="name 2", author="author 2", year=2021)),
]
library = Library(list_of_books)

for book in library:
    print(str(book))

print()
for book in library:
    print(str(book))


