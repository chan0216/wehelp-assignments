let req = new XMLHttpRequest();
req.open(
  "GET",
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
);

req.onload = function () {
  let data = JSON.parse(this.responseText);
  let result = data.result.results;

  myfunction(result);
};
req.send();

let container = document.querySelector(".container");
function myfunction(result) {
  for (let i = 0; i < 8; i++) {
    let title = result[i].stitle;
    let url = "http" + result[i].file.split("http")[1];
    let div = document.createElement("div");
    div.className = "div";
    document.body.appendChild(div);
    let img = document.createElement("img");
    let p = document.createElement("p");
    p.textContent = title;
    img.src = url;
    div.appendChild(img);
    div.appendChild(p);
    let container = document.querySelector(".container");
    container.appendChild(div);
  }
  let btn = document.getElementById("btn");
  let counter = 8;
  let n = 8;
  btn.addEventListener("click", function () {
    for (let i = counter; i < counter + n; i++) {
      let title = result[i].stitle;
      let url = "http" + result[i].file.split("http")[1];
      let div = document.createElement("div");
      div.className = "div";
      document.body.appendChild(div);
      let img = document.createElement("img");
      let p = document.createElement("p");
      p.textContent = title;
      img.src = url;
      div.appendChild(img);
      div.appendChild(p);
      let container = document.querySelector(".container");
      container.appendChild(div);
    }
    counter += 8;
    if (counter > 55) {
      n = 2;
    }
    if (counter == 64) {
      btn.disabled = true;
    }
  });
}
