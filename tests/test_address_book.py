import unittest

from src.address_book import AddressBook, validate_contact_data


class AddressBookTest(unittest.TestCase):
    def test_add_search_edit_and_delete_contact(self):
        book = AddressBook()

        contact_id = book.add_contact("Jan", "Kowalski", "123456789", "jan@example.com")

        self.assertEqual(contact_id, 1)
        self.assertEqual(book.search_contacts("kowal")[contact_id].first_name, "Jan")

        self.assertTrue(book.edit_contact(contact_id, phone="987654321"))
        self.assertEqual(book.contacts[contact_id].phone, "987654321")

        self.assertTrue(book.delete_contact(contact_id))
        self.assertEqual(book.list_contacts(), {})

    def test_contacts_are_stored_under_unique_ids(self):
        book = AddressBook()

        first_id = book.add_contact("Anna", "Nowak", "111222333", "anna@example.com")
        second_id = book.add_contact(
            "Piotr", "Zielinski", "444555666", "piotr@example.com"
        )

        self.assertNotEqual(first_id, second_id)
        self.assertEqual(set(book.list_contacts()), {first_id, second_id})

    def test_validate_contact_data_rejects_invalid_values(self):
        invalid_values = [
            ("", "Nowak", "123", "a@example.com"),
            ("Anna", "", "123", "a@example.com"),
            ("Anna", "Nowak", "12a", "a@example.com"),
            ("Anna", "Nowak", "123", "bez-malpy.example.com"),
            ("Anna", "Nowak", "123", "a@example"),
        ]

        for values in invalid_values:
            with self.subTest(values=values):
                with self.assertRaises(ValueError):
                    validate_contact_data(*values)


if __name__ == "__main__":
    unittest.main()
