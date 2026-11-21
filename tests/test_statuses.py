from uuid import uuid4

from pages.task_status_create_page import TaskStatusCreatePage
from pages.task_status_edit_page import TaskStatusEditPage
from pages.task_statuses_page import TaskStatusesPage


def create_status(statuses_page, create_page, name, slug):
    statuses_page.open_page()
    statuses_page.open_create_form()

    create_page.fill_status_form(name, slug)
    create_page.save_status()

    assert create_page.creation_notification_is_displayed()


def test_statuses_page_is_opened(logged_in_user, base_url):
    statuses_page = TaskStatusesPage(logged_in_user, base_url)

    statuses_page.open_page()

    assert statuses_page.table_is_loaded()


def test_status_create_form_is_opened(logged_in_user, base_url):
    statuses_page = TaskStatusesPage(logged_in_user, base_url)
    create_page = TaskStatusCreatePage(logged_in_user)

    statuses_page.open_page()
    statuses_page.open_create_form()

    assert create_page.name_is_displayed()
    assert create_page.slug_is_displayed()


def test_status_can_be_created(logged_in_user, base_url):
    statuses_page = TaskStatusesPage(logged_in_user, base_url)
    create_page = TaskStatusCreatePage(logged_in_user)

    name = f"test status {uuid4()}"
    slug = f"test_status_{uuid4()}"

    create_status(statuses_page, create_page, name, slug)

    statuses_page.open_page()

    assert statuses_page.status_is_in_table(name, slug)


def test_statuses_table_displays_name_and_slug(logged_in_user, base_url):
    statuses_page = TaskStatusesPage(logged_in_user, base_url)

    statuses_page.open_page()

    assert statuses_page.table_is_loaded()
    assert statuses_page.names_are_displayed()
    assert statuses_page.slugs_are_displayed()


def test_status_can_be_edited(logged_in_user, base_url):
    statuses_page = TaskStatusesPage(logged_in_user, base_url)
    create_page = TaskStatusCreatePage(logged_in_user)
    edit_page = TaskStatusEditPage(logged_in_user)

    original_name = f"Test Status {uuid4()}"
    original_slug = f"test_status_{uuid4()}"

    updated_name = f"Updated Status {uuid4()}"
    updated_slug = f"updated_status_{uuid4()}"

    create_status(
        statuses_page,
        create_page,
        original_name,
        original_slug,
    )

    statuses_page.open_page()
    statuses_page.open_edit_form(original_name)

    assert edit_page.name_is_displayed()
    assert edit_page.slug_is_displayed()

    edit_page.update_status(updated_name, updated_slug)
    edit_page.save_status()

    assert statuses_page.status_is_in_table(updated_name, updated_slug)


def test_status_can_be_deleted(logged_in_user, base_url):
    statuses_page = TaskStatusesPage(logged_in_user, base_url)
    create_page = TaskStatusCreatePage(logged_in_user)

    status_name = f"Delete Status {uuid4()}"
    status_slug = f"delete_status_{uuid4()}"

    create_status(
        statuses_page,
        create_page,
        status_name,
        status_slug,
    )

    statuses_page.open_page()

    assert statuses_page.status_is_in_table(status_name, status_slug)

    statuses_page.select_status(status_name)
    statuses_page.delete_selected_statuses()

    assert statuses_page.deletion_notification_is_displayed()
    assert statuses_page.status_is_not_in_table(status_name)


def test_multiple_statuses_can_be_deleted(logged_in_user, base_url):
    statuses_page = TaskStatusesPage(logged_in_user, base_url)
    create_page = TaskStatusCreatePage(logged_in_user)

    statuses = [
        (f"Delete Status {uuid4()}", f"delete_status_{uuid4()}"),
        (f"Delete Status {uuid4()}", f"delete_status_{uuid4()}"),
    ]

    for name, slug in statuses:
        create_status(statuses_page, create_page, name, slug)

    statuses_page.open_page()

    for name, slug in statuses:
        assert statuses_page.status_is_in_table(name, slug)
        statuses_page.select_status(name)

    statuses_page.delete_selected_statuses()

    assert statuses_page.deletion_notification_is_displayed()

    for name, slug in statuses:
        assert statuses_page.status_is_not_in_table(name)


def test_all_statuses_can_be_deleted(logged_in_user, base_url):
    statuses_page = TaskStatusesPage(logged_in_user, base_url)

    statuses_page.open_page()

    assert statuses_page.table_is_loaded()

    statuses_page.select_all_statuses()
    statuses_page.delete_selected_statuses()

    assert statuses_page.deletion_notification_is_displayed()
    assert statuses_page.statuses_list_is_empty()
