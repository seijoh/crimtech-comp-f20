// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];

function respond() {
    // Your Code Here
    console.log("Hello World!");
    var img_path = "img/";
    var response_text = "H";
    var quote_index = Math.floor(Math.random() * 5);

    speech = document.getElementById("textbox").value;
    if (speech.includes("cute") || speech.includes("baby")) {
        img_path += names[0];
        let num_m = Math.floor(Math.random() * 10) + 10;
        for (i = 0; i < num_m; i++) {
            response_text += "m"
        }
        response_text += "."
    } else {
        img_path += names[1]
        if (speech.includes("dark")) {
            response_text = dark_quotes[quote_index]
        } else if (speech.includes("force")) {
            response_text = force_quotes[quote_index]
        } else {
            response_text = std_quotes[quote_index]
        }
    }
    img_path += "-";
    if (speech.includes("force")) {
        if (speech.includes("dark")) {
            img_path += moods[0]
        } else {
            img_path += moods[1]
        }
    } else {
        img_path += moods[2]
    }
    img_path += ".jpg";

    document.getElementById("yoda_img").setAttribute("src", img_path);
    document.getElementById("response").innerHTML = response_text;
}
