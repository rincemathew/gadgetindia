const searchFieldOne = document.querySelector("#searchFieldOne");
const searchFieldTwo = document.querySelector("#searchFieldTwo");
const searchFieldThree = document.querySelector("#searchFieldThree");
$('#idofOne').hide();

/* first section */

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
                        out += '<a href="javascript:fuctionOne(\'' + dataOne[i].mobileNames.brandName.brand_name_url + '\',\'' + dataOne[i].mobileNames.mobile_name_url + '\',\'' + dataOne[i].mobile_variants_url + '\');"> <table class="table-borderless" style="width:100%"><tr><td rowspan="2"><img class="img-fluid" style="max-height:75px" src="' + dataOne[i].mobileNames.mobile_image + '"></img></td><th>' + dataOne[i].mobileNames.brandName.brand_name + ' ' + dataOne[i].mobileNames.mobile_name + '</th><td rowspan="2">' + dataOne[i].mobileGeneral.price + '</td></tr><tr><td>' + dataOne[i].mobile_variants + '</td></tr></table></a>';
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

function fuctionOne(brandNameOne,mobileNameOne,variantNameOne) {
    console.log(brandNameOne,mobileNameOne,variantNameOne)
    document.getElementById("id01One").classList.add("hide");
    $('#idofOne').show();
    fetch('https://gadget-india.el.r.appspot.com/mobiles/mobile/?mobileNames__mobile_name_url='+ mobileNameOne + '&mobileNames__brandName__brand_name_url='+ brandNameOne + '&mobile_variants_url='+ variantNameOne + '')
            .then(res => res.json())
            .then((sentOne) => {
                console.log('Checkout this JSON! ', sentOne);
                var getOne = sentOne[0];
                console.log(getOne)
                document.getElementById("nameOne").innerHTML = getOne.mobileNames.brandName.brand_name + " " + getOne.mobileNames.mobile_name;
                document.getElementById("imageOne").innerHTML = '<img style="max-width: 250px;max-height: 250px;" class="img-fluid" src="'+ getOne.mobileNames.mobile_image +'" alt="mobile image">';
                document.getElementById("variantOne").innerHTML = getOne.mobile_variants;
                document.getElementById("priceOne").innerHTML = "Rs " + getOne.mobileGeneral.price;
                document.getElementById("brandOne").innerHTML = getOne.mobileNames.brandName.brand_name;
                document.getElementById("modelOne").innerHTML = getOne.mobileNames.mobile_name;
                document.getElementById("osOne").innerHTML = getOne.mobileGeneral.os;
                document.getElementById("osversionOne").innerHTML = getOne.mobileGeneral.os_version;
                if (getOne.mobileGeneral.UI_version == null) {
                    document.getElementById("uiversionOne").innerHTML = "";
                } else {
                    document.getElementById("uiversionOne").innerHTML = getOne.mobileGeneral.UI_version;
                }
                document.getElementById("releaseOne").innerHTML = getOne.mobileGeneral.release_date;
                document.getElementById("slotsOne").innerHTML = getOne.mobileGeneral.slots;
                document.getElementById("weightOne").innerHTML = getOne.mobileGeneral.weight + " g";
                document.getElementById("dimensionOne").innerHTML = getOne.mobileGeneral.dimensions;
                document.getElementById("ramOne").innerHTML = getOne.mobilePerformance.ram + " GB";
                document.getElementById("processorOne").innerHTML = getOne.mobilePerformance.processor;
                document.getElementById("processobuildOne").innerHTML = getOne.mobilePerformance.processor_company;
                if (getOne.mobilePerformance.clock_speed == null) {
                    document.getElementById("clockspeedOne").innerHTML = "";
                } else {
                    document.getElementById("clockspeedOne").innerHTML = getOne.mobilePerformance.clock_speed + " Hz";
                }
                document.getElementById("storageOne").innerHTML = getOne.mobileStorage.device_storage + " GB";
                if (getOne.mobileStorage.expandable_memory == true){
                    document.getElementById("expandablememoryOne").innerHTML = "Yes";
                }else{
                    document.getElementById("expandablememoryOne").innerHTML = "No";
                } 
                if (getOne.mobileStorage.expandable_memory_capacity == null) {
                    document.getElementById("expandablecapacityOne").innerHTML = "";
                } else {
                    document.getElementById("expandablecapacityOne").innerHTML = getOne.mobileStorage.expandable_memory_capacity + " GB";
                }
                if (getOne.mobileStorage.OTG_support == true) {
                    document.getElementById("otgOne").innerHTML = "Yes";
                } else {
                    document.getElementById("otgOne").innerHTML = "No";
                }
                document.getElementById("slottypeOne").innerHTML = getOne.mobileStorage.sim_slot_type;
                document.getElementById("primarycamOne").innerHTML = getOne.mobileCamera.primary_camera_str;
                if (getOne.mobileCamera.primary_camera_features == null) {
                    document.getElementById("primcamfetuOne").innerHTML = "";
                } else {
                    document.getElementById("primcamfetuOne").innerHTML = getOne.mobileCamera.primary_camera_features;
                }
                document.getElementById("seondaryCamOne").innerHTML = getOne.mobileCamera.secondary_camera_str;
                if (getOne.mobileCamera.secondary_camera_features == null) {
                    document.getElementById("secondarycamfeatuOne").innerHTML = "";
                } else {
                    document.getElementById("secondarycamfeatuOne").innerHTML = getOne.mobileCamera.secondary_camera_features;
                }
                document.getElementById("batterycapaOne").innerHTML = getOne.mobileBattery.battery_capacity + " mAh";
                document.getElementById("batterytypeOne").innerHTML = getOne.mobileBattery.battery_type;
                if (getOne.mobileBattery.fast_charger == true) {
                    document.getElementById("fastchargerOne").innerHTML = "Yes";
                } else {
                    document.getElementById("fastchargerOne").innerHTML = "No";
                }
                if (getOne.mobileBattery.fast_charging == null) {
                    document.getElementById("chargertypeOne").innerHTML = "";
                } else {
                    document.getElementById("chargertypeOne").innerHTML = getOne.mobileBattery.fast_charging;
                }
                if (getOne.mobileBattery.replaceable == true) {
                    document.getElementById("replacableOne").innerHTML = "Yes";
                } else {
                    document.getElementById("replacableOne").innerHTML = "No";
                }
                document.getElementById("screensizeOne").innerHTML = getOne.mobileDisplay.screen_size + " inch";
                document.getElementById("resolutionOne").innerHTML = getOne.mobileDisplay.resolution;
                if (getOne.mobileDisplay.resolution_type == null) {
                    document.getElementById("resolutiontypeOne").innerHTML = "";
                } else {
                    document.getElementById("resolutiontypeOne").innerHTML = getOne.mobileDisplay.resolution_type;
                }
                if (getOne.mobileDisplay.display_type == null) {
                    document.getElementById("displaytypeOne").innerHTML = "";
                } else {
                    document.getElementById("displaytypeOne").innerHTML = getOne.mobileDisplay.display_type;
                }
                if (getOne.mobileDisplay.GPU == null) {
                    document.getElementById("gpuOne").innerHTML = "";
                } else {
                    document.getElementById("gpuOne").innerHTML = getOne.mobileDisplay.GPU;
                }
                if (getOne.mobileDisplay.display_features == null) {
                    document.getElementById("screenOtherFetureOne").innerHTML = "";
                } else {
                    document.getElementById("screenOtherFetureOne").innerHTML = getOne.mobileDisplay.display_features;
                }
                if (getOne.mobileConnectivity.mobile_connectivity_details[0].five_g == true) {
                    document.getElementById("5gOne").innerHTML = "Yes";
                } else {
                    document.getElementById("5gOne").innerHTML = "No";
                }
                if (getOne.mobileConnectivity.mobile_connectivity_details[0].four_g == true) {
                    document.getElementById("4gOne").innerHTML = "Yes";
                } else {
                    document.getElementById("4gOne").innerHTML = "No";
                }
                if (getOne.mobileConnectivity.USB_type_c == true) {
                    document.getElementById("typecOne").innerHTML = "Yes";
                } else {
                    document.getElementById("typecOne").innerHTML = "No";
                }
                if (getOne.mobileConnectivity.GPS == true) {
                    document.getElementById("gpsOne").innerHTML = "Yes";
                } else {
                    document.getElementById("gpsOne").innerHTML = "No";
                }
                if (getOne.mobileConnectivity.SAR_value == null) {
                    document.getElementById("sarvalueOne").innerHTML = "";
                } else {
                    document.getElementById("sarvalueOne").innerHTML = getOne.mobileConnectivity.SAR_value;
                }
                if (getOne.mobileConnectivity.audio_jack == null) {
                    document.getElementById("audiojackOne").innerHTML = "";
                } else {
                    document.getElementById("audiojackOne").innerHTML = getOne.mobileConnectivity.audio_jack;
                }
                if (getOne.mobileConnectivity.bluetooth == null) {
                    document.getElementById("bluetoothOne").innerHTML = "";
                } else {
                    document.getElementById("bluetoothOne").innerHTML = getOne.mobileConnectivity.bluetooth;
                }
                if (getOne.mobileConnectivity.wi_fi == null) {
                    document.getElementById("wifiOne").innerHTML = "";
                } else {
                    document.getElementById("wifiOne").innerHTML = getOne.mobileConnectivity.wi_fi;
                }
                if (getOne.mobileSensor.fingerprint_sensor == true) {
                    document.getElementById("fingerprintsensorOne").innerHTML = "Yes";
                } else {
                    document.getElementById("fingerprintsensorOne").innerHTML = "No";
                }
                if (getOne.mobileSensor.fingerprint_position == null) {
                    document.getElementById("fingerprintpositionOne").innerHTML = "";
                } else {
                    document.getElementById("fingerprintpositionOne").innerHTML = getOne.mobileSensor.fingerprint_position;
                }
                if (getOne.mobileSensor.other_sensor == null) {
                    document.getElementById("othersensorsOne").innerHTML = "";
                } else {
                    document.getElementById("othersensorsOne").innerHTML = getOne.mobileSensor.other_sensor;
                }
                if (getOne.otherFeature.other_Feature == null) {
                    document.getElementById("otherfeaturesOne").innerHTML = "";
                } else {
                    document.getElementById("otherfeaturesOne").innerHTML = getOne.otherFeature.other_Feature;
                }      
                $('#idofOne').hide();      
            })
            .catch(err => { throw err });
}

