const geocode = require('./utils/geocode.js');
const forecast = require('./utils/forecast.js');
const city = process.argv[2];
if(!city){
    console.log('Kindly provide a city name');
}else{
const getGeocode = geocode(city,(err,{latitude,longitude,location}={})=>{ //err,data1  data1.latitude etc
   if(err){
        console.log(err);
   }else{
            console.log('Latitude:',latitude,'\nLongitude:',longitude);
            forecast(latitude,longitude,(err,{temperature,humidity,weather_descriptions}={})=>{
                if(err){
                    console.log(err);
                    //return console.log(err) no need to use else
                }else{
                    //console.log(data);
                    console.log('Location:',location);
                    console.log('Temperature:',temperature,'\nHumidity:',humidity,'\nWeather:',weather_descriptions[0]);
                }
            });
   }
});
}
