import streamlit as st

import databutton as db


@db.apps.streamlit(route="/hello", name="Hello Databutton")
def hello():
    st.title("Hello, Databutton!")
    st.write("Tyler's First Edit")
    st.write("The rest of the streamlit app goes here")


@db.jobs.repeat_every(seconds=10 * 60)
def repeating_job():
    # Check for new data
    # Do some work on that data
    # Write that data to db.dataframes
    # Send slack notification
    print("Success!")
