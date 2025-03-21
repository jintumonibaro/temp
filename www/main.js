$(document).ready(function () {
    console.log("Document ready");

    $("#MicBtn").click(function () {
        console.log("Voice Chat button clicked");

        
        eel.speak("Hello dickless Fellow, how can I help you?")(function () {
            console.log("Greeting spoken");

            
            eel.takeCommand()(function (response) {
                console.log("Recognized Speech: " + response);
            });
        });
    });
});
