
// ~~~~~~~~~~~~~~~~~~~EXERCISE 1
let a = Math.floor(Math.random() * 10);
a = Number.parseInt(a);
let b;
let timesOfGuesses = 5;
timesOfGuesses = Number.parseInt(timesOfGuesses);
let gngk = document.getElementById('gngk')
gngk.addEventListener('click', gng)
function gng() {
    console.log(a);
    while (b != a) {
        b = prompt("Guess a number between 1-10 \nYou have 5 Chances");
        b = Number.parseInt(b);
        if (b) {
            if (b == a) {
                alert(`YOU GUESSED THE RIGHT NUMBER WHICH IS ${a}. \n YOUR NUMBER OF GUESSES LEFT ARE ${timesOfGuesses}`);
                break
            }
            timesOfGuesses = timesOfGuesses - 1
            if (timesOfGuesses <= 0) {
                alert("your have reached your guesses limit!! \n Click New Game to try again.")
                gngk.removeEventListener('click', gng)
                break
            }
        }
        else {
            break
        }

    }
}

// `````````````````````````CONGRATULATIONS!!!!!!!!!!!!!!!!!!!!!!!!!``````````````

// ~~~~~~~~~~~~~~~~~EXERCISE 2
let q = 0;
let sgwButt = document.getElementById('sgwButt')
sgwButt.addEventListener('click', game)
function game() {
    new Promise((resolve) => {
        let o = 3;
        while (o != 0) {
            let cpu = Math.floor(Math.random() * 3);
            let cp = ["s", "w", "g"][cpu];
            console.log(cp)
            let k = prompt('ENTER "s" FOR SNAKE \n ENTER "g" FOR GUN \n ENTER "w" FOR WATER');
            if (k) {
                o = o - 1;
                if (cp === k) {
                    alert("Tie");
                    location.reload()
                }
                else if (k === 's' && cp === 'w') {
                    alert("YOU WIN!");
                    q += 1
                    location.reload()
                }
                else if (k === 's' && cp === 'g') {
                    alert("YOU LOSE");
                    q -= 1
                    location.reload()
                }
                else if (k === 'w' && cp === 's') {
                    alert("YOU LOSE!");
                    q -= 1
                    location.reload()
                }
                else if (k === 'w' && cp === 'g') {
                    alert("YOU WIN!");
                    q += 1
                    location.reload()
                }
                else if (k === 'g' && cp === 's') {
                    alert("YOU WIN!");
                    q += 1
                    location.reload()
                }
                else if (k === 'g' && cp === 'w') {
                    alert("YOU LOSE!");
                    q -= 1
                    location.reload()
                }
                if (o == 0) {
                    alert("YOU USSED ALL CHANCES");
                    sgwButt.removeEventListener('click', game);
                    break;
                }
            }
            else {
                break
            }
            let queh = localStorage.setItem('0', q)
            resolve(queh)
        }
    }).then(() => {
        let queh2 = localStorage.getItem('0')
        console.log(queh2)
        if (queh2 >= 2) {
            alert("YOU WIN THE WHOLE GAME!");
        }
        else if (queh2 <= 1) {
            alert("YOU LOSE THE WHOLE GAME!");
        }
        else {
            console.log('Canceled')
        }
    }).catch((err) => {
        console.log(err)
    });
}

// ~~~~~~~~~~~~~~~~~~~EXERCISE 3
let ar = ['What do kids play when their mom is using the phone? Bored games.', 'What do you call an ant who fights crime? A vigilANTe!', 'Why are snails slow? Because they\'re carrying a house on their back.', 'What\'s the smartest insect? A spelling bee!', 'What does a storm cloud wear under his raincoat? Thunderwear.', 'What is fast, loud and crunchy? A rocket chip.', 'How does the ocean say hi? It waves!', 'What do you call a couple of chimpanzees sharing an Amazon account? PRIME-mates.', 'Why did the teddy bear say no to dessert? Because she was stuffed.', 'Why did the soccer player take so long to eat dinner? Because he thought he couldn\'t use his hands.', 'Name the kind of tree you can hold in your hand? A palm tree!', ' What do birds give out on Halloween? Tweets.', 'What has ears but cannot hear? A cornfield.', 'What\'s a cat\'s favorite dessert? A bowl full of mice-cream.', 'Where did the music teacher leave her keys? In the piano!', 'What did the policeman say to his hungry stomach? “Freeze. You\'re under a vest.”', ' What did the left eye say to the right eye? Between us, something smells!', 'What do you call a guy who\'s really loud? Mike.', ' Why do birds fly south in the winter? It\'s faster than walking!', 'What did the lava say to his girlfriend? “I lava you!”'];
let rando = Math.floor(Math.random() * ar.length - 1);
function jo(joke) {
    joke[0].innerHTML = ar[rando]
}
let joke = document.body.getElementsByClassName("joke")
jo(joke)

