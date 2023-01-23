import controller


class Phonebook:
    phone_book = []
    path = 'phone_book.txt'

    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as data:
            file = data.readlines()
        for contact in file:
            self.phone_book.append(contact.strip().split(';'))

    def save(self):
        pb_str = []
        for contact in self.phone_book:
            pb_str.append(';'.join(contact))
        with open(self.path, 'w', encoding='UTF-8') as data:
            data.write('\n'.join(pb_str))

    def get(self):
        return self.phone_book

    def new(self, new_contact: list):
        self. phone_book.append(new_contact)

    def search(self, find: str):
        result = []
        for contact in self.phone_book:
            for field in contact:
                if find in field:
                    result.append(contact)
                    break
        return result

    def delete(self, contact_for_delete: int):
        if contact_for_delete - 1 in range(len(self.phone_book)):
            for serial_number in range(len(self.phone_book)):
                if serial_number == contact_for_delete - 1:
                    del self.phone_book[serial_number]
        else:
            return False

    def change(self, contact_for_change: int, contact_change: list):
        self.phone_book[contact_for_change - 1][0] = contact_change[0] if contact_change[0] != '' else \
            self.phone_book[contact_for_change - 1][0]
        self.phone_book[contact_for_change - 1][1] = contact_change[1] if contact_change[1] != '' else \
            self.phone_book[contact_for_change - 1][1]
        self.phone_book[contact_for_change - 1][2] = contact_change[2] if contact_change[2] != '' else \
            self.phone_book[contact_for_change - 1][2]
