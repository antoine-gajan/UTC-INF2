from django.db import models


# Create your models here.
class Bureau(models.Model):
    centre = models.CharField(max_length=2, null=False)
    batiment = models.CharField(max_length=3, null=False)
    salle = models.IntegerField(null=False)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['centre', 'batiment', 'salle'], name="Contrainte d'unicité du bureau")]
    def __str__(self):
        return f"{self.centre}{self.batiment}{self.salle}"


class Etudiant(models.Model):
    INE = models.IntegerField()
    nom = models.CharField(max_length=30, null=False)
    prenom = models.CharField(max_length=30, null=False)
    niveau = models.CharField(max_length=4, null=False)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['INE'], name="Contrainte d'unicité de l'INE")]
    def __str__(self):
        return f"{self.INE} - {self.nom} {self.prenom} - {self.niveau}"


class Intervenant(models.Model):
    nom = models.CharField(max_length=30, null=False)
    prenom = models.CharField(max_length=30, null=False)
    tel = models.IntegerField()
    bureau = models.ForeignKey(Bureau, on_delete=models.SET_NULL, related_name='personnes', null=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['nom', 'prenom'], name="Contrainte d'unicité de la personne")]
    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Cours(models.Model):
    code = models.CharField(max_length=5, null=False)
    titre = models.TextField(max_length=100, null=False)
    etudiant = models.ManyToManyField(Etudiant, through='Inscrire')
    semestre = models.CharField(max_length=1, null=False)
    annee = models.IntegerField(null=False)
    mots_cles = models.CharField(max_length=100)
    responsable = models.ForeignKey(Intervenant, on_delete=models.SET_NULL, null=True, related_name='est_responsable')
    intervenants = models.ManyToManyField(Intervenant, related_name='intervient_dans')
    credit = models.IntegerField()

class TD(models.Model):
    num_groupe = models.IntegerField(null=False)
    charge = models.ForeignKey(Intervenant, on_delete=models.SET_NULL, null=True)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, null=False)


class TP(models.Model):
    num_groupe = models.IntegerField(null=False)
    charge = models.ForeignKey(Intervenant, on_delete=models.SET_NULL, null=True)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, null=False)


class Inscrire(models.Model):
    td = models.ForeignKey(TD, on_delete=models.CASCADE, null=False)
    tp = models.ForeignKey(TP, on_delete=models.CASCADE, null=False)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, null=False)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=False, related_name='est_inscrit')
    class Meta:
        constraints = [models.UniqueConstraint(fields=['cours','etudiant'], name="Etudiant déjà inscrit")]
