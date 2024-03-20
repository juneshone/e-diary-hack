# e-diary-hack

Cкрипт исправляет оценки ученика в журнале, удаляет замечания учителей и добавляет положительные комментарии от учителей.

## Как установить

Склонируйте репозиторий сайта по [ссылке](https://github.com/devmanorg/e-diary), подключите [базу данных](https://dvmn.org/filer/canonical/1562234129/166/) и запустите сервер с помощью [инструкции](https://github.com/devmanorg/e-diary/tree/master#переменные-окружения).

Редактировать базу данных можно 2 способами:

* Cкачать файл с кодом, добавить в корневую папку проекта рядом с manage.py и подключить через import.
* Запустить сервер, открыть Django shell в новом окне терминала с помощью команды:

```python
python manage.py shell
```

## Как использовать

Для запуска скрипта необходимо задать значения переменным:

* `object`- название предмета для похвалы от учителей;
* `child_name` - имя ученика для поиска учетной записи.

Для получения учетной записи ученика введите:

```python
schoolkid = get_schoolkid(child_name)
```

При редактировании БД внутри shell импортируйте модели БД и модуль `random`:

```python
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
import random
```

Для исправления оценок с 2 и 3 на 5 используйте функцию:

```python
fix_marks(schoolkid)
```

Для удаления всех замечаний от учителей используйте функцию:

```python
remove_chastisements(schoolkid)
```

Для создания похвалы от учителей используйте функцию:

```python
create_commendation(schoolkid, subject)
```

## Цель проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
