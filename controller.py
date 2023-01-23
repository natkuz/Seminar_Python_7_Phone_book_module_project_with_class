import view
import model


def start():
    pb = model.Phonebook()
    choice = ''
    while choice != 8:
        choice = view.main_menu()
        match choice:
            case 1:
                pb.open()
                view.view_open_file()
            case 2:
                pb.save()
                view.save_phone_book()
            case 3:
                view.show_contacts(pb.get())
            case 4:
                new_contact = list(view.create_new_contact())
                pb.new(new_contact)
                view.view_changes()
            case 5:
                view.show_contacts(pb.get())
                contact_for_del = view.del_contact()
                if contact_for_del in range(len(pb.phone_book) + 1):
                    confirm = view.del_confirm(contact_for_del, pb.phone_book[contact_for_del - 1][0])
                    if confirm:
                        pb.delete(contact_for_del)
                        view.view_changes()
                    else:
                        view.undo_changes()
                else:
                    view.input_error()
            case 6:
                view.show_contacts(pb.get())
                contact_for_change = view.select_change_contact()
                if contact_for_change in range(len(pb.phone_book)):
                    contact_change = list(view.modification_contact())
                    pb.change(contact_for_change, contact_change)
                    view.view_changes()
                else:
                    view.input_error()

            case 7:
                find = view.find_contact()
                result = pb.search(find)
                view.show_contacts(result)
            case 8:
                view.exit_prog()
            case _:
                view.input_error()
