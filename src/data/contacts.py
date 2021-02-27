from src.model.contact import Contact

testdata = [
    Contact(firstname="firstname1", lastname="lastname1", homephone="1+1+1 1", mobilephone="2-2-2 2",
            workphone="(3(3)3) 3", address="adress", notes="notes"),
    Contact(firstname="?firstname2*", lastname="=lastname2&", homephone="1+1+1 1", mobilephone="2-2-2 2",
            workphone="(3(3)3) 3", address="*adress?", notes="*notes/")
]

#
# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + " "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# test_data= [
#     Contact(firstname=random_string("name", 10), lastname=random_string("name", 10), homephone="1+1+1 1", mobilephone="2-2-2 2",
#                       workphone="(3(3)3) 3", address=random_string("adress", 30), notes=random_string("notes", 50))
#     for i in range(3)]
