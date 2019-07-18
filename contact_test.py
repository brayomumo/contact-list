import unittest
from contact import Contact
import pyperclip


class EstContact(unittest.TestCase):
    def setUp(self):
        self.new_contact = Contact(
            "james", "Muriuki", "0746743772", "james@ms.com")

    def tearDown(self):
        Contact.contact_list = []
    def test_init(self):
        self.assertEqual(self.new_contact.first_name, "james")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "0746743772")
        self.assertEqual(self.new_contact.email, "james@ms.com")

    def test_save_(self):
        self.new_contact.save_contact()

        self.assertEqual(len(Contact.contact_list), 1)
    def test_save_multiple_contacts(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678", "test@fgf.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    def test_delete_contact (self):
        self.new_contact.save_contact()
        test_contact =Contact("test", "user","078654321","test@df.com")
        test_contact.save_contact()

        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)
    



    def test_find_contact_by_number(self):


        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0711223344")

        self.assertEqual(found_contact.email,test_contact.email)
    def test_contact_exists(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()

        contact_exists = Contact.contact_exist("0711223344")

        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        self.assertEqual(Contact.display_contacts(),Contact.contact_list)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_contact.save_contact()
        Contact.copy_email("test@user.com")

        self.assertEqual(self.new_contact.email,pyperclip.paste())
    
if __name__ == '__main__':
    unittest.main()
