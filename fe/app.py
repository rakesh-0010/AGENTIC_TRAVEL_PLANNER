import streamlit as st
import requests as r 

st.title("AI TRAVEL PLANNER")

st.subheader("enter all trip data")

starting_loc=st.text_input("Enter Strting Location")
destination_loc=st.text_input("Enter Destination Location")
no_of_trip_dys=st.number_input("Enter Trip Days")
no_of_people=st.number_input("Enter People Count")
budget=st.number_input("Enter budget",min_value=10000,max_value=100000,step=10000)
specifications=st.text_area("Enter yr specifications",placeholder="Example:-- party places, temples etc..")
btn=st.button("BuildTravellingPlan")

if btn:
    payload={
        "starting_loc":starting_loc,
        "destination_loc":destination_loc,
        "no_of_trip_dys":no_of_trip_dys,
        "no_of_people":no_of_people,
        "budget":budget,
        "specifications":specifications
    }
    be_res=r.post("http://127.0.0.1:8000/plan_trip",json=payload)
    if be_res.status_code == 200:
        st.write(be_res.json()["content"])
    # r.get()
    # r.put()
    # r.delete()

# pip install streamlit
# python -m pip install streamlit
# py -m pip install streamlit

# streamlit run app.py
# python -m streamlit run app.py
# py -m streamlit run app.py

# pip install requests
# python -m pip install requests
# py -m pip install requests