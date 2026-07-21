from django.core.management.base import BaseCommand, CommandError
from django.db import connection


class Command(BaseCommand):
    help = "Полностью удаляет все таблицы и схему public в PostgreSQL"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.WARNING(
                "ВНИМАНИЕ! Эта команда полностью удалит ВСЕ таблицы и схему public!\n"
                "Все данные будут безвозвратно потеряны."
            )
        )

        confirm = input('Подтвердите вводом "Yes": ')
        if confirm != "Yes":
            raise CommandError("Отменено пользователем.")

        with connection.cursor() as cursor:
            cursor.execute("DROP SCHEMA public CASCADE;")
            cursor.execute("CREATE SCHEMA public;")
            cursor.execute("GRANT ALL ON SCHEMA public TO PUBLIC;")

        self.stdout.write(
            self.style.SUCCESS(
                "Схема public удалена и создана заново."
            )
        )