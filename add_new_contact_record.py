from time import sleep
from simple_salesforce import Salesforce

# Establish a connection
instance_url = "https://xxx-dev-ed.my.salesforce.com"
access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
sf = Salesforce(instance_url=instance_url, session_id=access_token)

def add_new_contact(no):
    # Create a dictionary containing contact details
    contact_details = {
        'LastName': 'Doe',
        'FirstName': 'John',
        'Phone': '1234567890',
        'Email': 'john.doe@example.com'
    }

    contact_details['FirstName'] += f'test'
    contact_details['LastName'] += f'{no}'
    contact_details['Phone'] += f'129{no}'
    contact_details['Email'] = f'test.{no}@example.com'

    # Insert the contact record
    result = sf.Contact.create(contact_details)

    # Check the result
    if result['success']:
        print(no, 'Contact inserted successfully. Contact ID:', result['id'])
    else:
        print(no, 'Contact insertion failed. Error:', result['errors'])

for x in range(3000):
    add_new_contact(x)
    # sleep(0.025)