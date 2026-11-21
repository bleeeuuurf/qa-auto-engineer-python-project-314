# Тестирование канбан-доски с Selenium (Python)

[![hexlet-check](https://github.com/bleeeuuurf/qa-auto-engineer-python-project-314/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/bleeeuuurf/qa-auto-engineer-python-project-314/actions)

Task Manager напоминает знакомые трекеры вроде Redmine: в системе есть пользователи, статусы, метки и задачи. Каждая задача привязана к статусу (колонке доски) и исполнителю, а работа строится вокруг перемещения карточек между этапами. Приложение развёрнуто в Docker-образе и доступно как SPA без отдельного бэкенда — все проверки выполняются на уровне клиентского интерфейса.

Учебный проект Хекслета: https://ru.hexlet.io/programs/qa-auto-engineer-python


## Стек

- Python 3.13
- Selenium WebDriver
- Pytest
- Ruff
- uv
- Docker

## Установка

Клонируйте репозиторий

```bash
git clone https://github.com/bleeeuuurf/qa-auto-engineer-python-project-314.git
cd qa-auto-engineer-python-project-314
```

Установите зависимости

```bash
uv sync
```

## Запуск приложения

Запустите приложение в Docker

```bash
make start
```

Приложение будет доступно по адресу  http://localhost:5173

## Запуск тестов

```bash
make test
```

## Структура проекта

- pages/ — Page Objects, содержащие логику взаимодействия со страницами приложения.
- tests/ — автоматизированные тесты.
- tests/conftest.py — фикстуры и общие настройки Pytest.
- Makefile — команды запуска приложения и тестов.
- pyproject.toml — настройки проекта и зависимости.

## Использование, запись примера

https://asciinema.org/a/qGY6YDwMAHaGNd0m

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.
