import streamlit as st
import queries

st.set_page_config(page_title="Food Wastage Management", layout="wide")

st.title("🍽️ Local Food Wastage Management System")

# --- Section 1: Providers ---
st.header("📍 Providers & Receivers")

df_city = queries.providers_and_receivers_by_city()
st.dataframe(df_city)

city_list = df_city["City"].unique().tolist()
selected_city = st.selectbox("🔎 Select City", ["All"] + city_list)

if selected_city != "All":
    st.subheader(f"Providers in {selected_city}")
    st.dataframe(queries.providers_contact_by_city(selected_city))
    st.subheader(f"Food Available in {selected_city}")
    st.dataframe(queries.food_by_city(selected_city))

# --- Section 2: Food Listings ---
st.header("🥗 Food Listings & Availability")

food_types = queries.most_common_food_types()
st.dataframe(food_types)

food_type_list = food_types["Food_Type"].tolist()
selected_food_type = st.selectbox("🍛 Select Food Type", ["All"] + food_type_list)

if selected_food_type != "All":
    st.subheader(f"Food Items of type: {selected_food_type}")
    st.dataframe(queries.food_by_type(selected_food_type))

# --- Section 3: Claims ---
st.header("📦 Claims & Distribution")

claim_dist = queries.claim_status_distribution()
st.dataframe(claim_dist)
st.bar_chart(claim_dist.set_index("Status"))

meal_types = queries.most_claimed_meal_type()
st.dataframe(meal_types)

meal_type_list = meal_types["Meal_Type"].tolist()
selected_meal = st.selectbox("🍴 Select Meal Type", ["All"] + meal_type_list)

if selected_meal != "All":
    st.subheader(f"Claims for {selected_meal}")
    st.dataframe(queries.claims_by_meal_type(selected_meal))