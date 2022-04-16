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
fetch("/api/ufo_json")
    .then(response => response.json())
    .then(function (json) {
        var markers = L.markerClusterGroup();
        for (var i = 0; i < json.length; i++) {
            var sighting = json[i];
            if (sighting) {
                markers.addLayer(L.marker([sighting.Latitude, sighting.Longitude])
                    .bindPopup(sighting.City + ", " + sighting.State + "<hr><p>" + "Shape: " + sighting.Shape + "Duration: "+ sighting.Duration + "<hr></p><p>" + sighting.Description + "</p>"));
            }
        }
    myMap.addLayer(markers);
    });


//   // Looping through the cities array, create one marker for each city, bind a popup containing its name and population, and add it to the map.
//   for (var i = 0; i < cities.length; i++) {
//     var city = cities[i];
//     L.marker(city.location)
//       .bindPopup(`<h1>${city.name}</h1> <hr> <h3>Population ${city.population.toLocaleString()}</h3>`)
//       .addTo(myMap);
//   }