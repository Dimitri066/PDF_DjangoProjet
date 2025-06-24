from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from PDF_Django.models import Template
from weasyprint import HTML
from django import forms


def generer_formulaire(formulaire_json):
    """ Ce programme va géneré le formulaire à l'aide du code JSON fourni en entrée via l'interface
    TemplateAdmin """

    champs = {}
    for champ_nom, propriete in formulaire_json.items():
        #récupère les champs et propriétés associés à partir du formulaire
        # print(nom_champ, propriete)
        type_champ = propriete.get("type", "str")
        etiquette = propriete.get("label", champ_nom)

    # Permet de gérer quelques types classiques, on peut don en rajouter aux besoins
        if type_champ == "str":
            champs[champ_nom] = forms.CharField(label = etiquette)
        elif type_champ == "int":
            champs[champ_nom] = forms.IntegerField(label= etiquette)
        elif type_champ == "bool":
            champs[champ_nom] = forms.BooleanField(label =etiquette)
        else:
            # Type par défaut
            champs[champ_nom] = forms.CharField(label= etiquette)

    return type("FormulaireJSONGenere", (forms.Form,), champs) #Crée une classe dynamique du formulaire généré

def renvoie_liste_templates(request):
    """Cette focntion renvoie la page HTML avec la liste des templates"""

    return render(request, "liste_templates.html", {"templates": Template.objects.all()})

def remplir_formulaire(request, id_template):
    """ Affiche le formulaire, attends la complétion et ensuite génére le PDF"""
    template = Template.objects.get(pk=id_template)
    formulaireGenere = generer_formulaire(template.json)

    if request.method == "POST": # méthode pour savoir si formulaire rempli
        formulaire = formulaireGenere(request.POST)
        if formulaire.is_valid(): # formulaire valide ?
            donnees = formulaire.cleaned_data # crée un  dic
            html_rempli = template.html.format(**donnees)
            pdf = HTML(string=html_rempli).write_pdf() #pdf à l'aide de weasyprint !
            res = HttpResponse(pdf, content_type="application/pdf") #on précise le type pour ne pas avoir de conflit d'interprétation
            return res
    else:
        formulaire = formulaireGenere() #renvoie le formulaire vide si invalide

    return render(request, "remplir_formulaire.html", {"form": formulaire, "template": template})
