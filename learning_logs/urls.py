# The path function, which is needed when mapping URLs to views
from django.urls import path

# The dot tells Python to import the views.py module from 
# the same directory as the current urls.py module.
from . import views

# The variabel app_name helps Django distinguish this urls.py file from 
# files of the same name in other apps within the project
app_name = 'learning_logs'

# The variable urlpatterns in this module is a list of individual pages
# that can be requested from the learning_logs app
urlpatterns = [
    # The first argument is an empty string ('') which matches the 
    # base URL - http://localhost:8000/. The second argument specifies
    # the function name to call in views.py. The third argument provides
    # the name 'index' for this URL pattern to refer to it later
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
] 