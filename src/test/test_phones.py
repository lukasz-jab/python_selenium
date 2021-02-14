import re


def test_phones_on_main_page(app):
    contact_from_home_page = app.contact.get_contacs_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(contact_from_home_page.id)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # in aplication version 9.0, secondaryphone(fax) is not displayed in home page in the table


def test_phones_on_view_page(app):
    test_contact = app.contact.get_contacs_list()[0]
    contact_from_view_page = app.contact.get_contact_info_from_view_page(test_contact.id)
    print(contact_from_view_page.all_phones_from_home_page)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(test_contact.id)
    assert clear(contact_from_view_page.all_phones_from_home_page) == merge_phones_like_on_home_page(contact_from_edit_page)
    # in aplication version 9.0, secondaryphone is field fax not added due to incompatibility with home page test


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x), filter(lambda x: x is not None,
                                                            [contact.homephone, contact.mobilephone, contact.workphone])))))
