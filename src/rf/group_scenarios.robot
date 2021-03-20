*** Settings ***
Library  src.rf.AddressBook
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new group
    Create Group  ?name>  :header;  =footer+

