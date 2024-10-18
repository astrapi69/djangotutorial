from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question, Member
from .forms import MemberForm

from django.shortcuts import render, redirect
from .forms import MemberForm

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)

            # Get hidden field data
            address_data = request.POST.get('addressData')
            bank_data = request.POST.get('bankData')

            # Handle saving this data appropriately
            # Example: Save as part of related Address or Bank models (if needed)

            member.save()
            return redirect('member_list')
    else:
        form = MemberForm()

    return render(request, 'polls/add_member.html', {'form': form})


# View to display all members
def member_list(request):
    members = Member.objects.all()  # Fetch all Member instances
    return render(request, 'polls/member_list.html', {'members': members})

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
