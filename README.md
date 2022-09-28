# CoinMarketCap-Tracker
This is a demo app to track the prices and other data of various cryptocurrencies by scrapping it from the original website: "coinmarketcap.com" and displaying the live data with react front end and django backend.

The below screen shot represents the output for the first five scrapped values from the website coinmarketcap.com

 ![image](https://user-images.githubusercontent.com/50429258/192712137-3b4384e7-1548-416e-bcb4-8df848278c90.png)


NOTE: The values in the table are dynamic and are updated every 3 seconds.
 
Technologies used:

	Backend: Django Rest
  
	Frontend: React Js

How does the backend work?

The backend contains two apis:

1.	/scrap/put-data  - This api updates the database with the latest scrap results.

2.	/scrap/fetch-data  - This api is used to fetch the latest database values from the backend, and is mostly used at the frontend side.

3.	Scraping engine – This is used to scrap the required data, and  is supposed to run either as a background task or on a separate worker server. It runs continuously and scraps the data after every 5 seconds.

NOTE: In my demo app, it is running as a separate worker, and not as a background task, as running it as an asynchronous task would require a broker like Redis or RabbitMQ, which would be required if this app needs to be deployed, however for testing purpose on local host, the separate worker method serves its purpose well. 

How does the frontend work?

The front end makes use of only one api:  /scrap/fetch-data  

The frontend calls this api every 3 seconds, and use the fetch results by displaying them in a tabular format.