// ~~~~~~~~~~~~~~~~~~~EXERCISE 4

const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
let clock = document.getElementById("clock")
setInterval(() => {
    const d = new Date();
    let year = d.getFullYear();
    let month = months[d.getMonth()];
    let Day = day[d.getDay()];
    let date = d.getDate();
    let hours = d.getHours();
    let minutes = d.getMinutes();
    let seconds = d.getSeconds();
    let milliseconds = d.getMilliseconds();
    let time = `Year-${year}\t | Month-${month}\t | Day-${Day}\t | Date-${date}\t | ${'<br>'} ${hours}h: ${minutes}min: ${seconds}sec ${milliseconds}milliSec`
    clock.innerHTML = time;
}, 1000);

//~~~~~~~~~~~~~~~~~~~~~~EXERCISE 5

let arr = [
    'Initializing Hack Tool...',
    'Connecting to Facebook...',
    'connecting to server 1...',
    'connection failed. Retrying....',
    'connected Succesfully...',
    'Username "Ameesha"...',
    'Trying Brute Force...',
    '200k passwords tried...',
    'Match not found...',
    'Another 200k password tried...',
    'Match not found...',
    'Another 200k password tried...',
    'Match found...',
    'Accessing Account...',
    'Hack Successful...'
]
let ti = async () => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(true)
        }, 2000)
    })
}
let fin = async function (message) {
    await ti()
    text.innerHTML = text.innerHTML + message + '<br>'
}
let lo = async function () {
    for (let i = 0; i < arr.length; i++) {
        await fin(arr[i]);
    }
}
lo()

// ```````````````ExTra Question
let arr2 = [
    {
        "word": "nature",
        "definitions": ["the complex of emotional and intellectual attributes that determine a person's characteristic actions and reactions", "the natural physical world including plants and animals and landscapes etc."
        ]
    },
    {
        "word": "animal",
        "definitions": [
            "marked by the appetites and passions of the body", "a living organism characterized by voluntary movement"
        ]
    }
]

let buto = document.getElementById('butoText')
let fomdTex = document.getElementById('raTexs')
buto.onclick = function name3() {
    let fomd = document.getElementById('inP').value
    for (let key in arr2) {
        if (Object.hasOwnProperty.call(arr2, key)) {
            key = Number.parseInt(key)
            const element = arr2[key];
            let word = element.word
            let definitio = element.definitions
            // console.log(element.definitions[0])
            for (let i = 0; i < definitio.length; i++) {
                const el = definitio[i];
                if (fomd == word) {
                    fomdTex.innerHTML = fomdTex.innerHTML + (`Meaning: ${el} ${'<br>'}`)
                }
            }
        }
    }
}

// Quote Fetcher
async function anime() {
    try {
        let options = {
            method: 'GET',
            headers: {
                'Content-type': 'application/json',
            },
        }
        let fetc = await fetch("https://animechan.vercel.app/api/quotes", options)
        let response = await fetc.json()
        let quotae = document.getElementById('quote')
        for (const key in response) {
            if (Object.hasOwnProperty.call(response, key)) {
                function porto() {
                    // quoteButton.onclick = function sdf() {
                    return quotae.innerHTML = quotae.innerHTML + (`ANIME: ${response[key].anime} ${'<br>'} CHARACTER: ${response[key].character} ${'<br>'} QUOTE: ${response[key].quote} <br> <br> <br>`)
                    // }
                }
                porto()
            }
        }
    } catch (error) {
        console.log(error)
    }
}
// e.preventDefault() for preventing reload
anime()

