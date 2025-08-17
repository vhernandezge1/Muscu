from django.core.management.base import BaseCommand
from training.models import Exercise, NutritionTip

EXERCISES = [
    ("Développé couché", "Pectoraux, triceps, épaules. 3x8-12.", "Pectoraux", "medium"),
    ("Squat", "Quadriceps, fessiers, lombaires. 4x6-10.", "Jambes", "hard"),
    ("Tractions", "Dos, biceps. 3x6-10.", "Dos", "medium"),
    ("Gainage", "Core/abdos, 3 x 45-60s.", "Abdos", "easy"),
]

TIPS = [
    ("Prioriser les protéines", "Vise 1,6–2,2 g/kg/jour répartis sur 3–4 repas.", "Macros"),
    ("Hydratation", "Boire 30–40 ml/kg/jour. Ajouter +500 ml si séance intense.", "Hydratation"),
    ("Sommeil", "7–9h par nuit. Évite les écrans 60 min avant dodo.", "Récupération"),
]

class Command(BaseCommand):
    help = "Insère des données de démonstration (exercices + nutrition)"

    def handle(self, *args, **options):
        created_e = 0
        for name, desc, cat, diff in EXERCISES:
            _, created = Exercise.objects.get_or_create(
                name=name,
                defaults={"description": desc, "category": cat, "difficulty": diff}
            )
            created_e += int(created)

        created_n = 0
        for title, content, cat in TIPS:
            _, created = NutritionTip.objects.get_or_create(
                title=title,
                defaults={"content": content, "category": cat}
            )
            created_n += int(created)

        self.stdout.write(self.style.SUCCESS(
            f"OK — {created_e} exercices, {created_n} conseils ajoutés."
        ))
