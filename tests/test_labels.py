from uuid import uuid4

from pages.label_create_page import LabelCreatePage
from pages.label_edit_page import LabelEditPage
from pages.labels_page import LabelsPage


def create_label(labels_page, create_page, label_name):
    labels_page.open_page()
    labels_page.open_create_form()

    create_page.fill_label_form(label_name)
    create_page.save_label()

    assert create_page.creation_notification_is_displayed()


def test_labels_page_is_opened(logged_in_user, base_url):
    labels_page = LabelsPage(logged_in_user, base_url)

    labels_page.open_page()

    assert labels_page.table_is_loaded()


def test_label_create_form_is_opened(logged_in_user, base_url):
    labels_page = LabelsPage(logged_in_user, base_url)
    create_page = LabelCreatePage(logged_in_user)

    labels_page.open_page()
    labels_page.open_create_form()

    assert create_page.name_is_displayed()


def test_label_can_be_created(logged_in_user, base_url):
    labels_page = LabelsPage(logged_in_user, base_url)
    create_page = LabelCreatePage(logged_in_user)

    label_name = f"Test Label {uuid4()}"

    create_label(labels_page, create_page, label_name)

    labels_page.open_page()

    assert labels_page.label_is_in_table(label_name)


def test_labels_table_displays_all_labels(logged_in_user, base_url):
    labels_page = LabelsPage(logged_in_user, base_url)

    labels_page.open_page()

    assert labels_page.table_is_loaded()
    assert labels_page.names_are_displayed()


def test_label_can_be_edited(logged_in_user, base_url):
    labels_page = LabelsPage(logged_in_user, base_url)
    create_page = LabelCreatePage(logged_in_user)
    edit_page = LabelEditPage(logged_in_user)

    label_name = f"Test Label {uuid4()}"
    updated_label_name = f"Updated Label {uuid4()}"

    create_label(labels_page, create_page, label_name)

    labels_page.open_page()
    labels_page.open_edit_form(label_name)

    assert edit_page.name_is_displayed()

    edit_page.update_label_name(updated_label_name)
    edit_page.save_label()

    assert edit_page.update_notification_is_displayed()
    assert labels_page.label_is_in_table(updated_label_name)


def test_label_can_be_deleted(logged_in_user, base_url):
    labels_page = LabelsPage(logged_in_user, base_url)
    create_page = LabelCreatePage(logged_in_user)

    label_name = f"Delete Label {uuid4()}"

    create_label(labels_page, create_page, label_name)

    labels_page.open_page()

    assert labels_page.label_is_in_table(label_name)

    labels_page.select_label(label_name)
    labels_page.delete_selected_labels()

    assert labels_page.deletion_notification_is_displayed()
    assert labels_page.label_is_not_in_table(label_name)


def test_multiple_labels_can_be_deleted(logged_in_user, base_url):
    labels_page = LabelsPage(logged_in_user, base_url)
    create_page = LabelCreatePage(logged_in_user)

    label_names = [
        f"Delete Label {uuid4()}",
        f"Delete Label {uuid4()}",
    ]

    for label_name in label_names:
        create_label(labels_page, create_page, label_name)

    labels_page.open_page()

    for label_name in label_names:
        assert labels_page.label_is_in_table(label_name)

    labels_page.select_labels(label_names)
    labels_page.delete_selected_labels()

    assert labels_page.deletion_notification_is_displayed()

    for label_name in label_names:
        assert labels_page.label_is_not_in_table(label_name)
