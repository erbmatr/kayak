# **🧭 Kayak smart trip recommender**
A data-driven prototype to inspire your next getaway.

### **Overview**
This project explores how data can enhance the travel experience by identifying the best places to visit in France, based on a combination of weather conditions and hotel quality.

Designed as a proof of concept for Kayak, the travel search platform, it aims to go beyond price comparisons helping users decide where to go, and when.

### **Why this project?**
Trip planning is exciting… but also overwhelming. Most people hesitate because they lack trusted, relevant, and personalized information.

To address this, I created a system that combines live weather forecasts and hotel reviews to dynamically highlight the most attractive destinations.

Whether you're chasing sunshine or charming cities, the goal is to answer one simple question:

Where should I go next weekend, and which hotel should I book?

### **How it works**
This smart recommender is built on a robust data pipeline that combines multiple components:

🔸 Weather data
→ Retrieved using OpenWeatherMap with geographic coordinates from Nominatim

🔸 Hotel data
→ Scraped directly from "booking.com", including names, locations, ratings, descriptions...

🔸 Data pipeline
→ Raw data stored in AWS S3, then processed and structured in a PostgreSQL database hosted on AWS RDS

🔸 Visualization
→ Interactive maps created with Plotly for intuitive and dynamic exploration

### **Smart recommendations**
The application analyzes and ranks destinations using weather metrics such as:

- Rainfall probability
- Temperature
- Humidity
- Wind
- Cloud

It then pairs those insights with top-rated hotels in each location, making it easy to identify the most appealing destinations and where to stay once you're there.

Focus area: France

The system was applied to a curated list of 35 iconic French cities, including: Paris, Lyon, Marseille, Colmar, Annecy, Biarritz, Eguisheim, Bormes-les-Mimosas, and many more.
This scope allowed for a diverse range of styles and regions from cultural capitals to coastal escapes while ensuring high data quality and personalization.

### **Preview**
Two interactive maps were designed as part of the project:

- 🏆 Top 5 destinations to travel in the next 7 days
- 🏨 Top 20 hotels across all destinations

These visualizations help users explore travel options intuitively and make decisions based on current conditions.
