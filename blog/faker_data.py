from .models import Blog, Category
from faker import Faker

def run():
    fake = Faker(["tr-TR"])
    categories = ("Cooking", "Science", "Politics", "Sports")
    
    for category in categories:
        new_category = Category.objects.create(name=category)
        for _ in range(50):
            Blog.objects.create(category = new_category, title= fake.name(), content = fake.text())
    print("FINISHED")