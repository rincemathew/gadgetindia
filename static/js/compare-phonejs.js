const searchFieldOne = document.querySelector("#searchFieldOne");

searchFieldOne.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;
    if (searchValue.trim().length > 0) {

        console.log(searchValue)
        fetch('https://gadgetin.in/mobiles/search/?search=' + searchValue)
            .then(res => res.json())
            .then((outOne) => {
                console.log('Checkout this JSON! ', outOne);
                var dataOne = outOne.results;
                console.log(dataOne)
                var out = "";
                var i;
                for (i = 0; i < dataOne.length; i++) {
                    if (i <= 10) {
                        out += '<a href="/' + dataOne[i].mobileNames.brandName.brand_name_url + '/' + dataOne[i].mobileNames.mobile_name_url + '/?variant=' + dataOne[i].mobile_variants_url + '"> <table class="table-borderless" style="width:100%"><tr><td rowspan="2"><img class="img-fluid" style="max-height:75px" src="' + dataOne[i].mobileNames.mobile_image + '"></img></td><th>' + dataOne[i].mobileNames.brandName.brand_name + ' ' + dataOne[i].mobileNames.mobile_name + '</th><td rowspan="2">' + dataOne[i].mobileGeneral.price + '</td></tr><tr><td>' + dataOne[i].mobile_variants + '</td></tr></table></a>';
                    }
                }
                document.getElementById("id01One").innerHTML = out;
            })
            .catch(err => { throw err });
    }
    else {
        console.log("nothing is there")
    }
});



$(document).click(function () {
    document.getElementById("id01One").classList.add("hide");
  });
  $("#myDropdownOne").click(function (e) {
    e.stopPropagation();
    document.getElementById("id01One").classList.remove("hide");
  });


/* second section */