const url = 'http://localhost:8080/get_records';

function fetchMessages() {
    fetch(url)
        .then(response => response.json())
        .then(messages => {
            messages.forEach(message => {
                addAnnouncement(message);
            });
        })
        .catch(error => console.error('Error:', error));
}

setInterval(fetchMessages, 1 * 1000);

function addAnnouncement(message) {
    var announcementWall = document.getElementById('announcementWall');
    var messageElement = document.createElement('div');
    messageElement.className = 'message';

    var fromText = document.createElement('span');
    fromText.className = 'from';
    fromText.appendChild(document.createTextNode(message.from));
    messageElement.appendChild(fromText);

    var textElement = document.createElement('span');
    textElement.className = 'text';
    textElement.appendChild(document.createTextNode(message.text));
    messageElement.appendChild(textElement);

    announcementWall.appendChild(messageElement);

    announcementWall.scrollTop = announcementWall.scrollHeight;
}