//~~~~~~~~~~~~~~~~~~~~~~EXERCISE 6
// NOTE SAVING APP  
let saveNoteTitle = document.getElementById('saveNoteTitle')
let saveNote = document.getElementById('saveNote')
let SaveNoteId = document.getElementById('SaveNoteId')
let Saved = document.getElementById('Saved')
let DeletButton = document.getElementById('DeletButton')
let Deleted = document.getElementById('Deleted')
let allTodo = document.getElementById('allTodo')
let ShowAllTodo = document.getElementById('ShowAllTodo')
try {
    SaveNoteId.addEventListener("click", save)
    function save() {
        let key = saveNoteTitle.value
        let value = saveNote.value
        if (key == '' || value == '') {
            Saved.innerHTML = Saved.innerHTML + `Title or Note is/are Empty, Write Something <br>`
        }
        else if (key) {
            localStorage.setItem(key, value)
            Saved.innerHTML = Saved.innerHTML + `Your Note Saved! <br> Title: "${key}" Note: "${value}" <br>`
        }
    }
    DeletButton.addEventListener("click", delet)

    function delet() {
        let key = saveNoteTitle.value
        let value = saveNote.value
        if (key == '' || value == '') {
            Deleted.innerHTML = Deleted.innerHTML + `Title or Note is/are Empty, Write Something <br>`
        }
        else if (key) {
            localStorage.removeItem(key, value)
            Deleted.innerHTML = Deleted.innerHTML + `"${key}" Titled Note Deleted <br>`
        }
    }

    allTodo.addEventListener('click', shoall)
    function shoall() {
        for (let i = 0; i < localStorage.length; i++) {
            let keyOf = localStorage.key(i);
            let valueOf = localStorage.getItem(keyOf);
            let tabl = `
            <table class="TodoTable">
      <thead>
        <tr>
          <th> Title: ${keyOf}</th>
          </tr>
          </thead>
          <tbody>
          <tr>
          <td> Note: ${valueOf}</td>
          
          </tr>
          </tbody>
          <tfoot>
            <td><button class="button sd"
             onclick="Wdeletew()">Delete</button></td>
      </tfoot>
        </table><br>`
            ShowAllTodo.innerHTML = ShowAllTodo.innerHTML + tabl

            if (ShowAllTodo.innerHTML != '') {
                allTodo.removeEventListener('click', shoall)
            }
            function Wdeletew() {
                // for (let i = 0; i < localStorage.length; i++) {
                //     let keyOfd = localStorage.key(i);
                //     let valueOfd = localStorage.getItem(keyOfd);
                //     localStorage.removeItem(keyOfd, valueOfd)
                //     return Deleted.innerHTML = Deleted.innerHTML + `${keyOfd} ${valueOfd} is deleted <br>`
                // }
                let div11 = document.getElementsByTagName("tr")[0]
                div11.remove()
                console.log('hey')
            }
        }
    }

} catch (error) {
    console.log(error)
}
// have to delete and edit table live

//~~~~~~~~~~~~~~~~~~~~~~EXERCISE 7
try {
    class Generator {
        constructor(lowercase, uppercase, numCase, specialCase) {
            this.lowercase = lowercase
            this.uppercase = uppercase
            this.numCase = numCase
            this.specialCase = specialCase
            this.num = ' '

        }
        ran(len) {
            // let low = Math.floor(Math.random() * lowercase.length)
            // let up = Math.floor(Math.random() * uppercase.length)
            // let int = Math.floor(Math.random() * numCase.length)
            // let special = Math.floor(Math.random() * specialCase.length)
            // let low2 = Math.floor(Math.random() * lowercase.length)
            // let up2 = Math.floor(Math.random() * uppercase.length)
            // let int2 = Math.floor(Math.random() * numCase.length)
            // let special2 = Math.floor(Math.random() * specialCase.length)
            // return lowercase[low] + uppercase[up] + numCase[int] + specialCase[special] + lowercase[low2] + uppercase[up2] + numCase[int2] + specialCase[special2]
            let i = 0
            while (i < len) {
                this.num += lowercase[Math.floor(Math.random() * lowercase.length)]
                this.num += uppercase[Math.floor(Math.random() * uppercase.length)]
                this.num += numCase[Math.floor(Math.random() * numCase.length)]
                this.num += specialCase[Math.floor(Math.random() * specialCase.length)]
                i += 3
            }
            this.num = this.num.substring(0, len)
            return this.num
        }
    }
    let lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    let uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    let numCase = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    let specialCase = ['@', '#', '$', '%']
    let passGener = new Generator(lowercase, uppercase, numCase, specialCase)
    passGener.ran(9)
    let CreatePass = document.getElementById('CreatePass')
    let generatePass = document.getElementById('generatePass')
    generatePass.addEventListener('click', genera)
    function genera() {
        CreatePass.value = CreatePass.value + passGener.ran()
        generatePass.innerHTML = '&#9745;'
        if (CreatePass.value != '') {
            generatePass.removeEventListener('click', genera)
        }
    }
    if (CreatePass.value == '') {
        generatePass.innerHTML = '&#9744;'
        generatePass.addEventListener('click', genera)
    }
} catch (error) {
    console.log(error)
}

