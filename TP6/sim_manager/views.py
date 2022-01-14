from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from .models import Simulation, Favorite, Share
from .forms import UserProfileForm, SimuForm, CreateProfileForm, UpdatePasswordForm, DeleteAccountForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse_lazy
from pyfhn.fhn_runner import run_fhn_base
import matplotlib.pyplot as plt
from io import StringIO


# Create your views here.
def landing(request):
    return render(request, "base.html", locals())


@login_required(login_url="/account/login/")
@require_http_methods(["POST", "GET"])
def simulation_list(request):
    "Liste des simulations de l'utilisateur"
    #Récupération de l'ensemble des simulations crées par l'utilisateur
    user_simulations = Simulation.objects.filter(user=request.user)
    #Récupération des simulations partagées avec l'utilisateur
    shared_simulations_id = Share.objects.filter(user_share=request.user).values_list('simulation')
    shared_simulations_id = list(elt[0] for elt in shared_simulations_id)
    shared_simulations = Simulation.objects.filter(id__in=shared_simulations_id)
    #Création de l'ensemble des simulations
    all_simulations = user_simulations.union(shared_simulations)
    #Récupération de l'ensemble des favoris
    fav_sim = Favorite.objects.filter(user=request.user).select_related('simulation')
    return render(request, "simulation_list.html", {"user_sims": all_simulations, "fav_sim": fav_sim})


@login_required(login_url="/account/login/")
@require_http_methods(["POST", "GET"])
def edit_profile(request):
    "Editer les informations du profil de l'utilisateur"
    envoi = False
    error = False
    if request.method == "POST":
        envoi = True
        user_profile_form = UserProfileForm(request.POST)
        #Si le formulaire a été correctement rempli
        if user_profile_form.is_valid() and user_profile_form.cleaned_data["email"]:
            current_user = User.objects.get(username=request.user.username)
            #Mise à jour des informations
            current_user.first_name = user_profile_form.cleaned_data["first_name"]
            current_user.last_name = user_profile_form.cleaned_data["last_name"]
            current_user.email = user_profile_form.cleaned_data["email"]
            #Sauvegarde dans la BDD
            current_user.save()
        else:
            #Erreur rencontrée
            error = True
    else:
        user_profile_form = UserProfileForm(instance=request.user)
    return render(request, "edit_profile.html", {"form": user_profile_form, "envoi":envoi, "error":error})


@require_http_methods(["POST", "GET"])
def create_profile(request):
    "Créer un nouvel utilisateur"
    envoi = False
    signup = False
    if request.method == "POST":
        envoi = True
        profile_create_form = CreateProfileForm(request.POST)
        #Si le formulaire envoyé est valide
        if profile_create_form.is_valid() and profile_create_form.cleaned_data["email"]:
            #Récupération des informations
            username = profile_create_form.cleaned_data["username"]
            password = profile_create_form.cleaned_data["password"]
            email = profile_create_form.cleaned_data["email"]
            #On regarde si un utilisateur avec cet username existe déjà
            if User.objects.filter(username=username).exists():
                #Impossible de créer l'utlisateur
                signup = False
            else:
                signup = True
                #Création de l'utilisateur
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                #Connecte automatiquement l'utilisateur après son inscription
                user = authenticate(request, username=username, password=password)
                login(request, user)
                #Redirection vers la page de modification des informations personnelles
                return redirect("profile")
    else:
        profile_create_form = CreateProfileForm()
    return render(request, "create_profile.html", {"form": profile_create_form, "envoi":envoi, "signup":signup})


@login_required(login_url="/account/login/")
@require_http_methods(["POST", "GET"])
def update_password(request):
    "Modifier le mot de passe de l'utilisateur"
    envoi = False
    modify = False
    if request.method == "POST":
        envoi = True
        update_password_form = UpdatePasswordForm(request.POST)
        # Si le formulaire envoyé est valide
        if update_password_form.is_valid():
            #Récupération des mots de passe saisis
            password1 = update_password_form.cleaned_data["password1"]
            password2 = update_password_form.cleaned_data["password2"]
            #Si l'utilisateur a saisi 2 fois le même mot de passe, on peut effectuer la modification
            if password1 == password2:
                modify = True
                #Récupère le compte de l'utilisateur
                user = User.objects.get(username=request.user.username)
                #Modification du mot de passe
                user.set_password(password1)
                #Sauvegarde des modifications
                user.save()
            else:
                modify = False
    else:
        update_password_form = UpdatePasswordForm()
    return render(request, "update_password.html", {"form": update_password_form, "envoi":envoi, "modify":modify})


