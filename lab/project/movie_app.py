from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        user = User(username, age)
        if user in self.users_collection:
            raise Exception("User already exists!")
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        current_user = self.find_user_by_username(username)

        if current_user not in self.users_collection:
            raise Exception("This user does not exist!")

        if current_user == movie.owner:
            if movie in self.movies_collection:
                raise Exception("Movie already added to the collection!")
            else:
                current_user.movies_owned.append(movie)
                self.movies_collection.append(movie)
                return f"{username} successfully added {movie.title} movie."
        else:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        current_user = self.find_user_by_username(username)
        edited = False
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if current_user == movie.owner:
            for key, val in kwargs.items():
                if key == "title":
                    movie.title = val
                    edited = True
                elif key == "year":
                    movie.year = val
                    edited = True
                elif key == "age_restriction":
                    movie.age_restriction = val
                    edited = True
        else:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if edited:
            return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        current_user = self.find_user_by_username(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if current_user == movie.owner:
            current_user.movies_owned.remove(movie)
            self.movies_collection.remove(movie)
            return f"{username} successfully deleted {movie.title} movie."
        else:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    def like_movie(self, username: str, movie: Movie):
        current_user = self.find_user_by_username(username)
        if current_user != movie.owner:
            if movie in current_user.movies_liked:
                raise Exception(f"{username} already liked the movie {movie.title}!")
            movie.likes += 1
            current_user.movies_liked.append(movie)
            return f"{username} liked {movie.title} movie."
        else:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

    def dislike_movie(self, username: str, movie: Movie):
        current_user = self.find_user_by_username(username)
        if movie in current_user.movies_liked:
            movie.likes -= 1
            current_user.movies_liked.remove(movie)
            return f"{username} disliked {movie.title} movie."
        else:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

    def display_movies(self):
        self.movies_collection.sort(key=lambda m: (-m.year, m.title))
        result = ''
        if not self.movies_collection:
            return "No movies found."
        for i in self.movies_collection:
            result += i.details() + '\n'
        return result.strip()

    def __str__(self):
        result = ''
        if not self.users_collection:
            result += "All users: No users."
        else:
            result += "All users: "
            result += f"{', '.join([x.username for x in self.users_collection])}"
            result += '\n'

        if not self.movies_collection:
            result += "All movies: No movies."
        else:
            result += "All movies: "
            result += f"{', '.join([x.title for x in self.movies_collection])}"

        return result.strip()

    def find_user_by_username(self, username):
        for i in self.users_collection:
            if i.username == username:
                return i







