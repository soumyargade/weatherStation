var weatherApp = angular.module('weatherApp', []);

weatherApp.controller('WeatherController', ($scope, $interval, $http, $q) => {
    const weather_api_uri='https://api.openweathermap.org/data/2.5/weather?';
    const api_key='c65e9b4872972150e9201b14b978f3f8';
    $scope.local_weather_set = false;

    $scope.get_feeling = () => {
        if ($scope.local_temp_f > 80.0) {
            $scope.local_feeling = "warm";
        } 
        if ($scope.local_temp_f <= 80.0) {
            $scope.local_feeling = "comfortable";
        } 
        if ($scope.local_temp_f > 75.0 && $scope.local_humidity >= 55.0) {
            $scope.local_feeling = "muggy";
        } 
        if ($scope.local_temp_f < 60.0) {
            $scope.local_feeling = "chilly";
        } 
        if ($scope.local_temp_f < 45.0) {
            $scope.local_feeling = "cold";
        }
    }


    // Get local zipcode
    $scope.get_auto_zip = () => {
        window.navigator.geolocation.getCurrentPosition(function(pos){
                geo_api = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+pos.coords.latitude+',';
                geo_api += pos.coords.longitude+'&sensor=true&key=AIzaSyB6U9bUUUVpIFCYIDuuS3v-fOsBGdFYS4Q';
                $http.get(geo_api).then(function(res){
                zipcode = res.data.results[0].address_components;
                zipcode = zipcode.filter(comp => comp.types[0] == "postal_code");
                zipcode = zipcode[0].long_name;
                console.log("zipcode: " + zipcode);
                $scope.zipcode = zipcode;
                $scope.get_local_data();
            });
        });
    }

    // Read from data.json
    var get_station_data = () => {
        $http.get('./data.json').then(response => {
            $scope.data = response.data;
            // Calculate station temp in celsius
            $scope.station_temp_c = ($scope.data.station_temp_f - 32) * 5 / 9;
            $scope.station_temp_c = $scope.station_temp_c.toFixed(2);
            $scope.station_humidity = $scope.data.station_humidity;
            $scope.station_feeling = $scope.data.station_feeling;
        })
        .catch(response => {
            console.log("Could not load data.json");
        });
    }

    $scope.get_local_data = (zipcode) => {
        var api_url = weather_api_uri + `zip=${$scope.zipcode},us&appid=${api_key}&units=imperial`;
        console.log("Sent! " + api_url);
        $http.get(api_url).then( response => {
            $scope.local_temp_f = response.data.main.temp;
            // Calculate local temp in celsius
            $scope.local_temp_c = ($scope.local_temp_f - 32) * 5 / 9;
            $scope.local_temp_c = $scope.local_temp_c.toFixed(2);
            $scope.local_humidity = response.data.main.humidity;
            $scope.local_weather_set = true;
            console.log(response.data);
            $scope.get_feeling();
        })
        .catch( response => {
            console.log("Couldn't contact weather api :( Status: " + response.status);
        });
    }

    // Get initial station data state
    get_station_data();
    // Every second reload station data
    $interval(function() {
        get_station_data();
        console.log("Reading from data.json...");
    }, 1000);

});