/* second section */

searchFieldTwo.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;
    if (searchValue.trim().length > 0) {

        console.log(searchValue)
        fetch('https://gadgetin.in/mobiles/search/?search=' + searchValue)
            .then(res => res.json())
            .then((outTwo) => {
                console.log('Checkout this JSON! ', outTwo);
                var dataTwo = outTwo.results;
                console.log(dataTwo)
                var out = "";
                var i;
                for (i = 0; i < dataTwo.length; i++) {
                    if (i <= 10) {
                        out += '<a href="javascript:fuctionTwo(\'' + dataTwo[i].mobileNames.brandName.brand_name_url + '\',\'' + dataTwo[i].mobileNames.mobile_name_url + '\',\'' + dataTwo[i].mobile_variants_url + '\');"> <table class="table-borderless" style="width:100%"><tr><td rowspan="2"><img class="img-fluid" style="max-height:75px" src="' + dataTwo[i].mobileNames.mobile_image + '"></img></td><th>' + dataTwo[i].mobileNames.brandName.brand_name + ' ' + dataTwo[i].mobileNames.mobile_name + '</th><td rowspan="2">' + dataTwo[i].mobileGeneral.price + '</td></tr><tr><td>' + dataTwo[i].mobile_variants + '</td></tr></table></a>';
                    }
                }
                document.getElementById("id01Two").innerHTML = out;
            })
            .catch(err => { throw err });
    }
    else {
        console.log("nothing is there")
    }
});



