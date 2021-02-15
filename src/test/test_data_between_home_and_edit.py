import random
import re


def test_data_home_edit_sites(app):
    index = app.contact.get_contacs_list()
    contact_from_home_page = app.contact.get_contacs_list()[random.randint(0,len(index)-1)]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(contact_from_home_page.id)
    # test all phones in file: test_phones.py
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)
    # main page cut more than one space " "
    assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", (map (lambda x: x, (filter(lambda x: x is not None,
                                                           [contact.emial_1, contact.emial_2, contact.emial_3]))))))
def clear(s):
    return re.sub(" ", "", s)
