import os

BASE_URL = os.getenv('BASE_URL', 'https://practicesoftwaretesting.com/')
CONTACT_URL = os.getenv('CONTACT_URL', 'https://practicesoftwaretesting.com/contact')
BROWSER = os.getenv('BROWSER', 'chrome')
HEADLESS = os.getenv('HEADLESS', 'false').lower() in ('1', 'true', 'yes')
IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '5'))