$(document).click(function () {
    document.getElementById("id01Two").classList.add("hide");
  });
  $("#myDropdownTwo").click(function (e) {
    e.stopPropagation();
    document.getElementById("id01Two").classList.remove("hide");
  });

function fuctionTwo(brandNameTwo,mobileNameTwo,variantNameTwo) {
    console.log(brandNameTwo,mobileNameTwo,variantNameTwo)
    document.getElementById("id01Two").classList.add("hide");
    $('#idofOne').show();
    fetch('https://gadget-india.el.r.appspot.com/mobiles/mobile/?mobileNames__mobile_name_url='+ mobileNameTwo + '&mobileNames__brandName__brand_name_url='+ brandNameTwo + '&mobile_variants_url='+ variantNameTwo + '')
            .then(res => res.json())
            .then((sentTwo) => {
                console.log('Checkout this JSON! ', sentTwo);
                var getTwo = sentTwo[0];
                console.log(getTwo)
                document.getElementById("nameTwo").innerHTML = getTwo.mobileNames.brandName.brand_name + " " + getTwo.mobileNames.mobile_name;
                document.getElementById("imageTwo").innerHTML = '<img style="max-width: 250px;max-height: 250px;" class="img-fluid" src="'+ getTwo.mobileNames.mobile_image +'" alt="mobile image">';
                document.getElementById("variantTwo").innerHTML = getTwo.mobile_variants;
                document.getElementById("priceTwo").innerHTML = "Rs " + getTwo.mobileGeneral.price;
                document.getElementById("brandTwo").innerHTML = getTwo.mobileNames.brandName.brand_name;
                document.getElementById("modelTwo").innerHTML = getTwo.mobileNames.mobile_name;
                document.getElementById("osTwo").innerHTML = getTwo.mobileGeneral.os;
                document.getElementById("osversionTwo").innerHTML = getTwo.mobileGeneral.os_version;
                if (getTwo.mobileGeneral.UI_version == null) {
                    document.getElementById("uiversionTwo").innerHTML = "";
                } else {
                    document.getElementById("uiversionTwo").innerHTML = getTwo.mobileGeneral.UI_version;
                }
                document.getElementById("releaseTwo").innerHTML = getTwo.mobileGeneral.release_date;
                document.getElementById("slotsTwo").innerHTML = getTwo.mobileGeneral.slots;
                document.getElementById("weightTwo").innerHTML = getTwo.mobileGeneral.weight + " g";
                document.getElementById("dimensionTwo").innerHTML = getTwo.mobileGeneral.dimensions;
                document.getElementById("ramTwo").innerHTML = getTwo.mobilePerformance.ram + " GB";
                document.getElementById("processorTwo").innerHTML = getTwo.mobilePerformance.processor;
                document.getElementById("processobuildTwo").innerHTML = getTwo.mobilePerformance.processor_company;
                if (getTwo.mobilePerformance.clock_speed == null) {
                    document.getElementById("clockspeedTwo").innerHTML = "";
                } else {
                    document.getElementById("clockspeedTwo").innerHTML = getTwo.mobilePerformance.clock_speed + " Hz";
                }
                document.getElementById("storageTwo").innerHTML = getTwo.mobileStorage.device_storage + " GB";
                if (getTwo.mobileStorage.expandable_memory == true){
                    document.getElementById("expandablememoryTwo").innerHTML = "Yes";
                }else{
                    document.getElementById("expandablememoryTwo").innerHTML = "No";
                } 
                if (getTwo.mobileStorage.expandable_memory_capacity == null) {
                    document.getElementById("expandablecapacityTwo").innerHTML = "";
                } else {
                    document.getElementById("expandablecapacityTwo").innerHTML = getTwo.mobileStorage.expandable_memory_capacity + " GB";
                }
                if (getTwo.mobileStorage.OTG_support == true) {
                    document.getElementById("otgTwo").innerHTML = "Yes";
                } else {
                    document.getElementById("otgTwo").innerHTML = "No";
                }
                document.getElementById("slottypeTwo").innerHTML = getTwo.mobileStorage.sim_slot_type;
                document.getElementById("primarycamTwo").innerHTML = getTwo.mobileCamera.primary_camera_str;
                if (getTwo.mobileCamera.primary_camera_features == null) {
                    document.getElementById("primcamfetuTwo").innerHTML = "";
                } else {
                    document.getElementById("primcamfetuTwo").innerHTML = getTwo.mobileCamera.primary_camera_features;
                }
                document.getElementById("seondaryCamTwo").innerHTML = getTwo.mobileCamera.secondary_camera_str;
                if (getTwo.mobileCamera.secondary_camera_features == null) {
                    document.getElementById("secondarycamfeatuTwo").innerHTML = "";
                } else {
                    document.getElementById("secondarycamfeatuTwo").innerHTML = getTwo.mobileCamera.secondary_camera_features;
                }
                document.getElementById("batterycapaTwo").innerHTML = getTwo.mobileBattery.battery_capacity + " mAh";
                document.getElementById("batterytypeTwo").innerHTML = getTwo.mobileBattery.battery_type;
                if (getTwo.mobileBattery.fast_charger == true) {
                    document.getElementById("fastchargerTwo").innerHTML = "Yes";
                } else {
                    document.getElementById("fastchargerTwo").innerHTML = "No";
                }
                if (getTwo.mobileBattery.fast_charging == null) {
                    document.getElementById("chargertypeTwo").innerHTML = "";
                } else {
                    document.getElementById("chargertypeTwo").innerHTML = getTwo.mobileBattery.fast_charging;
                }
                if (getTwo.mobileBattery.replaceable == true) {
                    document.getElementById("replacableTwo").innerHTML = "Yes";
                } else {
                    document.getElementById("replacableTwo").innerHTML = "No";
                }
                document.getElementById("screensizeTwo").innerHTML = getTwo.mobileDisplay.screen_size + " inch";
                document.getElementById("resolutionTwo").innerHTML = getTwo.mobileDisplay.resolution;
                if (getTwo.mobileDisplay.resolution_type == null) {
                    document.getElementById("resolutiontypeTwo").innerHTML = "";
                } else {
                    document.getElementById("resolutiontypeTwo").innerHTML = getTwo.mobileDisplay.resolution_type;
                }
                if (getTwo.mobileDisplay.display_type == null) {
                    document.getElementById("displaytypeTwo").innerHTML = "";
                } else {
                    document.getElementById("displaytypeTwo").innerHTML = getTwo.mobileDisplay.display_type;
                }
                if (getTwo.mobileDisplay.GPU == null) {
                    document.getElementById("gpuTwo").innerHTML = "";
                } else {
                    document.getElementById("gpuTwo").innerHTML = getTwo.mobileDisplay.GPU;
                }
                if (getTwo.mobileDisplay.display_features == null) {
                    document.getElementById("screenOtherFetureTwo").innerHTML = "";
                } else {
                    document.getElementById("screenOtherFetureTwo").innerHTML = getTwo.mobileDisplay.display_features;
                }
                if (getTwo.mobileConnectivity.mobile_connectivity_details[0].five_g == true) {
                    document.getElementById("5gTwo").innerHTML = "Yes";
                } else {
                    document.getElementById("5gTwo").innerHTML = "No";
                }
                if (getTwo.mobileConnectivity.mobile_connectivity_details[0].four_g == true) {
                    document.getElementById("4gTwo").innerHTML = "Yes";
                } else {
                    document.getElementById("4gTwo").innerHTML = "No";
                }
                if (getTwo.mobileConnectivity.USB_type_c == true) {
                    document.getElementById("typecTwo").innerHTML = "Yes";
                } else {
                    document.getElementById("typecTwo").innerHTML = "No";
                }
                if (getTwo.mobileConnectivity.GPS == true) {
                    document.getElementById("gpsTwo").innerHTML = "Yes";
                } else {
                    document.getElementById("gpsTwo").innerHTML = "No";
                }
                if (getTwo.mobileConnectivity.SAR_value == null) {
                    document.getElementById("sarvalueTwo").innerHTML = "";
                } else {
                    document.getElementById("sarvalueTwo").innerHTML = getTwo.mobileConnectivity.SAR_value;
                }
                if (getTwo.mobileConnectivity.audio_jack == null) {
                    document.getElementById("audiojackTwo").innerHTML = "";
                } else {
                    document.getElementById("audiojackTwo").innerHTML = getTwo.mobileConnectivity.audio_jack;
                }
                if (getTwo.mobileConnectivity.bluetooth == null) {
                    document.getElementById("bluetoothTwo").innerHTML = "";
                } else {
                    document.getElementById("bluetoothTwo").innerHTML = getTwo.mobileConnectivity.bluetooth;
                }
                if (getTwo.mobileConnectivity.wi_fi == null) {
                    document.getElementById("wifiTwo").innerHTML = "";
                } else {
                    document.getElementById("wifiTwo").innerHTML = getTwo.mobileConnectivity.wi_fi;
                }
                if (getTwo.mobileSensor.fingerprint_sensor == true) {
                    document.getElementById("fingerprintsensorTwo").innerHTML = "Yes";
                } else {
                    document.getElementById("fingerprintsensorTwo").innerHTML = "No";
                }
                if (getTwo.mobileSensor.fingerprint_position == null) {
                    document.getElementById("fingerprintpositionTwo").innerHTML = "";
                } else {
                    document.getElementById("fingerprintpositionTwo").innerHTML = getTwo.mobileSensor.fingerprint_position;
                }
                if (getTwo.mobileSensor.other_sensor == null) {
                    document.getElementById("othersensorsTwo").innerHTML = "";
                } else {
                    document.getElementById("othersensorsTwo").innerHTML = getTwo.mobileSensor.other_sensor;
                }
                if (getTwo.otherFeature.other_Feature == null) {
                    document.getElementById("otherfeaturesTwo").innerHTML = "";
                } else {
                    document.getElementById("otherfeaturesTwo").innerHTML = getTwo.otherFeature.other_Feature;
                }      
                $('#idofOne').hide();      
            })
            .catch(err => { throw err });
}

