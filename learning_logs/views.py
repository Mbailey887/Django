from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

# Create your views here.

# When a URL request matches the pattern we just defined,
# Django looks for a function called index() in the views.py file.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data sumitted; create a blank form(create an instance of TopicForm).
        # Because we included no arguments when initiating TopicForm, Django
        # creates a blank form that the user can fill out.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        # We make an instance of TopicForm and pass it the data entered by the user,
        # stored in the request.POST.
        form = TopicForm(data=request.POST)
        #The is_valid() method checks that all required fields have been filled
        # in (all fields in a form are required by default) and that the data entered
        # matches the field types expected
        if form.is_valid():
            # Write the data from the form to the database
            form.save()
            # Redirect the user's browser to the topics page
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)