/*
console.log('Hellow word!');
const marks = {
    student1 : "57",
    student2 : "76",
    student3 : "56",
    student4 : "89"
}
console.log(marks);
console.log(marks.student1);

var a = " a sentence string "
console.log(a +56);
console.log(typeof(a));

const a = 23
console.log(a +23);

const a = {
    conciousness: "chetna",
    famine: "akaall",
    forth: "aghe",
    unconciousness: "aachetna",   
    drink: "pina"
}
console.log(a);

const marks = 23
var a = (marks>40)? 'pass':'fail'
console.log(a);

const a = 13
console.log(a>10 && a<20);
if (a>10 && a<20){
    console.log("balik");
}
else {
    console.log("un-balik");
}

let a = 90
switch(a)
{
    case 0 :
        console.log('a is 0');
        break
    case 10 :
        console.log('a is 10');
        break
    case 20 :
        console.log('a is2 20');
        break
    case 30 :
        console.log('a is 30');
        break
    case 50 :
        console.log('a is 50');
        break
    case 70 :
        console.log('a is 70');
        break
    case 80 :
        console.log('a is 80');
        break
    case 90 :
        console.log('90');
        break
    default:
        console.log('a is less than 0, more than 90 or 90');
}

let a = prompt('enter a number:')
a = Number.parseInt(a)
if(a<30){
    console.log('30 se bhi chota hai!!');
}
else{
    console.log('30 se bda h');
}

let a = prompt('enter a number:')
a = Number.parseInt(a)
if(a%2==0 && a%3==0){
    console.log('divisible by 2 & 3');
}
else{
    console.log('not divisible by 2 & 3');
}

let a = prompt('enter a number:')
a = Number.parseInt(a)
if(a%2==0 || a%3==0){
    console.log('true');
}
else{
    console.log('false');
}

let a = prompt('enter ur age:\n')
a = Number.parseInt(a)
var b =(a>=18)? 'you can drive':'Your cannnot drive'
console.log(b)

for (let a=0; a<9;a++){
    console.log({a})
} 

let a = {
    k: "34",
    b: "23", 
    c: "232"
}
for (let x in a){
    console.log(x,a[x]);
}

let a = "oH mah Gaad";
for (k of a){
    console.log(k);
}

let a = prompt('enter a num');
a = Number.parseInt(a)
while (a<34){
    console.log(a);
    a+=1;
}

let a = prompt('enter a num');
a = Number.parseInt(a)
do{
    console.log(a);
    a+=1;
}while (a<34);

const a = (b,c)=>{
    console.log(b+c);
}
let d = a(34,34);
console.log(d)

const a = {
    b: 44,
    c: 34,
    d: 35
}
for (let k = 0; k < Object.keys(a).length; k++) {
    console.log(Object.keys(a)[k] + " " + a[Object.keys(a)[k]]);
}

let a = 23
let i=0
while(i!=a){
    i = prompt("enter a num");
    console.log("welcome");
}

const a=(b,c,d,e,f)=>{
    console.log((b+c+d+e+f)/5);
}
let i = a(2,3,4,5,6);
console.log(i)

let b= "wer";
let a = `hello ${b}`;
console.log(a);

console.log("her\"".length);

// console.log('hellow i\'m YOursd');
// console.log('hellow i\'m \rYOursd');

let a = "HWwer";
console.log(a.includes("hw"));
console.log(a.toLowerCase());
let b = a.replace("r", "O");
console.log(b);

let a = "Please give Rs 1000";
console.log(a.replace("Rs 1000", ""));

let a = [2,3,4,5,"four"];
for( let i =0;i<a.length;i++){
    console.log(a[i]);
}

let a = [];
let b = undefined
while (b!=0){
    b = prompt("enter a num");
    a.push(b);
    if(a.length==6){
        break
    }
}
console.log(a);

let a = [10,13,235,20]
let b = a.filter((c)=>{
    return c%10 == 0
})
console.log(b)
// function filteEr(a){
//     return a%10==0;
// }
// console.log(a.filter(filteEr));

let givenNum = [1,2,3,4,5];
const d =(value)=>{
    return value*value;
}
console.log(givenNum.map(d));

let k = [5,4,3,2,1];
function reducer(accumulator, currentValue, index) {
  const returns = accumulator * currentValue;
  console.log(
    `accumulator: ${accumulator}, currentValue: ${currentValue}, index: ${index}, returns: ${returns}`,
  );
  return returns;
}
console.log(k.reduce(reducer));

const again = (inp) => {
    if (inp < 18) {
        console.log(alert("YOU can't Drive"));
    }
    else if (inp != Number.parseInt(inp)) {
        console.log("enter a valid number")
        console.warn("enter a valid number")
    }
    else {
        console.log(alert("you can drive"));
    }
    if (inp<0){
        console.error("ENTER A POSITIVE INTEGAR");
    }
    // if (inp>4){
    //     location.href = "https://www.google.com/";
    // }
}
let inp = prompt("enter your age");
inp = Number.parseInt(inp)
console.log(again(inp));
let a = confirm("Do U want to change UR age?"); 
while(a==true){
   let inp = prompt('enter your age');
   console.log(again(inp));
   if (inp){
    a = confirm("Do U want to change UR age?"); 
    }

let k = prompt('enter the colour name if your want to change the colour of the website');
document.body.style.background = k
}*/
// document.getElementById("card-title").style.color = "red" 
// document.getElementsByTagName("nav")[0].firstChild.style.color = "red"

