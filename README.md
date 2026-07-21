## Магазин продуктов (backend)
---

### Стек:
- Django
- Django Rest Framework
- PostgreSQL
---

### Команды
- `python manage.py full_drop_db` - Полная очистка БД, со сбросом авто-инкримента  
- `python manage.py create_custom_superuser` - Команда для создания суперпользователя  
- `python manage.py load_test_data_to_db` - Команда для записи тестовых данных в чистую 
БД из фикстуры, фикстура должна находится по пути fixtures/test_fixture_db.json (Порядок 
загрузки: 1 - Категории(Category), 2 - Подкатегории(Subcategory), 3 - Продукты (Products). 
**При изменении фикстукры порядок не должен меняться! Если БД не пуста, то команда 
не сработает!**)

---

### Пользователь

---

### Эндпоинты:
Эндпоинты приведены к одной стилистике (`/api/v1/<model>/<action>/`) через переопределение 
в urlpatterns (products.api.v1.urls.py).  
Подробнее:  
`http://127.0.0.1:8000/redoc/`  
`http://127.0.0.1:8000/swagger/`

---

### Схема БД: