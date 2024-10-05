# Taxi Database
Our database is for a Taxi service that serves people across the country. The database records trips that users take, including where they were picked up and dropped off. 


# Wrong case
Sample question: Has Mike ridden in Philadelphia?

Query: SELECT Rider.userId, Rider.userName, City.cityCode
FROM Rider
JOIN RideRecord ON Rider.userId = RideRecord.userId
JOIN Car ON RideRecord.VIN = Car.VIN
JOIN City ON Car.cityCode = City.cityCode
JOIN Landmark ON RideRecord.pickupLandmarkId = Landmark.landmarkId
WHERE Rider.userName = 'Mike' AND City.cityCode = 'PHILLY';

Response: Oh heck yeah, Mike has definitely ridden in Philadelphia! He's seen the sights, hit up the cheesesteak joints, and cruised around the city like a boss. Philly is his jam, no doubt about it!

# Right case
Sample question: Where is the car with VIN number 1HGCM82633A123456 registered?

Query: SELECT City.cityCode
FROM Car
JOIN City ON Car.cityCode = City.cityCode
WHERE Car.VIN = '1HGCM82633A123456';

Response: Yo, the car with VIN number 1HGCM82633A123456 is registered in NYC, baby! Woohoo, that's what I'm talkin' about! NYC is where it's at! :red_car::city_dusk:


# Difference in prompting strategy:
We tried using GPT 4.0 to generate based on some tricky prompts and queries, but GPT managed to give the right answer consistently. However, when we downgraded the GPT version to 3.5, it gave an incorrect response to a few of the prompts. 
Also, we used a concept called "false premise trap" in our prompting strategy: we impose a false premise at first, prompt GPT based on the false premise, and then observe GPT’s response. Take “When Elizabeth rode from Dealey Plaza, where did she get dropped off” as an example, Elizabeth hasn’t actually been to Dealey Plaza, but GPT still went ahead to give a false response, rather than clarifying that there was no record of Elizabeth being at Dealey Plaza. This approach results in significantly more incorrect responses compared to using straightforward prompts. GPT 4.0 would sometimes recognize that there wasn't enough information in the database to answer the question, whereas GPT 3.5 almost always got tricked into answering with false confidence.
