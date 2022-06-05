from email import message
from django.test import TestCase
    #Import the model
from .models import MyPost

class TestMyApp(TestCase):
    def setUp(self):
        MyPost.objects.create(message='Just 4 test') # create new object 

    def test_message_content(self):
        post=MyPost.objects.get(id=1) #get the created object
        expected_object_name= f'{post.message}' #convert its value to variable
        self.assertEqual(expected_object_name,'Just 4 test')




