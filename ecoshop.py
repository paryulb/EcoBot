import streamlit as st

# Sample product database (manually sourced from EcoShop India)
products = [
    {
        "name": "Neem Wood Round Toothbrush – Plant Based Bristles",
        "price": "₹129",
        "category": "Oral Care",
        "image": "https://dukaan.b-cdn.net/700x700/webp/upload_file_service/4c5b8c58-b627-42ea-9adf-7dd147f1efa5/neem1.webp",
        "description": "Eco-friendly toothbrush made from neem wood. Plant-based bristles for a sustainable oral care routine."
    },
    {
        "name": "Purifying & Acne Control Organic Face Wash (Neem & Tulsi, 100 ml)",
        "price": "₹695",
        "category": "Face Care",
        "image": "https://dukaan.b-cdn.net/2000x2000/webp/upload_file_service/b3d9f326-b2d1-41e7-9a6e-9f7bb4062192/1-98.avif",
        "description": "Gentle organic face wash with Neem and Tulsi. Controls acne and purifies skin."
    },
    {
        "name": "Hair Fall Control & Repair Organic Hair Oil (Sesame Oil & Methi, 100 ml)",
        "price": "₹795",
        "category": "Hair Care",
        "image": "https://dukaan.b-cdn.net/700x700/webp/upload_file_service/93fad89c-da10-4ebf-bc41-e30b1ffc5878/hair-oil-1.avif",
        "description": "Strengthen roots and reduce hair fall with this nourishing hair oil made from Methi and Sesame."
    }
]

# App layout
st.set_page_config(page_title="EcoBot - Your Eco Shopping Assistant", layout="centered")

st.markdown("""
    <style>
        .main { background-color: #f4fdf8; }
        .stButton>button {
            color: white;
            background-color: #36b27c;
            border-radius: 10px;
            padding: 0.7em 1.5em;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Welcome to EcoBot (Prototype)")
st.subheader("Discover your perfect eco-friendly products 🌍")

st.write("Let's personalize your sustainable lifestyle. Answer a few quick questions 💬")

# Quiz
skin_type = st.radio("1. What’s your skin type?", ["Oily", "Dry", "Sensitive", "Combination"])
preference = st.radio("2. What do you care about most?", ["Plastic-free items", "Acne control", "Hair nourishment"])
routine = st.radio("3. What’s part of your daily routine?", ["Eco-Brushing", "Face wash", "Hair oiling"])

# Recommendation logic
if st.button("🔍 Show My Recommendation"):
    st.subheader("🎯 Recommended for You")

    if "Plastic" in preference or "Eco-Brushing" in routine:
        rec = products[0]
    elif "Acne" in preference or "Face" in routine:
        rec = products[1]
    else:
        rec = products[2]

    st.image(rec["image"], width=250)
    st.markdown(f"**{rec['name']}**  \n💰 *{rec['price']}*  \n📦 *{rec['category']}*")
    st.write(rec["description"])
    st.markdown("[🛍️ View on EcoShop India](https://ecoshopindia.in/?srsltid=AfmBOopalHohF7hMk6sJBlaoaYsrvwX_L6dQwkXWHdp7wMwsEY5Mi5vV)", unsafe_allow_html=True)
    st.success("Going green never looked better 💚")

st.markdown("---")
st.caption("🚀 Built by EDC_Girlies | IIM Jammu")
