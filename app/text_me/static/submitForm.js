document.getElementById("textForm").addEventListener("submit", function(event) {
    event.preventDefault(); 

    fetch("/", {
        method: "POST",
        body: new FormData(event.target)
    })
    .then(response => {
        if (response.ok) {
            var success_toast = document.getElementById("success-toast");
            success_toast.style.display = "block";
            setTimeout(function() {
                success_toast.style.display = "none";
            }, 3000);
	    document.getElementById("reset-button").click(); 
        } else {
            var fail_toast = document.getElementById("fail-toast");
            fail_toast.style.display = "block";
            setTimeout(function() {
                fail_toast.style.display = "none";
            }, 3000);
        }
    })
    .catch(error => {
        console.error("Error sending the message", error);
    });
});
