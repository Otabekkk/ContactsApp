// function confirmDelete(contact_id) {
//     var result = confirm('Вы правда хотите удалить контакт?')

//     if (result) {
//         window.location.href = 'delete/' + contact_id;
//     }
// }


function openModal(contact_id) {
    document.getElementById("confirm").style.display = 'block';

    document.getElementById("confirmDeleteBtn").onclick = function() {
        window.location.href = 'delete/' + contact_id;
        closeModal();
    }

}

function closeModal() {
    document.getElementById("confirm").style.display = "none";
}   