import json

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand


FIXTURE_PATH = settings.BASE_DIR / "fixtures" / "test_fixture_db.json"


class Command(BaseCommand):
    help = "Загружает тестовые данные из фикстуры в БД"

    def handle(self, *args, **options):
        with open(FIXTURE_PATH, encoding="utf-8") as f:
            data = json.load(f)

        # Проверяем что таблицы моделей из фикстуры пусты
        models_from_fixture = set()
        for record in data:
            app_label, model_name = record["model"].split(".")
            models_from_fixture.add(apps.get_model(app_label, model_name))

        for model in models_from_fixture:
            if model.objects.exists():
                self.stdout.write(self.style.WARNING(
                    "База данных не пуста. Загрузка возможна только в пустую БД."
                ))
                return

        created = 0

        # 3. Проходим по каждой записи и создаём объекты
        for record in data:
            app_label, model_name = record["model"].split(".")
            model = apps.get_model(app_label, model_name)
            fields = record["fields"]

            model.objects.create(**fields)

            created += 1
            self.stdout.write(f"  + {model.__name__}: {fields['name']}")

        # 4. Итог работы команды
        self.stdout.write(self.style.SUCCESS(
            f"\nГотово: создано {created} записей"
        ))
