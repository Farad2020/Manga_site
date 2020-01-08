from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
genres = (
    ("Action", "Action"), ("Adventure", "Adventure"), ("Comedy", "Comedy"), ("Cyberpunk", "Cyberpunk"),
    ("Demons", "Demons"), ("Drama", "Drama"), ("Ecchi", "Ecchi"), ("Fantasy", "Fantasy"),
    ("Game", "Game"), ("Harem", "Harem"), ("Hentai", "Hentai"), ("Historical", "Historical"),
    ("Horror", "Horror"), ("Isekai", "Isekai"), ("Josei", "Josei"), ("Kids", "Kids"), ("Magic", "Magic"),
    ("Martial Arts", "Martial Arts"), ("Mecha", "Mecha"), ("Military", "Military"), ("Music", "Music"),
    ("Mystery", "Mystery"), ("Parody", "Parody"), ("Police", "Police"), ("Post-Apocalyptic", "Post-Apocalyptic"),
    ("Psychological", "Psychological"), ("Reverse Harem", "Reverse Harem"), ("Romance", "Romance"),
    ("School", "School"), ("Sci-Fi", "Sci-Fi"), ("Seinen", "Seinen"), ("Shoujo", "Shoujo"),
    ("Shoujo-ai", "Shoujo-ai"), ("Shounen", "Shounen"), ("Shounen-ai", "Shounen-ai"), ("Slice of Life", "Slice of Life"),
    ("Space", "Space"), ("Sports", "Sports"), ("Super Power", "Super Power"), ("Supernatural", "Supernatural"),
    ("Tragedy", "Tragedy"), ("Vampire", "Vampire"), ("Yaoi", "Yaoi"), ("Yuri", "Yuri"),
)

class Manga(models.Model):
    manga_name = models.CharField(max_length=1000)
    manga_author = models.CharField(max_length=1000)
    manga_illustrator = models.CharField(max_length=1000)
    release_date = models.DateField('date published')
    manga_genre = MultiSelectField(choices=genres, max_choices=1, default=None)
    manga_score = models.FloatField(default=0.0)
    manga_description = models.TextField(max_length=1000)
    # manga_img = models.ImageField(upload_to='game_img/', default=None, null=True)  # need to create static files, neskol'ko kartinok
    is_available = models.BooleanField(verbose_name="Is Available For Readers", default=True)

class Volume(models.Model):
    # volume_img = models.ImageField(upload_to='game_img/', default=None, null=True)  # need to create static files
    volume_order=models.IntegerField(max_length=1000)
    from_manga = models.ForeignKey(Manga, on_delete=models.CASCADE)


class Chapter(models.Model):
    chapter_order=models.IntegerField(max_length=1000)
    from_volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    # chapter_img = models.ImageField(upload_to='game_img/', default=None, null=True)  # need to create static files

class Page(models.Model):
    # page_img = models.ImageField(upload_to='game_img/', default=None, null=True)  # need to create static files
    page_order = models.IntegerField(max_length=1000)
    from_chapter= models.ForeignKey(Chapter, on_delete=models.CASCADE)















