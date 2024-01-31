const country = "Italy"; //# Add country name
const visits = 7; //# Number of visits
const list_of_cities = ["Venice", "Rome", "Florence"]; //# create list from formatted string
let travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
];
// # Your code here 👇
function add_new_country(name, times_visited, cities_visited) {
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.push(new_country)
};

add_new_country(country, visits, list_of_cities);
console.log("I've been to " + travel_log[2]['country'] + " " + travel_log[2]['visits'] + " times.");
console.log("My favourite city was " + travel_log[2]['cities'][0] + ".");