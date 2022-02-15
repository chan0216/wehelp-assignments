function showname() {
  let search_name = document.querySelector("#serch_name");
  fetch(`http://127.0.0.1:3000/api/members?username=${search_name.value}`)
    .then((response) => {
      return response.json();
    })
    .then((Jsondata) => {
      let namediv = document.querySelector(".namediv");
      let searchdiv = document.querySelector(".searchdiv");
      namediv.textContent =
        Jsondata["data"]["name"] + "(" + Jsondata["data"]["username"] + ")";
      searchdiv.appendChild(namediv);
    })
    .catch(function (error) {
      console.error("error", error);
    });
}
function updatename() {
  let change_name = document.querySelector("#change_name");
  fetch("http://127.0.0.1:3000/api/member", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name: change_name.value }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      if (data["ok"] == "true") {
        let newdiv = document.querySelector(".newdiv");
        newdiv.textContent = "更新成功";
        let renewdiv = document.querySelector(".renewdiv");
        renewdiv.appendChild(newdiv);
        let wel = document.querySelector("#wel");
        wel.textContent = `${change_name.value}，歡迎登入系統`;
      } else {
        alert("更新失敗，請重新登入");
      }
    })
    .catch(function (error) {
      console.error("error", error);
    });
}
