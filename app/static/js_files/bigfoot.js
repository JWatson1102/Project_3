// Create a map object.
var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5
});

// Add a tile layer.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);


// fetch("../../bigfoot_data/bigfoot.json")
//     .then(response => response.json())
//     .then(function (json) {
//         console.log(json)
//         for (var i = 0; i < json.length; i++) {
//             var county = json[i];
//             L.marker([county.longitude, county.latitude])
//                 .bindPopup(`${county.county}<hr><p>${county.date}</p>`)
//                 .addTo(myMap);
//         }
//     });

fetch("/api/bigfoot_data")
    .then(response => response.json())
    .then(function (json) {
        var markers = L.markerClusterGroup();
        for (var i = 0; i < json.length; i++) {
            var sighting = json[i];
            // var location = ([city.latitude, city.longitude])
            if (sighting) {
                markers.addLayer(L.marker([sighting.latitude, sighting.longitude])
                    .bindPopup(sighting.county + ", " + sighting.state + "<hr><p>" + sighting.observed + "</p>"));
            }
        }
    myMap.addLayer(markers);
    });