//~~~~~~~~~~~~~~~~~~~~~~EXERCISE 8


const months2 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const day2 = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
let time1 = document.getElementById("time")
let card2 = document.getElementById("card2")
setInterval(() => {
    const d = new Date();
    let month = months2[d.getMonth()];
    let Day = day2[d.getDay()];
    let date = d.getDate();
    let hours = d.getHours();
    let minutes = d.getMinutes();
    let seconds = d.getSeconds();
    let milliseconds = d.getMilliseconds();
    let time = `Month-${month}\t | Day-${Day}\t | Date-${date}\t | ${'<br>'} ${hours}h: ${minutes}min: ${seconds}sec ${milliseconds}milliSec`
    time1.innerHTML = time;
}, 1000);

let inputTime = document.getElementById('inputTime');
let setAlarmButton = document.getElementById('setAlarmButton');
async function ht() {
    return new Promise((resolve) => {
        setAlarmButton.addEventListener('click', function handleClick(event) {
            let inpValue = inputTime.value
            if (inpValue != '') {
                function imnp() {
                    return card2.innerHTML = card2.innerHTML + `
                    <ul class='displalrm'>
                        <li>${inpValue}</li>
                    </ul> <label class="switch">
                    <input class='checkId' type="checkbox">
                    <span class="slider round"></span>
                    </label>` + '<br>'
                }
                resolve()
                imnp()
            }

            else {
                console.log('Make a Alarm First!')
            }
            let ne = new Date()
            let neH = ne.getHours()
            let neM = ne.getMinutes()
            // console.log(neH, neM)
            async function mix() {
                let hor1 = await inpValue[0]
                let hor2 = await inpValue[1]
                let hour1 = hor1 + hor2
                let mi1 = await inpValue[3]
                let mi2 = await inpValue[4]
                let min1 = mi1 + mi2
                // console.log(hour1, min1)
                let realH = (hour1 - neH) * 600000
                let realM = (min1 - neM) * 60000
                //  seconds ka farak thik karna hai
                // console.log(realH)
                // console.log(realM)
                // if (hour1 === neH && min1 === neM) {
                //     console.log('hey')
                // }
                let audio1 = document.getElementById('audio1')
                let audio2 = document.getElementById('audio2')
                let audio3 = document.getElementById('audio3')
                let OptionButt = document.getElementById('OptionButt')
                OptionButt.addEventListener('click',getOptions)
                async function getOptions() {
                    let selectElement = document.querySelector("#Audios")
                    let output = selectElement.value
                    console.log(output)
                    return output
                }
                let outputa = await getOptions()
                if (inpValue != '' && outputa=="audio1") {
                    console.log('Playing audio 1')
                    setTimeout(() => {
                        audio1.play()
                    }, realH + realM);
                }
                else if (inpValue != '' && outputa=="audio2") {
                    console.log('Playing audio 2')
                    setTimeout(() => {
                        audio2.play()
                    }, realH + realM);
                }
                else if (inpValue != '' && outputa=="audio3") {
                    console.log('Playing audio 3')
                    setTimeout(() => {
                        audio3.play()
                    }, realH + realM);
                }
                else{
                    console.log('Problem in playing audio')
                }
                
                if (inpValue == 'PM') {
                    console.log('PM')
                }
                else if (inpValue == 'AM') {
                    console.log('AM')
                }
            }
            mix()
        });
    })
}
let ht2 = await ht()

// let checkId = document.querySelector('.checkId')
// console.log(checkId)
// if (checkId.checked == true) {
//     console.log('hey')
// }

// element.remove()
// Checkbox: <input type="checkbox" id="myCheck" onclick="myFunction()">
// <p id="text" style="display:none">Checkbox is CHECKED!</p>
// function myFunction() {
//   // Get the checkbox
//   var checkBox = document.getElementById("myCheck");
//   // Get the output text
//   var text = document.getElementById("text");

//   // If the checkbox is checked, display the output text
//   if (checkBox.checked == true){
//     text.style.display = "block";
//   } else {
//     text.style.display = "none";
//   }
// }