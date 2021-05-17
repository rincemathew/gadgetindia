/* topside.html */
const searchField = document.querySelector("#searchField");

searchField.addEventListener('keyup', (e) => {
  const searchValue = e.target.value;
  if (searchValue.trim().length > 0) {

    fetch("search_query", {
      body: JSON.stringify({ searchText: searchValue }),
      method: "POST"
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("comeon")
        console.log("data", data)
        var out = "";
        var i;
        for (i = 0; i < data.length; i++) {
          if (i <= 10) {
            out += '<a href="/'+ data[i].mobileNames__brandName__brand_name_url + '/' + data[i].mobileNames__mobile_name_url + '/?variant=' + data[i].mobile_variants_url + '"> <table style="width:100%"><tr><td rowspan="2"><img class="img-fluid" style="max-height:50px" src="https://storage.googleapis.com/gadget_india_bucket/' + data[i].mobileNames__mobile_image + '"></img></td><th>' + data[i].mobileNames__brandName__brand_name + ' ' + data[i].mobileNames__mobile_name + '</th><td rowspan="2">' + data[i].mobileGeneral__price + '</td></tr><tr><td>' + data[i].mobile_variants + '</td></tr></table></a>';
          }
        }
        document.getElementById("id01").innerHTML = out;
      });
  }
});

$(document).click(function () {
  document.getElementById("id01").classList.toggle("hide");
});
$("#myDropdown").click(function (e) {
  e.stopPropagation();
  document.getElementById("id01").classList.remove("hide");
});
/* .html */

