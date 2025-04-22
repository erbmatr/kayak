🧭 Kayak — Smart Trip Recommender

This project explores how real-time data can enhance travel recommendations by identifying the best destinations to visit in France, based on both weather conditions and hotel quality.

It was developed as a proof of concept for Kayak, the travel search platform, to help users choose not just how to travel — but where to go, and when.

Users often hesitate when planning trips: they want to make the right choice, and they want trusted, relevant information. By combining live weather forecasts and hotel reviews, I designed a system that dynamically highlights the most attractive cities to visit — at any given moment.

The project focused on 35 of the most iconic destinations in France, aiming to answer a simple but powerful question:
Where should I go next weekend, and which hotel should I book?

How it works :

To build this recommendation system, I combined several components:

- Weather data: Pulled using OpenWeatherMap and city coordinates from Nominatim
- Hotel data: Scraped directly from Booking.com (names, ratings, descriptions, and locations)
- Data pipeline: Raw data stored in AWS S3 and cleaned and structured into a PostgreSQL database hosted on AWS RDS
- Visualization tools: Interactive maps built with Plotly, allowing dynamic exploration of destinations and hotels

Smart Recommendations

The app surfaces:

Cities with the best weather forecast over the next 7 days (based on criteria like rainfall, temperature, humidity, etc.)

Top-rated hotels in those areas, filtered by user score and location

This allows users to easily identify where the weather will be nicest — and where the best places to stay are — in just a few clicks.

Focus: France’s Top 35 Cities
The recommendation engine was limited to a curated list of French cities — from Paris, Lyon, and Marseille to charming towns like Colmar, Eguisheim, or Bormes-les-Mimosas.

This made it possible to fine-tune the scoring and ensure data quality while offering a wide range of travel styles and regions.

Preview

Two interactive maps were created:

- Top 5 travel destinations for the coming week
- Top 20 hotels across all destinations


These help visualize patterns and offer an intuitive way to explore options.