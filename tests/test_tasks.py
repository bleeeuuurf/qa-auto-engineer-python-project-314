from uuid import uuid4

import pytest

from pages.task_create_page import TaskCreatePage
from pages.task_edit_page import TaskEditPage
from pages.tasks_page import TasksPage


def create_task(tasks_page, create_page, task_title):
    tasks_page.open_page()
    tasks_page.open_create_form()

    create_page.fill_title(task_title)
    create_page.select_first_assignee()
    create_page.select_first_status()
    create_page.save_task()

    assert create_page.creation_notification_is_displayed()


@pytest.mark.smoke
def test_task_create_form_is_opened(logged_in_user, base_url):
    tasks_page = TasksPage(logged_in_user, base_url)
    create_page = TaskCreatePage(logged_in_user)

    tasks_page.open_page()
    tasks_page.open_create_form()

    assert create_page.title_is_displayed()
    assert create_page.assignee_is_displayed()
    assert create_page.status_is_displayed()


@pytest.mark.smoke
def test_task_can_be_created(logged_in_user, base_url):
    tasks_page = TasksPage(logged_in_user, base_url)
    create_page = TaskCreatePage(logged_in_user)

    task_title = f"Test Task {uuid4()}"

    tasks_page.open_page()
    tasks_page.open_create_form()

    create_page.fill_title(task_title)

    assignee_name, assignee_id = create_page.select_first_assignee()
    status_name, status_id = create_page.select_first_status()

    assert assignee_name
    assert assignee_id
    assert status_name
    assert status_id

    create_page.save_task()

    assert create_page.creation_notification_is_displayed()

    tasks_page.open_page()

    assert tasks_page.board_is_loaded()
    assert tasks_page.task_is_in_column(task_title, status_id)


@pytest.mark.smoke
def test_tasks_board_displays_all_tasks(logged_in_user, base_url):
    tasks_page = TasksPage(logged_in_user, base_url)

    tasks_page.open_page()

    assert tasks_page.board_is_loaded()
    assert tasks_page.tasks_are_displayed()
    assert tasks_page.task_cards_have_titles()


@pytest.mark.smoke
def test_tasks_can_be_filtered_by_assignee(logged_in_user, base_url):
    tasks_page = TasksPage(logged_in_user, base_url)

    tasks_page.open_page()

    assert tasks_page.board_is_loaded()

    assignee_name, assignee_id = tasks_page.select_assignee_filter()

    assert assignee_name
    assert assignee_id
    assert tasks_page.tasks_are_displayed()


@pytest.mark.smoke
def test_tasks_can_be_filtered_by_status(logged_in_user, base_url):
    tasks_page = TasksPage(logged_in_user, base_url)

    tasks_page.open_page()

    assert tasks_page.board_is_loaded()

    status_name, status_id = tasks_page.select_status_filter()

    assert status_name
    assert status_id
    assert tasks_page.tasks_are_in_status(status_name)


@pytest.mark.smoke
def test_tasks_can_be_filtered_by_label(logged_in_user, base_url):
    tasks_page = TasksPage(logged_in_user, base_url)

    tasks_page.open_page()

    assert tasks_page.board_is_loaded()

    label_name, label_id = tasks_page.select_label_filter()

    assert label_name
    assert label_id
    assert tasks_page.tasks_are_displayed()


@pytest.mark.smoke
def test_task_can_be_edited(logged_in_user, base_url):
    tasks_page = TasksPage(logged_in_user, base_url)
    create_page = TaskCreatePage(logged_in_user)
    edit_page = TaskEditPage(logged_in_user)

    task_title = f"Test Task {uuid4()}"
    updated_title = f"Updated Task {uuid4()}"

    create_task(tasks_page, create_page, task_title)

    tasks_page.open_page()

    assert tasks_page.board_is_loaded()
    assert tasks_page.task_is_displayed(task_title)

    tasks_page.open_edit_form(task_title)

    assert edit_page.title_is_displayed()
    assert edit_page.get_title() == task_title

    edit_page.update_title(updated_title)
    edit_page.save_task()

    assert tasks_page.task_is_displayed(updated_title)


@pytest.mark.smoke
def test_task_can_be_moved_to_another_status(logged_in_user, base_url):
    tasks_page = TasksPage(logged_in_user, base_url)
    create_page = TaskCreatePage(logged_in_user)
    edit_page = TaskEditPage(logged_in_user)

    task_title = f"Move Task {uuid4()}"

    tasks_page.open_page()
    tasks_page.open_create_form()

    create_page.fill_title(task_title)
    create_page.select_first_assignee()
    create_page.select_status_by_name("Draft")
    create_page.save_task()

    assert create_page.creation_notification_is_displayed()

    tasks_page.open_page()

    assert tasks_page.board_is_loaded()
    assert tasks_page.task_is_displayed(task_title)

    tasks_page.open_edit_form(task_title)

    assert edit_page.title_is_displayed()
    assert edit_page.get_title() == task_title

    edit_page.select_status("To Review")
    edit_page.save_task()

    assert edit_page.update_notification_is_displayed()

    tasks_page.filter_by_status("To Review")

    assert tasks_page.task_is_displayed(task_title)


@pytest.mark.smoke
def test_task_can_be_deleted(logged_in_user, base_url):
    tasks_page = TasksPage(logged_in_user, base_url)
    create_page = TaskCreatePage(logged_in_user)
    edit_page = TaskEditPage(logged_in_user)

    task_title = f"Delete Task {uuid4()}"

    create_task(tasks_page, create_page, task_title)

    tasks_page.open_page()

    assert tasks_page.board_is_loaded()
    assert tasks_page.task_is_displayed(task_title)

    tasks_page.open_edit_form(task_title)

    assert edit_page.title_is_displayed()

    edit_page.delete_task()

    assert edit_page.deletion_notification_is_displayed()
    assert tasks_page.board_is_loaded()
    assert tasks_page.task_is_not_displayed(task_title)
