import json


class Books:
    def __init__(self, title: str, author: str):
        """
        Initialize a Books object with a title and an author.

        Args:
        - title (str): The title of the book.
        - author (str): The author of the book.
        """
        self.author = author
        self.title = title


# Create a Books object with specific title and author
my_book = Books(title="To Kill a Mockingbird", author="Harper Lee")

# Convert the Books object to a JSON-formatted string
my_book_json = json.dumps(
    {"title": my_book.title, "author": my_book.author}, indent=4, separators=(",", ":")
)

# Print the JSON-formatted string
print(my_book_json)