/* third section */

searchFieldThree.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;
    if (searchValue.trim().length > 0) {
  
        console.log(searchValue)
        fetch('https://gadgetin.in/mobiles/search/?search=' + searchValue)
            .then(res => res.json())
            .then((outThree) => {
                console.log('Checkout this JSON! ', outThree);
                var dataThree = outThree.results;
                console.log(dataThree)
                var out = "";
                var i;
                for (i = 0; i < dataThree.length; i++) {
                    if (i <= 10) {
                        out += '<a href="javascript:fuctionThree(\'' + dataThree[i].mobileNames.brandName.brand_name_url + '\',\'' + dataThree[i].mobileNames.mobile_name_url + '\',\'' + dataThree[i].mobile_variants_url + '\');"> <table class="table-borderless" style="width:100%"><tr><td rowspan="2"><img class="img-fluid" style="max-height:75px" src="' + dataThree[i].mobileNames.mobile_image + '"></img></td><th>' + dataThree[i].mobileNames.brandName.brand_name + ' ' + dataThree[i].mobileNames.mobile_name + '</th><td rowspan="2">' + dataThree[i].mobileGeneral.price + '</td></tr><tr><td>' + dataThree[i].mobile_variants + '</td></tr></table></a>';
                    }
                }
                document.getElementById("id01Three").innerHTML = out;
            })
            .catch(err => { throw err });
    }
    else {
        console.log("nothing is there")
    }
  });
  
  
  
  $(document).click(function () {
    document.getElementById("id01Three").classList.add("hide");
  });
  $("#myDropdownThree").click(function (e) {
    e.stopPropagation();
    document.getElementById("id01Three").classList.remove("hide");
  });
  
  function fuctionThree(brandNameThree,mobileNameThree,variantNameThree) {
    console.log(brandNameThree,mobileNameThree,variantNameThree)
    document.getElementById("id01Three").classList.add("hide");
    $('#idofOne').show();
    fetch('https://gadget-india.el.r.appspot.com/mobiles/mobile/?mobileNames__mobile_name_url='+ mobileNameThree + '&mobileNames__brandName__brand_name_url='+ brandNameThree + '&mobile_variants_url='+ variantNameThree + '')
            .then(res => res.json())
            .then((sentThree) => {
                console.log('Checkout this JSON! ', sentThree);
                var getThree = sentThree[0];
                console.log(getThree)
                document.getElementById("nameThree").innerHTML = getThree.mobileNames.brandName.brand_name + " " + getThree.mobileNames.mobile_name;
                document.getElementById("imageThree").innerHTML = '<img style="max-width: 250px;max-height: 250px;" class="img-fluid" src="'+ getThree.mobileNames.mobile_image +'" alt="mobile image">';
                document.getElementById("variantThree").innerHTML = getThree.mobile_variants;
                document.getElementById("priceThree").innerHTML = "Rs " + getThree.mobileGeneral.price;
                document.getElementById("brandThree").innerHTML = getThree.mobileNames.brandName.brand_name;
                document.getElementById("modelThree").innerHTML = getThree.mobileNames.mobile_name;
                document.getElementById("osThree").innerHTML = getThree.mobileGeneral.os;
                document.getElementById("osversionThree").innerHTML = getThree.mobileGeneral.os_version;
                if (getThree.mobileGeneral.UI_version == null) {
                    document.getElementById("uiversionThree").innerHTML = "";
                } else {
                    document.getElementById("uiversionThree").innerHTML = getThree.mobileGeneral.UI_version;
                }
                document.getElementById("releaseThree").innerHTML = getThree.mobileGeneral.release_date;
                document.getElementById("slotsThree").innerHTML = getThree.mobileGeneral.slots;
                document.getElementById("weightThree").innerHTML = getThree.mobileGeneral.weight + " g";
                document.getElementById("dimensionThree").innerHTML = getThree.mobileGeneral.dimensions;
                document.getElementById("ramThree").innerHTML = getThree.mobilePerformance.ram + " GB";
                document.getElementById("processorThree").innerHTML = getThree.mobilePerformance.processor;
                document.getElementById("processobuildThree").innerHTML = getThree.mobilePerformance.processor_company;
                if (getThree.mobilePerformance.clock_speed == null) {
                    document.getElementById("clockspeedThree").innerHTML = "";
                } else {
                    document.getElementById("clockspeedThree").innerHTML = getThree.mobilePerformance.clock_speed + " Hz";
                }
                document.getElementById("storageThree").innerHTML = getThree.mobileStorage.device_storage + " GB";
                if (getThree.mobileStorage.expandable_memory == true){
                    document.getElementById("expandablememoryThree").innerHTML = "Yes";
                }else{
                    document.getElementById("expandablememoryThree").innerHTML = "No";
                } 
                if (getThree.mobileStorage.expandable_memory_capacity == null) {
                    document.getElementById("expandablecapacityThree").innerHTML = "";
                } else {
                    document.getElementById("expandablecapacityThree").innerHTML = getThree.mobileStorage.expandable_memory_capacity + " GB";
                }
                if (getThree.mobileStorage.OTG_support == true) {
                    document.getElementById("otgThree").innerHTML = "Yes";
                } else {
                    document.getElementById("otgThree").innerHTML = "No";
                }
                document.getElementById("slottypeThree").innerHTML = getThree.mobileStorage.sim_slot_type;
                document.getElementById("primarycamThree").innerHTML = getThree.mobileCamera.primary_camera_str;
                if (getThree.mobileCamera.primary_camera_features == null) {
                    document.getElementById("primcamfetuThree").innerHTML = "";
                } else {
                    document.getElementById("primcamfetuThree").innerHTML = getThree.mobileCamera.primary_camera_features;
                }
                document.getElementById("seondaryCamThree").innerHTML = getThree.mobileCamera.secondary_camera_str;
                if (getThree.mobileCamera.secondary_camera_features == null) {
                    document.getElementById("secondarycamfeatuThree").innerHTML = "";
                } else {
                    document.getElementById("secondarycamfeatuThree").innerHTML = getThree.mobileCamera.secondary_camera_features;
                }
                document.getElementById("batterycapaThree").innerHTML = getThree.mobileBattery.battery_capacity + " mAh";
                document.getElementById("batterytypeThree").innerHTML = getThree.mobileBattery.battery_type;
                if (getThree.mobileBattery.fast_charger == true) {
                    document.getElementById("fastchargerThree").innerHTML = "Yes";
                } else {
                    document.getElementById("fastchargerThree").innerHTML = "No";
                }
                if (getThree.mobileBattery.fast_charging == null) {
                    document.getElementById("chargertypeThree").innerHTML = "";
                } else {
                    document.getElementById("chargertypeThree").innerHTML = getThree.mobileBattery.fast_charging;
                }
                if (getThree.mobileBattery.replaceable == true) {
                    document.getElementById("replacableThree").innerHTML = "Yes";
                } else {
                    document.getElementById("replacableThree").innerHTML = "No";
                }
                document.getElementById("screensizeThree").innerHTML = getThree.mobileDisplay.screen_size + " inch";
                document.getElementById("resolutionThree").innerHTML = getThree.mobileDisplay.resolution;
                if (getThree.mobileDisplay.resolution_type == null) {
                    document.getElementById("resolutiontypeThree").innerHTML = "";
                } else {
                    document.getElementById("resolutiontypeThree").innerHTML = getThree.mobileDisplay.resolution_type;
                }
                if (getThree.mobileDisplay.display_type == null) {
                    document.getElementById("displaytypeThree").innerHTML = "";
                } else {
                    document.getElementById("displaytypeThree").innerHTML = getThree.mobileDisplay.display_type;
                }
                if (getThree.mobileDisplay.GPU == null) {
                    document.getElementById("gpuThree").innerHTML = "";
                } else {
                    document.getElementById("gpuThree").innerHTML = getThree.mobileDisplay.GPU;
                }
                if (getThree.mobileDisplay.display_features == null) {
                    document.getElementById("screenOtherFetureThree").innerHTML = "";
                } else {
                    document.getElementById("screenOtherFetureThree").innerHTML = getThree.mobileDisplay.display_features;
                }
                if (getThree.mobileConnectivity.mobile_connectivity_details[0].five_g == true) {
                    document.getElementById("5gThree").innerHTML = "Yes";
                } else {
                    document.getElementById("5gThree").innerHTML = "No";
                }
                if (getThree.mobileConnectivity.mobile_connectivity_details[0].four_g == true) {
                    document.getElementById("4gThree").innerHTML = "Yes";
                } else {
                    document.getElementById("4gThree").innerHTML = "No";
                }
                if (getThree.mobileConnectivity.USB_type_c == true) {
                    document.getElementById("typecThree").innerHTML = "Yes";
                } else {
                    document.getElementById("typecThree").innerHTML = "No";
                }
                if (getThree.mobileConnectivity.GPS == true) {
                    document.getElementById("gpsThree").innerHTML = "Yes";
                } else {
                    document.getElementById("gpsThree").innerHTML = "No";
                }
                if (getThree.mobileConnectivity.SAR_value == null) {
                    document.getElementById("sarvalueThree").innerHTML = "";
                } else {
                    document.getElementById("sarvalueThree").innerHTML = getThree.mobileConnectivity.SAR_value;
                }
                if (getThree.mobileConnectivity.audio_jack == null) {
                    document.getElementById("audiojackThree").innerHTML = "";
                } else {
                    document.getElementById("audiojackThree").innerHTML = getThree.mobileConnectivity.audio_jack;
                }
                if (getThree.mobileConnectivity.bluetooth == null) {
                    document.getElementById("bluetoothThree").innerHTML = "";
                } else {
                    document.getElementById("bluetoothThree").innerHTML = getThree.mobileConnectivity.bluetooth;
                }
                if (getThree.mobileConnectivity.wi_fi == null) {
                    document.getElementById("wifiThree").innerHTML = "";
                } else {
                    document.getElementById("wifiThree").innerHTML = getThree.mobileConnectivity.wi_fi;
                }
                if (getThree.mobileSensor.fingerprint_sensor == true) {
                    document.getElementById("fingerprintsensorThree").innerHTML = "Yes";
                } else {
                    document.getElementById("fingerprintsensorThree").innerHTML = "No";
                }
                if (getThree.mobileSensor.fingerprint_position == null) {
                    document.getElementById("fingerprintpositionThree").innerHTML = "";
                } else {
                    document.getElementById("fingerprintpositionThree").innerHTML = getThree.mobileSensor.fingerprint_position;
                }
                if (getThree.mobileSensor.other_sensor == null) {
                    document.getElementById("othersensorsThree").innerHTML = "";
                } else {
                    document.getElementById("othersensorsThree").innerHTML = getThree.mobileSensor.other_sensor;
                }
                if (getThree.otherFeature.other_Feature == null) {
                    document.getElementById("otherfeaturesThree").innerHTML = "";
                } else {
                    document.getElementById("otherfeaturesThree").innerHTML = getThree.otherFeature.other_Feature;
                }      
                $('#idofOne').hide();      
            })
            .catch(err => { throw err });
  }