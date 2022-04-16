// Create a map object.
var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5
});

// Add a tile layer.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

// An array containing each city's name, location, and population
fetch("/api/ufo_json")
    .then(response => response.json())
    .then(function (json) {
        var markers = L.markerClusterGroup();
        for (var i = 0; i < json.length; i++) {
            var sighting = json[i];
            if (sighting) {
                // console.log(sighting);
                markers.addLayer(L.marker([sighting.Latitude, sighting.Longitude])
                    .bindPopup(sighting.City + ", " + sighting.State + "<hr><p>" + "Shape: " + sighting.Shape + "<br>" + "Duration: "+ sighting.Duration + "<hr></p><p>" + sighting.Description + "</p>"));
            }
        }
    myMap.addLayer(markers);
    });


