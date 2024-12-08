from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MovieReviewSerializer


# Movie List API View
@api_view(http_method_names=['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    # list_ = []
    # for director in directors:
    #     list_.append(
    #         model_to_dict(director)
    #     )
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    movie = Movie.objects.get(id=id)
    data = MovieSerializer(movie).data
    return Response(data=data)


# Director List API View
@api_view(http_method_names=['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(instance=directors, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def director_detail_api_view(request, id):
    director = Director.objects.get(id=id)
    data = DirectorSerializer(director).data
    return Response(data=data)


# Review List API View
@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(instance=reviews, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_api_view(request, id):
    review = Review.objects.get(id=id)
    data = ReviewSerializer(review).data
    return Response(data=data)


# Movie with Review List API View
@api_view(http_method_names=['GET'])
def movie_review_list_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


