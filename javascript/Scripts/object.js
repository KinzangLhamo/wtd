let cat = {name:"lucy", color: "golden brown", age:3 };

let dog = new Object();
dog.breed = "husky";
dog.name = "jacky"
dog.isVaccinatedm = true;

document.getElementById("paral").innerHTML = "breed: " + dog.breed + "<br>name: " + dog["name"] + "<br>isvaccinated: "+ dog.isVaccinatedm; 

delete dog.isvaccinated;
console.log(dog);

dog.age = 5;
console.log(dog);

const person = {
    fname: "Yuthra",
    lname: "Chotshok",
    age: 9,
    fullname: function() {
        return this.fname + " " + this.lname
    } 


};
console.log(person);


document.getElementById("paral").innerHTML = person.fullname();


let x = 5;
let y = 8;

document.getElementById("paral").innerHTML =x ** y;

