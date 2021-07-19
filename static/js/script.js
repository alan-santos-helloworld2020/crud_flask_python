window.onload = M.AutoInit();


function deletar(event){
 
    if(!confirm('Deseja realmente excluir')){
        event.preventDefault()
        return false
    }
}

function editar(event,cl){
    document.getElementById('id_cliente').value = cl[0]
    document.getElementById('nome').value = cl[1]
    document.getElementById('telefone').value = cl[2]
    document.getElementById('email').value = cl[3]
    document.getElementById('cep').value = cl[4]
    event.preventDefault()
}