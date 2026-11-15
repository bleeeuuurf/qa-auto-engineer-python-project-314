import pytest
from uuid import uuid4

from pages.users_page import UsersPage
from pages.users_create_page import UserCreatePage
from pages.users_edit_page import UsersEditPage


@pytest.mark.smoke
def test_users_page_is_opened(logged_in_user, base_url):
    users_page = UsersPage(logged_in_user, base_url)

    users_page.open_page()

    assert users_page.page_is_opened()


@pytest.mark.smoke
def test_users_table_is_loaded(logged_in_user, base_url):
    users_page = UsersPage(logged_in_user, base_url)

    users_page.open_page()

    assert users_page.table_is_loaded()


@pytest.mark.smoke
def test_user_create_form_is_opened(logged_in_user, base_url):
    users_page = UsersPage(logged_in_user, base_url)
    create_page = UserCreatePage(logged_in_user)

    users_page.open_page()
    users_page.open_create_form()

    assert create_page.page_is_opened()
    assert create_page.email_is_displayed()
    assert create_page.first_name_is_displayed()
    assert create_page.last_name_is_displayed()


@pytest.mark.smoke
def test_user_can_be_created(logged_in_user, base_url):
    users_page = UsersPage(logged_in_user, base_url)
    create_page = UserCreatePage(logged_in_user)

    email = f"test_{uuid4()}@example.com"
    first_name = "Test"
    last_name = "User"

    users_page.open_page()
    users_page.open_create_form()

    create_page.fill_user_form(email, first_name, last_name)
    create_page.save_user()

    users_page.open_page()
    assert users_page.user_is_in_table(email)

@pytest.mark.smoke
def test_user_can_be_edited(logged_in_user, base_url):
    users_page = UsersPage(logged_in_user, base_url)
    create_page = UserCreatePage(logged_in_user)
    edit_page = UsersEditPage(logged_in_user)

    email = f"test_{uuid4()}@example.com"
    first_name = "Test"
    last_name = "User"

    users_page.open_page()
    users_page.open_create_form()

    create_page.fill_user_form(email, first_name, last_name)
    create_page.save_user()

    users_page.open_page()
    users_page.open_edit_form(email)

    assert edit_page.get_email() == email
    assert edit_page.get_first_name() == first_name
    assert edit_page.get_last_name() == last_name

    updated_email = f"updated_{uuid4()}@example.com"
    updated_first_name = "Updated"
    updated_last_name = "UserUpdated"

    edit_page.update_user(
        updated_email,
        updated_first_name,
        updated_last_name
    )
    edit_page.save_user()

    assert users_page.page_is_opened()
    assert users_page.user_is_in_table(updated_email)

@pytest.mark.smoke
def test_user_email_validation(logged_in_user, base_url):
    users_page = UsersPage(logged_in_user, base_url)
    create_page = UserCreatePage(logged_in_user)
    edit_page = UsersEditPage(logged_in_user)

    email = f"test_{uuid4()}@example.com"

    users_page.open_page()
    users_page.open_create_form()

    create_page.fill_user_form(email, "Test", "User")
    create_page.save_user()

    users_page.open_page()
    users_page.open_edit_form(email)

    edit_page.update_email("111")
    edit_page.save_user()

    assert edit_page.email_is_invalid()
    assert edit_page.email_error_is_displayed()

@pytest.mark.smoke
def test_user_can_be_deleted(logged_in_user, base_url):
    users_page = UsersPage(logged_in_user, base_url)
    create_page = UserCreatePage(logged_in_user)

    email = f"test_{uuid4()}@example.com"

    users_page.open_page()
    users_page.open_create_form()

    create_page.fill_user_form(email, "Test", "Delete")
    create_page.save_user()

    users_page.open_page()

    assert users_page.user_is_in_table(email)

    users_page.select_user(email)
    users_page.delete_selected_user()

    assert users_page.deletion_notification_is_displayed("Element deleted")
    assert users_page.user_is_not_in_table(email)

@pytest.mark.smoke
def test_multiple_users_can_be_deleted(logged_in_user, base_url):
    users_page = UsersPage(logged_in_user, base_url)
    create_page = UserCreatePage(logged_in_user)

    first_email = f"test_{uuid4()}@example.com"
    second_email = f"test_{uuid4()}@example.com"

    users_page.open_page()

    users_page.open_create_form()
    create_page.fill_user_form(first_email, "First", "User")
    create_page.save_user()

    users_page.open_page()

    users_page.open_create_form()
    create_page.fill_user_form(second_email, "Second", "User")
    create_page.save_user()

    users_page.open_page()

    assert users_page.user_is_in_table(first_email)
    assert users_page.user_is_in_table(second_email)

    users_page.select_user(first_email)
    users_page.select_user(second_email)

    users_page.delete_selected_user()

    assert users_page.deletion_notification_is_displayed(
        "2 elements deleted"
    )

    assert users_page.user_is_not_in_table(first_email)
    assert users_page.user_is_not_in_table(second_email)

@pytest.mark.smoke
def test_all_users_can_be_deleted(logged_in_user, base_url):
    users_page = UsersPage(logged_in_user, base_url)

    users_page.open_page()

    assert users_page.table_is_loaded()

    users_page.select_all_users()
    users_page.delete_selected_user()

    assert users_page.users_list_is_empty()