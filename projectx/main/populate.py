import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','main.settings')
import django
django.setup()

# FAKE POPUPULATE SCRIPTS
import random
from projectx_app.models import Blog, Description, AccessRecord
from faker import Faker

fakegen = Faker()
blogs =['Find Me If You Can', '10 Minutes To Summer', 'Perang Subuh Di Manila & Jakarta', 'Kemana Kita Pergi', 'Kucing Ku Kahwin Lari']

def add_blog():
    b = Blog.objects.get_or_create(blog_name=random.choice(blogs))[0]
    b.save()
    return b

def populate(N=5):
    for entry in range(N):

        # get topic for the entry
        blogger = add_blog()

        # create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create new choice webpage entry. sebab dia foreign key, panggil balik topic
        desc = Description.objects.get_or_create(blog=blogger, description=fake_name)[0]

        # create a fake access record for that webpage. sebab dia foreign key, panggil balik webpg
        acc_rec = AccessRecord.objects.get_or_create(description=desc, date=fake_date)[0]

if __name__=='__main__':
    print("populating scripts!")
    populate(20)
    print("hoo yeahh. populating complete!")
