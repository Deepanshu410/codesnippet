let ting = new Audio('ting.mp3')
let turn = "X"
let isgameover = false

const changeTurn = () => {
    return turn === "X" ? "0" : "X"
}
const checkwin = () => {
    let boxtext = document.getElementsByClassName('boxtext')
    let win = [
        [0, 1, 2, 5, 6.2, 0],
        [3, 4, 5, 5, 19.2, 0],
        [6, 7, 8, 5, 32.2, 0],
        [0, 3, 6, -9, 19.5, 90],
        [1, 4, 7, 5, 19, 90],
        [2, 5, 8, 19, 19, 90],
        [0, 4, 8, 6, 20, 41],
        [2, 4, 6, 5, 20, 138]
    //     transform: translate(14vw, 17vw) rotate(138deg);
    // width: 32vw;
    // margin: -44px;
    ]
    win.forEach(e => {
        if ((boxtext[e[0]].innerText === boxtext[e[1]].innerText) && (boxtext[e[2]].innerText === boxtext[e[1]].innerText) && (boxtext[e[0]].innerText !== "")) {
            let turnInfo = document.querySelector('.turn');
            turnInfo.innerText = `${boxtext[e[0]].innerText} WIN!`;
            isgameover = true;
            document.querySelector('.winImg').style.width = '200px'
            document.querySelector(".line").style.transform = `translate(${e[3]}vw, ${e[4]}vw) rotate(${e[5]}deg)`
            document.querySelector(".line").style.width = "32vw";
            
        }
    });
}

let box = document.getElementsByClassName('box');
Array.from(box).forEach(element => {
    let boxtext = element.querySelector('.boxtext');
    element.addEventListener('click', () => {
        if (boxtext.innerText === '') {
            boxtext.innerText = turn
            turn = changeTurn()
            ting.play()
            checkwin()
            if (!isgameover) {
                let turnInfo = document.querySelector('.turn');
                turnInfo.innerText = `${turn} Turn`;
            }
        }
    })

});

let reset = document.getElementById('reset')
reset.addEventListener('click', () => {
    let boxtext = document.getElementsByClassName('boxtext')
    Array.from(boxtext).forEach(element => {
        element.innerText = ''
    });
    isgameover = false;
    turn = "X";
    document.querySelector('.winImg').style.width = '0vw'
    let turnInfo = document.querySelector('.turn');
    turnInfo.innerText = `${turn} Turn`;
    document.querySelector(".line").style.width = "0vw";
})