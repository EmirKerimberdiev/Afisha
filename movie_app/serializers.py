from rest_framework import serializers
from .models import Movie, Director, Review


# ReviewSerializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie stars'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'.split()


# MovieSerializer
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = 'id title description duration director '.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'.split()


# DirectorSerializer
class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, director):
        movies_count = director.movies.count()
        return movies_count


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    review_name = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director reviews review_name rating'.split()

    def get_review_name(self, movie):
        if movie.reviews.exists():
            return movie.reviews.first().text
        return None

    def get_rating(self, movie):
        reviews = movie.reviews.all()
        total_stars = sum(review.stars for review in reviews)
        count = reviews.count()
        return total_stars / count if count > 0 else 0
