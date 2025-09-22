from .models import Favorite

def favorites_count(request):
    if request.user.is_authenticated:
        return {"fav_count": Favorite.objects.filter(user=request.user).count()}
    return {"fav_count": 0}
