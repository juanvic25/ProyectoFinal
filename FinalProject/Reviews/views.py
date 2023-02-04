from django.shortcuts import render
from Movies.models import category, movie
from Reviews.models import review
from datetime import datetime

def createReview(request,id):
    categories_active = category.objects.filter(active = True)
    movie_review = movie.objects.get(id=id)
    if request.method == 'GET':
        review_filter = review.objects.filter(user = request.user.profile, title = movie_review)
        if list(review_filter) == []:
            context = {
                        'categories':categories_active,
                        'movie' : movie_review,
            }
            return render(request,'Reviews/create_review.html',context=context)
        else:
            reviews = review.objects.filter(title = movie_review)
            context= {
                'categories':categories_active,
                'movie' : movie_review,
                'reviews' :reviews,
                'message': 'El Usuario ya ha registrado una reseña de esta Pelicula'
            }
            return render(request,'Reviews/list_reviews.html',context=context)

    elif request.method == 'POST':
        review.objects.create(user= request.user.profile, 
                            summary = request.POST['summary'],
                            score = request.POST['score'],
                            title = movie_review,
                            date = datetime.now().date() )
       
        reviews = review.objects.filter(title = movie_review)
        total = 0
        for review_select in reviews:
            total = total + review_select.score
        total = total / len(reviews)

        movie_review.score = round(total,1)
        movie_review.save()

        context= {
            'categories':categories_active,
            'movie' : movie_review,
            'reviews' :reviews
        }
        return render(request,'Reviews/list_reviews.html',context=context)

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

def deleteReview(request, id, id_movie):
    categories_active = category.objects.filter(active = True)
    if request.method == 'POST':
        movie_review = movie.objects.get(id=id_movie)
        review.objects.get(id=id).delete()
        reviews = review.objects.filter(title = movie_review)
        context= {
            'categories':categories_active,
            'movie' : movie_review,
            'reviews' :reviews
        }
        return render(request,'Reviews/list_reviews.html',context=context)

def updateReview(request, id, id_movie):
    categories_active = category.objects.filter(active = True)
    movie_review = movie.objects.get(id=id_movie)
    review_select = review.objects.get(id=id)
    if request.method == 'GET':
        context = {
                    'categories':categories_active,
                    'movie' : movie_review,
                    'review' : review_select
        }
        return render(request,'Reviews/update_review.html',context=context)
    elif request.method == 'POST':
        review_select.summary = request.POST['summary']
        review_select.score = request.POST['score']
        review_select.date = datetime.now().date()
        review_select.save()
        reviews = review.objects.filter(title = movie_review)

        context= {
            'categories':categories_active,
            'movie' : movie_review,
            'reviews' :reviews
        }
        return render(request,'Reviews/list_reviews.html',context=context)