@login_required(login_url="/account/login/")
@require_http_methods(["POST", "GET"])
def delete_account(request):
    "Supprimer le compte de l'utilisateur"
    envoi = False
    supprime = False
    if request.method == "POST":
        envoi = True
        delete_account_form = DeleteAccountForm(request.POST)
        # Si le formulaire envoyé est valide
        if delete_account_form.is_valid():
            # Récupération du choix de l'utilisateur
            choice = delete_account_form.cleaned_data['delete']
            # Si l'utilisateur a choisi de supprimer son compte
            if choice == 'Yes':
                supprime = True
                # Récupère le compte de l'utilisateur
                user = User.objects.get(username=request.user.username)
                # Suppression de l'utilisateur
                user.delete()
            else:
                #Sinon, on ne supprime pas le compte
                supprime = False
    else:
        delete_account_form = DeleteAccountForm()
    return render(request, "delete_account.html", {"form": delete_account_form, "envoi":envoi, "supprime":supprime})


@login_required(login_url="/account/login/")
@require_http_methods(["POST", "GET"])
def new_simu(request):
    "Construit une nouvelle simulation à partir de paramètres rentrés par l'utilisateur"
    form = SimuForm(request.POST, request.FILES)
    #Si le formulaire rentré est valide
    if form.is_valid():
        params = form.cleaned_data
        print(params)
        #Création de la simulation
        newsim = Simulation(
            user=request.user,
            alpha=params["alpha"],
            beta=params["beta"],
            gamma=params["gamma"],
            delta=params["delta"],
            epsilon=params["epsilon"],
        )
        #Sauvegarde dans la BDD de la simulation
        newsim.save()
        #Lance la simulation
        return run_sim(request, newsim.id)
    return render(request, "newsimu.html", locals())

@require_http_methods(["POST", "GET"])
def run_sim(request, object_id):
    "Lance la simulation et affiche le graphe associé"
    simulation = Simulation.objects.filter(id=object_id).get()
    params = model_to_dict(get_object_or_404(Simulation, pk=object_id))
    params.pop("user")
    params.pop("id")
    res = run_fhn_base(params)
    f = plt.figure()
    plt.title("FHN Simulation")
    plt.xlabel("Time")
    plt.ylabel("Outputs")
    plot = plt.plot(res["t"], res["y"][0], res["t"], res["y"][1])
    plt.legend(["v", "w"])
    imgdata = StringIO()
    f.savefig(imgdata, format="svg")
    imgdata.seek(0)
    data = imgdata.getvalue()
    #Si la simulation est déjà marquée dans les favoris de l'utilisateur
    if Favorite.objects.filter(user=request.user, simulation=simulation).exists():
        #Initialisation de la variable favorite à True
        favorite = True
    else:
        #Sinon, on l'initialise à False
        favorite = False
    # Utilisateurs avec qui la simulation est déjà partagée
    shared = Share.objects.filter(simulation=simulation).values_list('user_share')
    shared = list(elt[0] for elt in shared)
    #Ajout de l'utilisateur actif afin qu'il ne puisse pas s'auto-partager la simulation
    shared.append(request.user.id)
    # Utilisateurs possibles pour le partage
    users_to_share = User.objects.exclude(id__in=shared)
    return render(request, "graphic.html", {"graphic": data, "favorite": favorite, "object_id": object_id,"users_to_share": users_to_share})


