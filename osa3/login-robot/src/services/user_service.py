from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)
        self.short_username(username)
        self.valid_username(username)
        self.short_password(password)
        self.valid_password(password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
    
    def short_username(self, username):
        if len(username) < 3:
            raise UserInputError("Username too short")
        
    def valid_username(self, username):
        if re.match("^[a-z]+$", username):
            0 == 0
        else:
            raise UserInputError("Username contains invalid characters")
        
    def short_password(self, password):
        if len(password) < 8:
            raise UserInputError("Password too short")
        
    def valid_password(self, password):
        if re.match("^[a-z]+$", password):
            raise UserInputError("Password too weak")
        
    
            