// document.getElementById("joId").classList.remove("hoke")
// let b = setInterval(() => {
//     alert("hello");
// }, 5000);
// let c = setTimeout(() => {
//     alert("jello")
// }, 2000);
// clearInterval(b)
// clearInterval(c)

// let l = document.getElementById('nese')
// l.onclick = function lk() {
//     alert('click')
// }
// let m = document.getElementById("arevent")
// document.getElementById("arevent").addEventListener('click', click)
// function click() {
//     m.innerHTML = "YOu clicked me"
// }
// document.getElementById('arevent').removeEventListener('click', click)

// document.getElementById("bookmark1").addEventListener('click',function() {
//     location = "https://www.google.com"
// })
// document.getElementById("bookmark2").addEventListener('click',function() {
//     location = "https://www.w3schools.com/jsref/met_document_removeeventlistener.asp"
// })

setInterval(() => {
    document.querySelector('#bulb').classList.toggle('bulb')
}, 500);

// let f = function va(first , callback) {
//     setTimeout(() => {
//         document.getElementById('ra').innerHTML = first
//         console.log('hey')
//         callback()
//     }, 3000);
// }
// function ra() {
//     let m = 'HEEY ITS first'
//     return m
// }
// function da() {
//     setTimeout(() => {
//         console.log('callback confirmed')
//     }, 1000);
// }
// f(ra(),da)

// function load(src,callback) {
//     let srcId = document.createElement('script')
//     srcId.src = src
//     srcId.onload = function () {
//         console.log(src)
//         callback(null,src)
//     }
//     srcId.onerror = function () {
//         console.log("error" + src)
//         callback(new Error("new error"))
//     }
//     document.body.appendChild(srcId)
// }
// function good(error,src) {
//     if(error){
//         console.log(error)
//         return
//     }
//     console.log('good\t' + src)
// }
// load("https://www.keybr.conm/", good);

// let pro = new Promise((resolve, reject) => {
//     console.log('pending...')
//     setTimeout(() => {
//         resolve(console.log('resolved'))
//         // reject(console.log('error'))
//     }, 2000);
//     reject(new Error('Error ni aaa ra tha toh banana pada ye error hi h'))
// })
// pro.then((value) => {
//     setTimeout(() => {
//         console.log(value + ' resolve confirmed!')
//     }, 1000)
// }).catch((error) => {
//     console.log(error)
// })

// let c1 = new Promise((resolve, reject)=> {
//     setTimeout(() => {
//         resolve(1)
//         console.log('hey1')
//     }, 1000);
// })
// let c2 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve(2)
//         console.log('hey2')
//     }, 2500);
// })
// let c3 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve(3)
//         console.log('hey3')
//     }, 5000);
// })
// Promise.all([c1, c2, c3]).then((values) => {
//   console.log(values);
// });
// Promise.allSettled([c1, c2, c3]).then((values) => {
//   console.log(values);
// });
// Promise.race([c1, c2, c3]).then((result) => {
//     console.log(result)
// });
// Promise.any([c1, c2, c3]).then((values) => {
//   console.log(values);
// });
// Promise.resolve([c1,c2,c3]).then((values) => {
//   console.log(values);
// });
// Promise.reject([c1, c2, c3]).then((values) => {
//   console.log(values);
// });

