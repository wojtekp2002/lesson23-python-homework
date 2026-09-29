"""Prosta książka adresowa przechowywana w słowniku."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Contact:
    first_name: str
    last_name: str
    phone: str
    email: str


class AddressBook:
    """Książka adresowa, w której kluczem kontaktu jest unikalne ID."""

    def __init__(self) -> None:
        self.contacts: dict[int, Contact] = {}
        self._next_id = 1

    def add_contact(
        self, first_name: str, last_name: str, phone: str, email: str
    ) -> int:
        validate_contact_data(first_name, last_name, phone, email)
        contact_id = self._next_id
        self.contacts[contact_id] = Contact(first_name, last_name, phone, email)
        self._next_id += 1
        return contact_id

    def list_contacts(self) -> dict[int, Contact]:
        return dict(self.contacts)

    def search_contacts(self, phrase: str) -> dict[int, Contact]:
        phrase = phrase.strip().lower()
        return {
            contact_id: contact
            for contact_id, contact in self.contacts.items()
            if phrase in contact.first_name.lower()
            or phrase in contact.last_name.lower()
        }

    def delete_contact(self, contact_id: int) -> bool:
        return self.contacts.pop(contact_id, None) is not None

    def edit_contact(
        self,
        contact_id: int,
        first_name: str | None = None,
        last_name: str | None = None,
        phone: str | None = None,
        email: str | None = None,
    ) -> bool:
        contact = self.contacts.get(contact_id)
        if contact is None:
            return False

        updated = Contact(
            first_name=first_name if first_name else contact.first_name,
            last_name=last_name if last_name else contact.last_name,
            phone=phone if phone else contact.phone,
            email=email if email else contact.email,
        )
        validate_contact_data(
            updated.first_name, updated.last_name, updated.phone, updated.email
        )
        self.contacts[contact_id] = updated
        return True


def validate_contact_data(
    first_name: str, last_name: str, phone: str, email: str
) -> None:
    if not first_name.strip():
        raise ValueError("Imię nie może być puste.")
    if not last_name.strip():
        raise ValueError("Nazwisko nie może być puste.")
    if not phone.isdigit():
        raise ValueError("Numer telefonu może składać się tylko z cyfr.")
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Podaj poprawny adres email.")


def read_required(prompt: str) -> str:
    value = input(prompt).strip()
    while not value:
        print("To pole jest wymagane.")
        value = input(prompt).strip()
    return value


def read_contact_id() -> int | None:
    value = input("Podaj ID kontaktu: ").strip()
    if not value.isdigit():
        print("ID musi być liczbą.")
        return None
    return int(value)


def print_contacts(contacts: dict[int, Contact]) -> None:
    if not contacts:
        print("Brak kontaktów.")
        return

    for contact_id, contact in contacts.items():
        print(
            f"{contact_id}. {contact.first_name} {contact.last_name} | "
            f"tel. {contact.phone} | {contact.email}"
        )


def prompt_contact_data() -> tuple[str, str, str, str]:
    return (
        read_required("Imię: "),
        read_required("Nazwisko: "),
        read_required("Telefon: "),
        read_required("Email: "),
    )


def add_contact_from_menu(address_book: AddressBook) -> None:
    try:
        contact_id = address_book.add_contact(*prompt_contact_data())
    except ValueError as error:
        print(f"Błąd: {error}")
        return
    print(f"Dodano kontakt z ID {contact_id}.")


def search_contacts_from_menu(address_book: AddressBook) -> None:
    phrase = read_required("Szukaj po imieniu lub nazwisku: ")
    print_contacts(address_book.search_contacts(phrase))


def delete_contact_from_menu(address_book: AddressBook) -> None:
    contact_id = read_contact_id()
    if contact_id is None:
        return
    if address_book.delete_contact(contact_id):
        print("Kontakt usunięty.")
    else:
        print("Nie znaleziono kontaktu o podanym ID.")


def edit_contact_from_menu(address_book: AddressBook) -> None:
    contact_id = read_contact_id()
    if contact_id is None:
        return

    current = address_book.contacts.get(contact_id)
    if current is None:
        print("Nie znaleziono kontaktu o podanym ID.")
        return

    print("Zostaw puste pole, aby zachować obecną wartość.")
    try:
        updated = address_book.edit_contact(
            contact_id,
            first_name=input(f"Imię [{current.first_name}]: ").strip() or None,
            last_name=input(f"Nazwisko [{current.last_name}]: ").strip() or None,
            phone=input(f"Telefon [{current.phone}]: ").strip() or None,
            email=input(f"Email [{current.email}]: ").strip() or None,
        )
    except ValueError as error:
        print(f"Błąd: {error}")
        return

    print("Kontakt zaktualizowany." if updated else "Nie udało się edytować kontaktu.")


def print_menu() -> None:
    print("\nKsiążka adresowa")
    print("1. Dodaj kontakt")
    print("2. Wyświetl wszystkie kontakty")
    print("3. Wyszukaj kontakt")
    print("4. Usuń kontakt")
    print("5. Edytuj kontakt")
    print("0. Zakończ")


def main() -> None:
    address_book = AddressBook()

    while True:
        print_menu()
        choice = input("Wybierz opcję: ").strip()

        if choice == "1":
            add_contact_from_menu(address_book)
        elif choice == "2":
            print_contacts(address_book.list_contacts())
        elif choice == "3":
            search_contacts_from_menu(address_book)
        elif choice == "4":
            delete_contact_from_menu(address_book)
        elif choice == "5":
            edit_contact_from_menu(address_book)
        elif choice == "0":
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana opcja. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
