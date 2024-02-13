const url = 'https://rizz.gizmolab.net/get_records';

let post_counter = -1;

function fetchMessages() {
    if (typeof fetchMessages.post_count == "undefined") {
        fetchMessages.post_count = 0;
    }
    fetch(url)
        .then(response => response.json())
        .then(messages => {
            messages.forEach(message => {
                if (message.counter > post_counter) {
                    addAnnouncement(message);
                    post_counter = message.counter;
                }
            });
        })
        .catch(error => console.error('Error:', error));
};

setInterval(fetchMessages, 5 * 1000);

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

fetchMessages()
