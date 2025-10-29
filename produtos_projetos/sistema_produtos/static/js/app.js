function removerProduto(codigo) {
    // 1. Pede confirmação ao utilizador
    if (!confirm('Tem a certeza de que deseja remover este produto?')) {
        return; // Se cancelar, não faz nada
    }

    // 2. Envia a requisição AJAX para o servidor
    fetch(`/api/remover/${codigo}`, {
        method: 'DELETE',
    })
    .then(response => response.json()) // Converte a resposta para JSON
    .then(data => {
        // 3. Verifica se a remoção foi bem-sucedida
        if (data.success) {
            // 4. Remove a linha da tabela da interface
            const linhaParaRemover = document.getElementById(`produto-${codigo}`);
            if (linhaParaRemover) {
                // Adiciona um efeito de fade-out antes de remover
                linhaParaRemover.style.transition = 'opacity 0.5s ease';
                linhaParaRemover.style.opacity = '0';
                setTimeout(() => linhaParaRemover.remove(), 500);
            }
            // Opcional: Em vez de um alert, podemos criar uma notificação mais elegante no futuro
            console.log(data.message); 
        } else {
            // Mostra uma mensagem de erro se algo correr mal
            alert('Erro: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Erro na requisição:', error);
        alert('Ocorreu um erro de comunicação com o servidor.');
    });
}