@login_required(login_url="/account/login/")
@require_http_methods(["GET", "POST"])
def add_or_remove_favorite(request):
    "Ajouter ou retire des favoris la simulation"
    envoi = False
    #Récupération si l'utilisateur a mis ou non en favori la simulation
    favorite = Favorite.objects.filter(user=request.user, simulation=request.POST['object_id']).exists()
    #Si le formulaire est envoyé
    if request.method == "POST":
        envoi = True
        #Récupération de la simulation choisie
        simulation = Simulation.objects.filter(id=request.POST['object_id']).get()
        #Si l'utilisateur a choisi d'enlever la simulation des favoris
        if request.POST['submit'] == "Remove from favorite":
            #Initialisation de la variable favorite à False
            favorite = False
            #Suppression de la ligne associé à ce "favori" dans la BDD
            Favorite.objects.filter(user=request.user, simulation=request.POST['object_id']).delete()
        #Si l'utilisateur a choisi d'ajouter la simulation dans ses favoris
        else:
            #Initialisation de la variable favorite à True
            favorite = True
            #Création de la ligne associée à ce favori dans la BDD
            new_fav = Favorite(user=request.user, simulation=simulation)
            new_fav.save()

    #Récupération des utilisateurs avec qui la simulation est déjà partagée
    shared = Share.objects.filter(simulation=simulation).values_list('user_share')
    #Tableau avec l'ensemble des id des utilisateurs avec qui la simulation est déjà partagée
    shared = list(elt[0] for elt in shared)
    #Ajout de l'utilisateur actif afin qu'il ne puisse pas s'auto-partager la simulation
    shared.append(request.user.id)
    #Utilisateurs possibles pour le partage
    users_to_share = User.objects.exclude(id__in=shared)
    return render(request, "graphic.html",{"graphic": request.POST['data'], "favorite": favorite, "object_id": request.POST['object_id'], "users_to_share": users_to_share})


@login_required(login_url="/account/login/")
@require_http_methods(["GET", "POST"])
def share(request):
    envoi = False
    partager = False
    # Récupération si l'utilisateur a mis ou non en favori la simulation
    favorite = Favorite.objects.filter(user=request.user, simulation=request.POST['object_id']).exists()
    #Si le formulaire est envoyé
    if request.method == "POST":
        envoi = True
        #Récupération de la simulation choisie
        simulation = Simulation.objects.filter(id=request.POST['object_id']).get()
        #Récupération de l'utilisateur à partager
        share_user = User.objects.filter(id=request.POST['user_id']).get()
        #Vérification par sécurité si l'utilisateur ne repartage pas avec un même utilisateur et s'il ne se partage pas lui-même la simulation
        if Share.objects.filter(user_share=share_user, simulation=simulation).exists() or share_user == request.user:
            partager = False
        else:
            #Ajout du partage à la BDD
            partage = Share(user_share=share_user, simulation=simulation)
            partage.save()

        #Récupération des utilisateurs avec qui la simulation est déjà partagée
        shared = Share.objects.filter(simulation=simulation).values_list('user_share')
        #Tableau avec l'ensemble des id des utilisateurs avec qui la simulation est déjà partagée
        shared = list(elt[0] for elt in shared)
        #Ajout de l'utilisateur actif afin qu'il ne puisse pas s'auto-partager la simulation
        shared.append(request.user.id)
        #Utilisateurs possibles pour le partage
        users_to_share = User.objects.exclude(id__in=shared)
        return render(request, "graphic.html", {"graphic": request.POST['data'], "favorite": favorite, "object_id": request.POST['object_id'],"users_to_share": users_to_share, "partage":partager})


@login_required(login_url="/login/")
@require_http_methods(["GET"])
def simulation_delete(request, object_id):
    "Supprime une simulation"
    #Récupération de la simulation à supprimer
    sim = get_object_or_404(Simulation, pk=object_id)
    #Si l'utilisateur demandant la suppression de la simulation en est aussi l'auteur, on la supprime pour tous les utilisateurs
    if sim.user == request.user:
        sim.delete()
    #Si l'utilisateur est uniquement en "partage", on la supprime uniquement pour lui
    else:
        share_sim = Share.objects.filter(user_share=request.user, simulation=object_id)
        share_sim.delete()
    return HttpResponseRedirect(reverse_lazy("sim_list"))


@login_required(login_url="/login/")
@require_http_methods(["GET"])
def disconnect(request):
    "Déconnecte l'utilisateur"
    #Déconnexion de l'utilisation
    logout(request)
    disconnect = True
    return render(request, "registration/logout.html", {"disconnect":disconnect})

