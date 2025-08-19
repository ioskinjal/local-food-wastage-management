import pandas as pd
from db import get_connection

# ---------- Food Providers & Receivers ----------

def providers_and_receivers_by_city():
    conn = get_connection()
    query = """
    SELECT City, 
           COUNT(DISTINCT Provider_ID) AS Total_Providers,
           (SELECT COUNT(DISTINCT Receiver_ID) 
            FROM receivers r 
            WHERE r.City = p.City) AS Total_Receivers
    FROM providers p
    GROUP BY City;
    """
    return pd.read_sql(query, conn)

def top_provider_type():
    conn = get_connection()
    query = """
    SELECT Type, COUNT(*) AS Total_Providers
    FROM providers
    GROUP BY Type
    ORDER BY Total_Providers DESC;
    """
    return pd.read_sql(query, conn)

def providers_contact_by_city(city):
    conn = get_connection()
    query = "SELECT Name, Contact, Type, Address FROM providers WHERE City = ?;"
    return pd.read_sql(query, conn, params=(city,))

def top_receivers():
    conn = get_connection()
    query = """
    SELECT r.Name, COUNT(c.Claim_ID) AS Total_Claims
    FROM claims c
    JOIN receivers r ON c.Receiver_ID = r.Receiver_ID
    GROUP BY r.Name
    ORDER BY Total_Claims DESC;
    """
    return pd.read_sql(query, conn)

# ---------- Food Listings & Availability ----------

def total_food_quantity():
    conn = get_connection()
    query = "SELECT SUM(Quantity) AS Total_Quantity FROM food_listings;"
    return pd.read_sql(query, conn)

def city_with_most_food():
    conn = get_connection()
    query = """
    SELECT Location, COUNT(Food_ID) AS Total_Food_Items
    FROM food_listings
    GROUP BY Location
    ORDER BY Total_Food_Items DESC;
    """
    return pd.read_sql(query, conn)

def most_common_food_types():
    conn = get_connection()
    query = """
    SELECT Food_Type, COUNT(*) AS Count
    FROM food_listings
    GROUP BY Food_Type
    ORDER BY Count DESC;
    """
    return pd.read_sql(query, conn)

def food_by_type(food_type):
    conn = get_connection()
    query = "SELECT * FROM food_listings WHERE Food_Type = ?;"
    return pd.read_sql(query, conn, params=(food_type,))

def food_by_city(city):
    conn = get_connection()
    query = "SELECT * FROM food_listings WHERE Location = ?;"
    return pd.read_sql(query, conn, params=(city,))

# ---------- Claims & Distribution ----------

def claims_per_food_item():
    conn = get_connection()
    query = """
    SELECT f.Food_Name, COUNT(c.Claim_ID) AS Total_Claims
    FROM claims c
    JOIN food_listings f ON c.Food_ID = f.Food_ID
    GROUP BY f.Food_Name;
    """
    return pd.read_sql(query, conn)

def provider_with_most_successful_claims():
    conn = get_connection()
    query = """
    SELECT p.Name, COUNT(c.Claim_ID) AS Successful_Claims
    FROM claims c
    JOIN food_listings f ON c.Food_ID = f.Food_ID
    JOIN providers p ON f.Provider_ID = p.Provider_ID
    WHERE c.Status = 'Completed'
    GROUP BY p.Name
    ORDER BY Successful_Claims DESC;
    """
    return pd.read_sql(query, conn)

def claim_status_distribution():
    conn = get_connection()
    query = """
    SELECT Status, 
           COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims) AS Percentage
    FROM claims
    GROUP BY Status;
    """
    return pd.read_sql(query, conn)

def claims_by_meal_type(meal_type):
    conn = get_connection()
    query = """
    SELECT f.Meal_Type, f.Food_Name, COUNT(c.Claim_ID) AS Total_Claims
    FROM claims c
    JOIN food_listings f ON c.Food_ID = f.Food_ID
    WHERE f.Meal_Type = ?
    GROUP BY f.Food_Name;
    """
    return pd.read_sql(query, conn, params=(meal_type,))

# ---------- Analysis & Insights ----------

def avg_quantity_claimed_per_receiver():
    conn = get_connection()
    query = """
    SELECT r.Name, AVG(f.Quantity) AS Avg_Quantity_Claimed
    FROM claims c
    JOIN receivers r ON c.Receiver_ID = r.Receiver_ID
    JOIN food_listings f ON c.Food_ID = f.Food_ID
    GROUP BY r.Name;
    """
    return pd.read_sql(query, conn)

def most_claimed_meal_type():
    conn = get_connection()
    query = """
    SELECT Meal_Type, COUNT(c.Claim_ID) AS Total_Claims
    FROM claims c
    JOIN food_listings f ON c.Food_ID = f.Food_ID
    GROUP BY Meal_Type
    ORDER BY Total_Claims DESC;
    """
    return pd.read_sql(query, conn)

def total_quantity_per_provider():
    conn = get_connection()
    query = """
    SELECT p.Name, SUM(f.Quantity) AS Total_Donated
    FROM food_listings f
    JOIN providers p ON f.Provider_ID = p.Provider_ID
    GROUP BY p.Name
    ORDER BY Total_Donated DESC;
    """
    return pd.read_sql(query, conn)