// let l1 = new Promise(async function(resolve, reject) {
//     setTimeout(() => {
//         resolve(1)
//         console.log('hey1')
//     }, 5000);
// })
// l1.then(() => {
//     console.log('done')
// })

// let awt = async function awai() {
//     let w1 = new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve(1)
//             console.log('hey1')
//         }, 1000);
//     })
//     let w2 = new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve(2)
//             console.log('hey2')
//         }, 2500);
//     })
//     let w3 = await w1
//     let w4 = await w2
//     console.log('fetching hey1 result....')
//     console.log('fetching hey2 result....')
//     setTimeout(() => {
//         console.log(w3,w4)
//     }, 3500);

// }

// try {
//     console.log(ds)
// } catch (error) { //catch handles all error it even handle's the new error except throw new error
//     // console.log(error.name)
//     // console.log(error.message)
//     // console.log(error.stack)
//     console.log(new Error('new error looks like this in catch'))
//     throw new Error('throw new error looks like this, its actual custom error in catch')
// }
// finally{
//     console.log('This was error objects and custom error btw this is a final clause. It runs irrespective of any other javascript code.')
// }
// let q = alert(new Error('new error looks like this out of catch'))
// console.log(q)
// throw new Error('throw new error looks like this, its error')

// const r = async (src) => {
//     return new Promise((resolve, reject) => {
//         let script = document.createElement('script')
//         script.src = src
//         script.onload = resolve(src)
//     })
// }
// const as = async () => {
//     let a = await r('https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js')
//     .then((value) => {
//         console.log(value)
//     })
// }
// as()
// const re = async ()=>{
//     let rw = await r('https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js')
//     console.log(rw)
// }
// re()

// const rjct = async function rt() {
//     return new Promise((resolve, reject) => {
//         console.log('pending...')
//         setTimeout(() => {
//             reject('rejected')
//         }, 3000)
//     })
// }
// const handl = async function han(){
//     try {
//         let awa = await rjct()
//         console.log(awa)
//     } catch (error) {
//         console.log('Rejected! error handled')
//     }
// }
// handl()

// let ro1 = async ()=>{
//     return new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve(2 + 'sec')
//     }, 2000);
// })}
// let ro2 = async ()=>{
//     return new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve(3 + 'sec')
//     }, 3000);
// })}
// let ro3 = async ()=>{
//     return new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve(4 + 'sec')
//     }, 4000);
// })}
// const roAl = async function () {
//     // console.time('roAl')
//     // let ry1 = await ro1()
//     // let ry2 = await ro2()
//     // let ry3 = await ro3()
//     // console.log([ry1,ry2,ry3])
//     // console.timeEnd('roAl')
//     console.time('roAl')
//     let ry1 = ro1()
//     let ry2 = ro2()
//     let ry3 = ro3()
//     let compare = await Promise.all([ry1,ry2,ry3])
//     console.log(compare)
//     console.timeEnd('roAl')
// }
// roAl()

// function promi() {
//     function roa() {
//         let roaSub = Math.floor(Math.random() * 10)
//         roaSub = Number.parseInt(roaSub)
//         if (roaSub > 5) {
//             return true
//         }
//         else {
//             return false
//         }
//     }
//     roa()
//     return new Promise((resolve, reject) => {
//         function promis(error) {
//             // const error = true
//             if (!error) {
//                 console.log('Hellow')
//                 resolve('fullfiled')
//             }
//             else {
//                 reject(console.error('Error occured'))
//             }
//         }
//         promis(roa)
//     })
// }
// promi().then((result) => {
//     console.log(result + '\nfullfillment confirmed \n')
// }).catch((error) => {
//     console.log('rejected')
// });

// async function load() {
//     return new Promise(async(resolve, reject) => {
//         let src = ('https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js')
//         let srclo = await src.onload
//         resolve(src)
//     })
// }
// load().then((vba) => console.log(vba)).then(alert('finished'))

// async function pro1() {
//     console.log('hey i want to come do you accept me?')
//     try {
//         let pr2=new Promise(async(resolve, reject) => {
//             setTimeout(() => {
//                 console.log('Nah')
//                 reject('REjected')
//             }, 3000);
//         })
//         return await pr2

//     } catch (error) {
//         console.log(error)
//     }
// }
// pro1()

