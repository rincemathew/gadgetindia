/* topside.html */
const searchField = document.querySelector("#searchField");

searchField.addEventListener('keyup', (e) => {
  const searchValue = e.target.value;
  if (searchValue.trim().length > 0) {
    fetch('https://gadgetin.in/mobiles/search/?search='+searchValue)
      .then((res) => res.json())
      .then((dataqaz) => {
        console.log("comeon")
        console.log("data", data)
        var data = dataqaz.results;
        console.log(data)
        var out = "";
        var i;
        for (i = 0; i < data.length; i++) {
          if (i <= 10) {
            out += '<a href="/'+ data[i].mobileNames.brandName.brand_name_url + '/' + data[i].mobileNames.mobile_name_url + '/?variant=' + data[i].mobile_variants_url + '"> <table style="width:100%"><tr><td rowspan="2"><img class="img-fluid" style="max-height:50px" src="' + data[i].mobileNames.mobile_image + '"></img></td><th>' + data[i].mobileNames.brandName.brand_name + ' ' + data[i].mobileNames.mobile_name + '</th><td rowspan="2">' + data[i].mobileGeneral.price + '</td></tr><tr><td>' + data[i].mobile_variants + '</td></tr></table></a>';
          }
        }
        document.getElementById("id01").innerHTML = out;
      });
  }
});

$(document).click(function () {
  document.getElementById("id01").classList.add("hide");
});
$("#myDropdown").click(function (e) {
  e.stopPropagation();
  document.getElementById("id01").classList.remove("hide");
});
/* .html */

