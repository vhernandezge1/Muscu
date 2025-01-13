const roomName = JSON.parse(document.getElementById('room-name').textContent);
let chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
);

// Réception des messages du serveur
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const message = data.message;

    const chatLog = document.querySelector('#chat-log');
    chatLog.innerHTML += '<p>' + message + '</p>';
    chatLog.scrollTop = chatLog.scrollHeight; // Scroll automatique
};

// Gestion des fermetures de WebSocket
chatSocket.onclose = function(e) {
    console.error('WebSocket fermé. Tentative de reconnexion dans 5 secondes.', e);
    setTimeout(() => {
        reconnectWebSocket();
    }, 5000);
};

// Envoi des messages au serveur
document.querySelector('#chat-message-send').onclick = function(e) {
    const messageInput = document.querySelector('#chat-message-input');
    const message = messageInput.value;
    if (chatSocket.readyState === WebSocket.OPEN && message.trim() !== '') {
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        messageInput.value = ''; // Réinitialiser l'input
    } else {
        console.error('Impossible d’envoyer : WebSocket fermé.');
    }
};

// Permet d'envoyer le message en appuyant sur Entrée
document.querySelector('#chat-message-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        document.querySelector('#chat-message-send').click();
    }
});

// Fonction pour reconnecter le WebSocket
function reconnectWebSocket() {
    chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const message = data.message;

        const chatLog = document.querySelector('#chat-log');
        chatLog.innerHTML += '<p>' + message + '</p>';
        chatLog.scrollTop = chatLog.scrollHeight;
    };

    chatSocket.onclose = function(e) {
        console.error('WebSocket fermé à nouveau. Tentative de reconnexion dans 5 secondes.', e);
        setTimeout(() => {
            reconnectWebSocket();
        }, 5000);
    };

    console.log('WebSocket reconnecté.');
}
