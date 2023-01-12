from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# monthly challanges object
monthly_challenge = {
    "january": "Do pushups for at least 20 minutes every day",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Do pushups for at least 20 minutes every day",
    "may": "Walk for at least 20 minutes every day",
    "june": "Learn Django for at least 20 minutes every day",
    "july": "Do pushups for at least 20 minutes every day",
    "august": "Walk for at least 20 minutes every day",
    "september": "Learn Django for at least 20 minutes every day",
    "october": "Do pushups for at least 20 minutes every day",
    "november": "Walk for at least 20 minutes every day",
    "december": None,
}
# Create your views here.


def index(request):

    months = list(monthly_challenge.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]

    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenges_text = monthly_challenge[month]
        return render(request, "challenges/challenge.html", {
            "text": challenges_text,
            "month_name": month,
        })
    except:
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)
