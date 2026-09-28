from abc import ABC, abstractmethod


class User(ABC):
    """Abstract base class for every person using the system."""
    # class variable
    users_count = 0

    def __init__(self, name, email):
        if not User.is_valid_email(email):
            raise ValueError("Invalid email address")
        self.name = name
        self._email = email # protected
        User.users_count += 1
        self.user_id = User.users_count

    # Encapsulation is behaviour of class where class controls how its internal data is modified.
    @property  # Encapsulation: We don't directly expose the email. access it through getter
    def email(self):
        return self._email

    @email.setter   # So we can validate the email before changing variable value through setter
    def email(self, value):
        if not User.is_valid_email(value):
            raise ValueError("Invalid email address")
        self._email = value

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    @classmethod
    def get_total_users(cls):
        return User.users_count

    #Every child class provide its own implementation of display_role()
    @abstractmethod
    def display_role(self):
        pass

    # Instance method
    def display_info(self):
        print(f"User ID : {self.user_id}")
        print(f"Name    : {self.name}")
        print(f"Email   : {self.email}")
        print(f"Role    : {self.display_role()}")
