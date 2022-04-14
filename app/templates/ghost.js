// Create a map object.
var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5
});

// Add a tile layer.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

//   // An array containing each city's name, location, and population
// var ghostFiles = $.getJSON("../../haunted_data/haunted.json", function(){
//     console.log("success");
// fetch("../../haunted_data/haunted.json")
//     .then(response => response.json())
//     .then(function (json) {
//         console.log(json)
//         for (var i = 0; i < json.length; i++) {
//             var city = json[i];
//             L.marker([city.latitude, city.longitude])
//                 .bindPopup(`${city.city}<hr><p>${city.description}</p>`)
//                 .addTo(myMap);
//         }
//     });

fetch("../../haunted_data/haunted.json")
    .then(response => response.json())
    .then(function (json) {
        var markers = L.markerClusterGroup();
        for (var i = 0; i < json.length; i++) {
            var sighting = json[i];
            // var location = ([city.latitude, city.longitude])
            if (sighting) {
                markers.addLayer(L.marker([sighting.latitude, sighting.longitude])
                    .bindPopup(sighting.location + "<br>" + sighting.city + ", " + sighting.state_abbrev + "<hr><p>" + sighting.description + "</p>"));
            }
        }
    myMap.addLayer(markers);
    });