from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Simulation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user")
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    alpha = models.FloatField(validators=[MinValueValidator(0.08), MaxValueValidator(0.12)],)
    beta = models.FloatField(validators=[MinValueValidator(0.4), MaxValueValidator(0.6)],)
    gamma = models.FloatField(validators=[MinValueValidator(0.04), MaxValueValidator(0.06)],)
    delta = models.FloatField(validators=[MinValueValidator(0.008), MaxValueValidator(0.012)],)
    epsilon = models.FloatField(validators=[MinValueValidator(0.08), MaxValueValidator(0.12)],)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_fav")
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE, related_name="simulation_fav")
    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'simulation'], name="Une simulation ne peut être mise qu'une fois en favori par un utilisateur")]


class Share(models.Model):
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE, related_name="simulation_share")
    user_share = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_share")
    class Meta:
        constraints = [models.UniqueConstraint(fields=['simulation', 'user_share'], name="Une simulation ne peut pas être partagée 2 fois avec le même utilisateur")]




