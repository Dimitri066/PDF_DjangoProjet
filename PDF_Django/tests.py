from django.test import TestCase
from django import forms
from PDF_Django.views import generer_formulaire


class TestUnitaireGenererFormulaire(TestCase):
    """Classe pour les tests unitaires de la fonction generer_formulaire, elle hérite de TestCase"""

    def test_formulaire_vide(self):
        """Teste lafonction generer_formulaire avec un JSON vide"""
        json = {}
        Formulaire = generer_formulaire(json)
        form = Formulaire()
        self.assertEqual(len(form.fields), 0)

    def test_formulaire_type(self):
        # On teste les types 3 types qui sont gérés par la fonction ("str", "int", "bool")
        # et un type random pour voir si les clefs et valeurs sont bien remplies et justes.

        # On crée un JSON pour ne pas utiliser la base de donnée ce qui peut l'endommager
        json = {"nom_etudiant": {"type": "str", "label": "Nom"},
            "age": {"type": "int", "label": "Age"},
            "majorite": {"type": "bool", "label": "Majeur"},
            "champ_inconnu": {"type": "random", "label": "abc"}}

        # Appel de la fonction qui génère une classe Formulaire puis un objet form de cette classe
        Formulaire = generer_formulaire(json)
        form = Formulaire()
        # Test pour l'existence du champ
        self.assertIn("nom_etudiant", form.fields)
        self.assertIn("age", form.fields)
        self.assertIn("majorite", form.fields)
        self.assertIn("champ_inconnu", form.fields)
        # Test pour savoir si le champ est du bon type
        self.assertIsInstance(form.fields["nom_etudiant"], forms.CharField)
        self.assertIsInstance(form.fields["age"], forms.IntegerField)
        self.assertIsInstance(form.fields["majorite"], forms.BooleanField)
        self.assertIsInstance(form.fields["champ_inconnu"], forms.CharField)

        # Test pour si la valeur associée à la clef est correcte
        self.assertEqual(form.fields["nom_etudiant"].label, "Nom")
        self.assertEqual(form.fields["age"].label, "Age")
        self.assertEqual(form.fields["majorite"].label, "Majeur")
        self.assertEqual(form.fields["champ_inconnu"].label, "abc")
