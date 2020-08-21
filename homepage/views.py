from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Roast_Boast
from homepage.forms import Add_Roast_Boast
from datetime import datetime



# Create your views here.
def homepage(request):
    posts = Roast_Boast.objects.all().order_by('post_date')
    return render(request, 'homepage.html', {"posts": posts})

def add_roast_boast(request):
    if request.method == "POST":
        form = Add_Roast_Boast(request.POST)
        form.save()

        return HttpResponseRedirect(reverse("homepage"))
    form = Add_Roast_Boast()
    return render(request, "genericform.html", {"form": form})

def add_upvote(request, post_id):
    post = Roast_Boast.objects.filter(id =post_id).first()
    post.upvote += 1
    post.save()
    return HttpResponseRedirect(reverse("homepage"))

def add_downvote(request, post_id):
    post = Roast_Boast.objects.filter(id =post_id).first()
    post.downvote -= 1
    post.save()
    return HttpResponseRedirect(reverse("homepage"))

def roasts(request):
    posts = Roast_Boast.objects.filter(is_boast=False).order_by('post_date')
    return render(request, 'roast.html', {"posts": posts})

def boasts(request):
    posts = Roast_Boast.objects.filter(is_boast=True).order_by('post_date')
    return render(request, 'boast.html', {"posts": posts})

def top_votes(request):
    posts = sorted(Roast_Boast.objects.all(), key=lambda sort: sort.total, reverse=True)
    return render(request, 'sorted.html', {"posts": posts})
    