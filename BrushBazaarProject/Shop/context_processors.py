from . models import Categories

def BrushBazaar_Category(request):
    cat = Categories.objects.all()
    return dict(cat=cat)


