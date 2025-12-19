from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Eliminar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        users = [
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='test', first_name='Peter', last_name='Parker'),
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='test', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='test', first_name='Diana', last_name='Prince'),
        ]

        # Crear actividades
        Activity.objects.create(user='spiderman', type='run', duration=30, team='Marvel')
        Activity.objects.create(user='ironman', type='cycle', duration=45, team='Marvel')
        Activity.objects.create(user='batman', type='swim', duration=25, team='DC')
        Activity.objects.create(user='wonderwoman', type='run', duration=35, team='DC')

        # Crear leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=60)

        # Crear workouts
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        Workout.objects.create(name='Strength Builder', description='Full body strength training')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
