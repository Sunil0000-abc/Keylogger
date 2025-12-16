import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.set_page_config(page_title="Keylogger Detection", layout="centered")
st.title("🔐 Keylogger Detection System")
st.write("Enter network traffic details to predict if it is a keylogger attack.")

# Input fields
protocol = st.number_input("Protocol", min_value=0)
flow_duration = st.number_input("Flow Duration", min_value=0.0)
total_fwd_packets = st.number_input("Total Forward Packets", min_value=0)
total_bwd_packets = st.number_input("Total Backward Packets", min_value=0)
total_len_fwd = st.number_input("Total Length of Forward Packets", min_value=0.0)
total_len_bwd = st.number_input("Total Length of Backward Packets", min_value=0.0)
fwd_pkt_len_mean = st.number_input("Forward Packet Length Mean", min_value=0.0)
bwd_pkt_len_mean = st.number_input("Backward Packet Length Mean", min_value=0.0)
avg_pkt_size = st.number_input("Average Packet Size", min_value=0.0)
ack_flag_count = st.number_input("ACK Flag Count", min_value=0)

# Prediction button
if st.button("🔍 Predict"):
    input_data = np.array([[ 
        protocol,
        flow_duration,
        total_fwd_packets,
        total_bwd_packets,
        total_len_fwd,
        total_len_bwd,
        fwd_pkt_len_mean,
        bwd_pkt_len_mean,
        avg_pkt_size,
        ack_flag_count
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🚨 Keylogger Detected!")
    else:
        st.success("✅ Safe Traffic (No Keylogger Detected)")
