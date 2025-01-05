import requests
from newspaper.models import Category, Post, Tag


def navigation(request):
    tags = Tag.objects.all()[:12]
    categories = Category.objects.all()[:3]
    trending_posts = Post.objects.filter(
        published_at__isnull=False, status="active"
    ).order_by("-views_count")[:3]
    
    popular_posts = Post.objects.filter(
            published_at__isnull=False , status="active"
        ).order_by("-published_at","-views_count")[:7]

    side_categories = Category.objects.all()[:6]

    recent_posts = Post.objects.filter(
        published_at__isnull=False, status="active"
    ).order_by("-published_at")[:6]
    

    url = 'https://api.openweathermap.org/data/2.5/weather?lat=27.712021&lon=85.312950&appid=6c62ad933476962cee65062e600c5435&units=metric'
    response = requests.get(url)
    weather_data = response.json()    

    
  
  
  
    return{
        "tags" : tags,
        "categories" : categories,
        "trending_posts" : trending_posts,
        "side_categories" : side_categories,
        "popular_posts" : popular_posts,
        "recent_posts" : recent_posts,
        "weather_data" : weather_data,
        }
    