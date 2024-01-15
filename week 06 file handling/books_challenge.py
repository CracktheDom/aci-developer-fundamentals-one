import json


class Books:
    def __init__(self, title: str, author: str):
        self.author = author
        self.title = title


my_book = Books(title="To Kill a Mockingbird", author="Harper Lee")
my_book_json = json.dumps(
    {"title": my_book.title, "author": my_book.author}, indent=4, separators=(",", ":")
)
print(my_book_json)
