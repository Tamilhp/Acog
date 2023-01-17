let msg_element = document.getElementById("msg")
let request = new XMLHttpRequest();
request.open("GET", "/message")
request.send()
request.onload = () => {
    console.log(request);
    if (request.status == 200) {
        result = JSON.parse(request.response);
        msg_element.innerHTML = result.msg
    } else {
        console.log(`error: ${request.status} ${request.statusText}`)
    }
}

