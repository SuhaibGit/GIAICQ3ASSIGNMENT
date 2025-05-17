import streamlit as st
st.title("Google-style Unit Converter")
category = st.selectbox("Choose a category:", ["Length","Mass","Area"])
if category == "Length":
    units = {
        "Metre": 1,
        "Centimetre": 100,
        "Millimetre": 1000,
        "Kilometre": 0.001,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Yard": 1.09361,
        "Mile": 0.000621371
    }
    input_value = st.number_input("Enter value:", value=1.0)
    from_unit = st.selectbox("From unit:", units.keys())
    to_unit = st.selectbox("To unit:", units.keys())
    result = input_value * (units[to_unit] / units[from_unit])
    st.write(f"### {input_value} {from_unit} = {result:.4f} {to_unit}")
    st.info(f"Formula: multiply by {units[to_unit] / units[from_unit]:.4f}")
elif category == "Area":
    units = {
        "Square meter": 1,
        "Square Kilometer": 1e-6,
        "Square mile": 3.861e-7,
        "Square yard": 1.19599,
        "Square foot": 10.7639,
        "Square inch": 1550,
        "Hectare": 1e-4,
        "Acre": 0.000247105
    }
    input_value = st.number_input("Enter value:", value=1.0)
    from_unit = st.selectbox("From unit:", units.keys())
    to_unit = st.selectbox("To unit:", units.keys())
    result = input_value * (units[to_unit] / units[from_unit])
    st.write(f"### {input_value} {from_unit} = {result:.4f} {to_unit}")
    st.info(f"Formula: multiply by {units[to_unit] / units[from_unit]:.4f}")
elif category == "Mass":
    units = {
    "Tonne": 1000,                  
    "Microgram": 1e-9,              
    "Milligram": 1e-6,              
    "Gram": 0.001,                  
    "Kilogram": 1,                  
    "US ton": 907.18474,            
    "Imperial ton": 1016.0469088,   
    "Stone": 6.35029318,           
    "Pound": 0.45359237,            
    "Ounce": 0.0283495231           
    }
    input_value = st.number_input("Enter value:", value=1.0)
    from_unit = st.selectbox("From unit:", units.keys())
    to_unit = st.selectbox("To unit:", units.keys())
    result = input_value * (units[to_unit] / units[from_unit])
    st.write(f"### {input_value} {from_unit} = {result:.4f} {to_unit}")
    st.info(f"Formula: multiply by {units[to_unit] / units[from_unit]:.4f}")