# 🌦️ Weather App

A Python-based desktop weather application using **Tkinter**, **OpenWeatherMap API**, and **GeoPy** to fetch and display real-time weather information based on user-entered city names.

---

## ✨ Features

- 🌍 Real-time weather updates by city name  
- 🕒 Automatically shows local time based on timezone  
- 🌡️ Displays temperature, weather condition, pressure, humidity, wind speed  
- 🎨 Clean and modern UI with images and labels  
- 🔒 Uses `.env` file to securely store the API key

---

## 🛠️ Tech Stack

- **Python 3**
- **Tkinter** (for GUI)
- **GeoPy** (to get coordinates)
- **TimezoneFinder** (for timezone)
- **OpenWeatherMap API** (for weather data)
- **python-dotenv** (to load API key securely)

---

## 📦 Installation

1. **Clone the repo**
```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
Create and activate a virtual environment

bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file in the root directory and add your API key:

ini
Copy
Edit
OMW_API_KEY=your_openweathermap_api_key_here
Run the app

bash
Copy
Edit
python Weather.py
📂 Project Structure
bash
Copy
Edit
weather-app/
│
├── Weather.py              # Main application script
├── .env                    # Hidden file storing API key
├── requirements.txt        # Python dependencies
├── search.png              # Search bar background image
├── search_icon.png         # Search button icon
├── logo.png                # App logo
├── box.png                 # Bottom box image
└── README.md               # You're here!
📄 Requirements
Install dependencies using pip:

bash
Copy
Edit
pip install geopy timezonefinder pytz requests python-dotenv
Or save them in a requirements.txt:

nginx
Copy
Edit
geopy
timezonefinder
pytz
requests
python-dotenv
🤝 Contributions
Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

📜 License
MIT License © 2025 Imani Dinkins
