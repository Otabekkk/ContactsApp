function confirmDelete(contact_id) {
    var result = confirm('Вы правда хотите удалить контакт?')

    if (result) {
        window.location.href = 'delete/' + contact_id;
    }
}