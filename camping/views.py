from django.shortcuts import render,redirect
from .models import Camp, Review
from .forms import CampForm, ReviewForm
from django.core.files.storage import FileSystemStorage
from django.db.models import Q


def camp_list(request):
    camps = Camp.objects.all()
    return render(request, 'camp/camp_list.html', {'camps': camps})

def camp_detail(request, pk):
    camp = Camp.objects.get(pk=pk)
    return render(request, 'camp/camp_detail.html', {'camp': camp})
    review =Review.objects.get(pk=pk)

def camp_create(request):
    if request.method == 'POST':
        # add request.FILES to get images to show up
        form = CampForm(request.POST, request.FILES)
        if form.is_valid():
            camp = form.save()
            return redirect('camp_detail', pk=camp.pk)
    else:
        form = CampForm()
    return render(request, 'camp/camp_form.html', {'form': form})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'camp/review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    return render(request, 'camp/review_detail.html', {'review': review})

def review_create(request, pk):
    review =Camp.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review= form.save(commit=False)
            review.camp_id = pk
            review=form.save()
            # review = form.save()
            # camp = review.camp_id
            return redirect('camp_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'camp/review_form.html', {'form': form})



