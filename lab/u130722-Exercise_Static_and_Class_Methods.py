# Exercise: Static and Class Methods

# 1
# from math import ceil
#
#
# class PhotoAlbum:
#     PHOTOS_PER_PAGE = 4
#
#     def __init__(self, pages):
#         self.pages = pages
#         self.photos = self.build_photos()
#
#     def build_photos(self):
#         result = []
#         for i in range(self.pages):
#             result.append([])
#         return result
#
#     @classmethod
#     def from_photos_count(cls, photos_count):
#         pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
#         return cls(pages)
#
#     def add_photo(self, label):
#         for row, page in enumerate(self.photos):
#             if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
#                 page.append(label)
#                 return f"{label} photo added successfully on page {row + 1} slot {len(page)}"
#         return "No more free slots"
#
#     def display(self):
#         delimiter = '-' * 11
#         result = delimiter + '\n'
#         for page in self.photos:
#             page_str = ' '.join(['[]' for _ in page])
#             result += page_str + '\n' + delimiter + '\n'
#         return result.strip()
#
#
# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())

# -----------------------------------------------------------------

# 2
# from project_10.customer import Customer
# from project_10.dvd import DVD
# from project_10.movie_world import MovieWorld
#
# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
#
# print(movie_world)


# 3
# from project_10.category import Category
# from project_10.document import Document
# from project_10.storage import Storage
# from project_10.topic import Topic
#
# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project_10")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)


# 4
from project_11.customer import Customer
from project_11.equipment import Equipment
from project_11.exercise_plan import ExercisePlan
from project_11.gym import Gym
from project_11.subscription import Subscription
from project_11.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))













