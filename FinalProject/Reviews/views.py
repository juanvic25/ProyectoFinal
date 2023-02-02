from django.shortcuts import render
from Reviews.forms import reviewForm
from Movies.models import category, movie
from Reviews.models import review

def createReview(request):
    categories_active = category.objects.filter(active = True)
    if request.method == 'GET':
        context = {
                    'categories':categories_active,
                    'form':reviewForm()
        }
        return render(request,'Reviews/create_review.html',context=context)
    elif request.method == 'POST':
        form = reviewForm(request.POST)
        if form.is_valid():
            review.objects.create(
                user        = request.user.profile,
                summary     = form.cleaned_data['summary'],
                score       = form.cleaned_data['score'],
                title       = form.cleaned_data['title']
            )
            context = {
                        'categories':categories_active,
                        'form':reviewForm()
            }
            return render(request,'Reviews/create_review.html',context=context)
        else:
            context = {
                        'categories':categories_active,
                        'form':reviewForm(),
                        'errors': form.errors
            }
            return render(request,'Reviews/create_review.html',context=context)

def listReviews (request,id):
    categories_active = category.objects.filter(active = True)
    movie_review = movie.objects.get(id=id)
    reviews = review.objects.filter(title = movie_review)
    context= {
        'categories':categories_active,
        'movie' : movie_review,
        'reviews' :reviews
    }
    return render(request,'Reviews/list_reviews.html',context=context)
