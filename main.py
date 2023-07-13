import streamlit as st
import plotly.express as px
from backend import get_data

import streamlit as st
st.markdown("<h1 style='text-align: center; color: red;font-size:50px'>WEATHERPY</h1>", unsafe_allow_html=True)
st.title("Weather Forecast for the Next Days🌡️☁️ ")

place = st.text_input(label="Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select the data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place} ")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images (1)/clear.png",
                      "Clouds": "images (1)/cloud.png",
                      "Rain": "images (1)/rain.png",
                      "Snow": "images (1)/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            print(sky_conditions)
            images_path = [images[condition] for condition in sky_conditions]
            print(images_path)
            st.image(images_path, width=115)
    except KeyError:
        st.info("This place does not exist.Please enter a valid name.")