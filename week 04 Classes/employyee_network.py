class Employee:
    # class attribute to track current number of employees
    employee_count = 0

    def __init__(self, name, email, hire_date):
        """
        Constructor method for Employee class
        Initializes an Employee object with name, email, and hire date.
        Adjusts the employee_count class attribute when a new employee
            is created.
        """
        self.name = name
        self.email = email
        self.hire_date = hire_date
        Employee.employee_count += 1
        self.posts = list()

    def post_message(self, message):
        post = Post(self, message)
        self.posts.append(message)
        return post


class Post:
    def __init__(self, message, author):
        """
        Constructor method for Post class
        Initializes an Post object with message, author and empty list.
        """
        self.message = message
        self.author = author
        self.comments = list()

    def edit_post(self, new_message):
        self.message = new_message
