import factory
from accounts.models import User
from django.contrib.auth.hashers import make_password

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    
    email = factory.Sequence(lambda n: "person{}@example.com".format(n))
    password = make_password("TestPass")