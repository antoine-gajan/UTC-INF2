from django import forms
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Etudiant, Intervenant, Inscrire, Bureau, Cours, TD, TP
# Create your views here.
from django.views.decorators.http import require_http_methods
from gestion_cours.forms import CoursForm, getIntervenantSelectFormUsingKey, EtudiantForm


@require_http_methods(["GET"])
def base(req: HttpRequest):
    return render(req, "base.html", {"prenom": req.GET.get("prenom")})


@require_http_methods(["GET", "POST"])
def creer_cours(req: HttpRequest):
    if req.method == 'POST':
        #Récupération du formulaire
        creer_cours_form = CoursForm(req.POST)
        #S'il est valide, on le sauvegarde
        if creer_cours_form.is_valid() and not Cours.objects.filter(code=creer_cours_form.cleaned_data['code']):
            creer_cours_form.save()

        content = {'intervenants_td': req.POST.getlist('intervenants_td'),
                   'intervenants_tp': req.POST.getlist('intervenants_tp')}

        cours = Cours.objects.filter(code=creer_cours_form.cleaned_data['code'])

        for i, id_intervenant in enumerate(content['intervenants_td']):
            charge = Intervenant.objects.filter(id=id_intervenant)
            td = TD(num_groupe=i, charge=charge, cours=cours)
            td.save()

        for i, id_intervenant in enumerate(content['intervenants_td']):
            charge = Intervenant.objects.filter(id=id_intervenant)
            tp = TP(num_groupe=i, charge=charge, cours=cours)
            tp.save()
    else:
        #Renvoyer un formulaire vide (GET)
        form = CoursForm()
        content = {'intervenants_td': [], 'intervenants_tp': []}

    TDInterForm = getIntervenantSelectFormUsingKey('td')
    TPInterForm = getIntervenantSelectFormUsingKey('tp')

    return render(req, 'creer_cours.html', {
        'form': form,
        'td_inter_form': TDInterForm(initial=content),
        'tp_inter_form': TPInterForm(initial=content)
    })


@require_http_methods(['GET', 'POST'])
def creer_etudiant(request):
    envoi = False
    creer = False
    if request.method == 'POST':
        envoi = True
        #Récupération des données du formulaire
        creer_etudiant_form = EtudiantForm(request.POST)
        if creer_etudiant_form.is_valid():
            INE = creer_etudiant_form.cleaned_data['INE']
            #Si un utilisateur possède déjà cet INE, erreur
            if Etudiant.objects.filter(INE=INE).exists():
                creer = False
            else:
                #Création de l'utilisateur
                creer = True
                creer_etudiant_form.save()
                return redirect('creer_etudiant')
    else:
        creer_etudiant_form = EtudiantForm()
    return render(request, 'creer_etudiant.html', {'form':creer_etudiant_form})

@require_http_methods(["GET"])
def afficher_etudiants(request):
    all_etudiants = Etudiant.objects.all()
    return render(request, 'afficher_etudiants.html', {'etudiants': all_etudiants})

@require_http_methods(["GET"])
def afficher_cours(request):
    all_cours = Cours.objects.all()
    return render(request, 'afficher_cours.html', {'cours': all_cours})