// const fet = fetch('https://jsonplaceholder.typicode.com/todos/', {
//     method: 'POST',
//     headers: {
//         'Content-type': 'application/json'
//     },
//     body: {
//         "a": "Dj"
//     }
// }).then((result) => {
//     return result.json()
// }).then((value) => {
//     console.log(value)
// });

// 97363f19bb9f4741bab32606d5b89640
// https://newsapi.org/v2/top-headlines?country=in&apiKey=97363f19bb9f4741bab32606d5b89640

// function fet(url) {
//     fetch(url).then((res)=>{
//         return res.text();
// }).then((data)=>(console.log(data)))
// }
// fet('wwx.txt')
// function fet(url) {
//     fetch(url).then((res)=>{
//         return res.json();
// }).then((data)=>(console.log(data)))
// }
// fet('https://api.github.com/users')


// const p = fetch('https://goweather.herokuapp.com/weather/india')
// p.then((Response) => {
//     console.log(Response.status)
//     console.log(Response.ok)
//     return Response.json()
// }).then((data) => { console.log(data) })

// async function fe() {
//     let options = {
//         method: 'POST',
//         body: JSON.stringify({
//             title: 'deehj',
//             body: 'body',
//             userId: 7,
//         }),
//         headers: {
//             'Content-type': 'application/json; charset=UTF-8',
//         },
//     }
//     let resp = await fetch('https://jsonplaceholder.typicode.com/posts', options)
//     let teh = await resp.json()
//     return teh
// }
// async function get(id) {
//     let fe = await fetch('https://jsonplaceholder.typicode.com/posts/'+ id)
//     let feres = await fe.json()
//     console.log(feres)
// }
// async function was() {
//     let wai = await fe()
//     console.log(wai)
//     await get(5)
// }
// was()


// class complex {
//     constructor(real, imaginary) {
//         this.real = real
//         this.imaginary = imaginary
//     }
//     // f() {
//     //     console.log(`${this.real}+${this.imaginary}i`)
//     // }
//     addno(num) {
//         this.real = this.real  + num.real
//         this.imaginary = this.imaginary + num.imaginary
//         console.log(`${this.real}+${this.imaginary}i`)
//     }
//     get real(){
//         return this._real
//     }
//     get imaginary(){
//         return this._imaginary
//     }
//     set real(newreas){
//         this._real = newreas
//     }
//     set imaginary(newimag){
//         this._imaginary = newimag
//     }
// }
// let co = new complex(3, 5)
// co.real = 7
// co.imaginary = 4
// let lo = new complex(7, 5)
// co.addno(lo)
// console.log(co.real,co.imaginary)

// class human{
//     constructor(devlop,die){
//         this.devlop = devlop
//         this.die = die
//     }
//     hum(){
//         console.log(`${this.devlop} Human devlop \n ${this.die} Then Human die`)
//     }
// }
// class student extends human {
//     hum(){
//         console.log(`${this.devlop} students also devlop \n ${this.die} Then students also die`)
//     }
// }
// let studen = new student('spiecies of ','and after some time')
// console.log(studen.hum())
// console.log(studen instanceof human) 

// let ar = [2, 3, 4, 5, 6]
// let [a, b, ...rest] = ar
// console.log(a, b, rest)
// const c = async () => {
//     return new Promise((resolve) => {
//         setTimeout(() => {
//             console.log('hey G')
//             resolve(45)
//         }, 2000);
//     })
// }

// (async  () =>{
//     let d = await c()
//     console.log(d)
//     let e = await c()
//     console.log(e)
// })();

// function nme() {
//     let greet = 'hello'
//     let name = 'dj'
//     setTimeout(() => {
//         console.log(greet + ' ' + name)

//     }, 2000)
// };
// nme()

// let arr5 = [1,2,3,4,5]
// let [a, b,c,d,e] = arr5
// function ins() {
//     console.log((a+b+c+d+e)/arr5.length)
// }
// ins()

// function nNum(n) {
//     return new Promise((resolve) => {
//         setTimeout(() => {s
//             resolve(5)
//         }, n);
//     })
// }
// (async () => {
//         let n1 = await nNum(2000)
//         console.log(n1 + " first num of n (2000)")
//         let n2 = await nNum(3000)
//         console.log(n2 + " second num of n (3000)")
//         let n3 = await nNum(1000)
//         console.log(n3 + " third num of n (1000)")
//     }
// )()


// 
