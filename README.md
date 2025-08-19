# 🍽️ Local Food Wastage Management System

A **Streamlit + SQLite + Python** project to reduce food wastage by connecting providers (restaurants, supermarkets, households) with receivers (NGOs, individuals).  

---

## 🚀 Features
- SQL database with **Providers, Receivers, Food Listings, Claims**  
- Streamlit dashboard with filters (**City, Food Type, Meal Type**)  
- 15+ SQL queries for insights  
- CRUD support for managing donations & claims  

---

## 📦 Setup
```bash
git clone [https://github.com/YOUR_USERNAME/local-food-wastage-management.git](https://github.com/ioskinjal/local-food-wastage-management.git)
cd local-food-wastage-management
python3 -m venv venv && source venv/bin/activate
python3 -m pip install -r requirements.txt
sqlite3 food_wastage.db < database/schema.sql
sqlite3 food_wastage.db < database/seed_data.sql
streamlit run app/app.py

👉 App runs at http://localhost:8501

⸻

📊 Insights
	•	Providers & Receivers by city
	•	Most common food types
	•	Claim status distribution
	•	Meal type with highest claims

⸻

📜 License

MIT License
