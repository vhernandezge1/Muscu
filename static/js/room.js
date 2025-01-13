// Récupérer le nom de la salle depuis le HTML (sans JSON.parse)
const roomName = document.getElementById("room-name").textContent;

// Créer une connexion WebSocket
const chatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data); // Les messages reçus doivent être un JSON valide
    const chatLog = document.querySelector("#chat-log");
    chatLog.innerHTML += `<div>${data.message}</div>`; // Ajouter le message reçu
    chatLog.scrollTop = chatLog.scrollHeight; // Scroll automatique en bas
};

chatSocket.onclose = function (e) {
    console.error("Chat socket closed unexpectedly");
};

// Gérer l'envoi du message
document.querySelector("#chat-message-input").focus();
document.querySelector("#chat-message-input").onkeyup = function (e) {
    if (e.keyCode === 13) {
        // Appuyer sur Entrée pour envoyer
        document.querySelector("#chat-message-send").click();
    }
};

document.querySelector("#chat-message-send").onclick = function (e) {
    const messageInputDom = document.querySelector("#chat-message-input");
    const message = messageInputDom.value;

    // Envoyer le message via WebSocket
    chatSocket.send(
        JSON.stringify({
            message: message,
        })
    );

    messageInputDom.value = ""; // Vider le champ de texte après envoi
};
