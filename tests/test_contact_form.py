import time
from pages.contact_page import ContactPage
from utils.config import BASE_URL, CONTACT_URL

def test_contact_form_validation_and_submission(driver):
    contact = ContactPage(driver)
    contact.go(CONTACT_URL)
    print("--> contact page loaded")

    contact.submit_empty()
    print("--> empty form submited")
    assert contact.has_validation_errors(), 'Expected validation errors when submitting blank form'

    contact.fill_form('Arpita', 'Test', 'arpita@example.com', 'Hello! This is a test message. lorem ipsam lorem ipsam lorem ipsam lorem ipsam')
    time.sleep(1)
    assert contact.success_message_present(), 'Expected success message after valid form submission'
