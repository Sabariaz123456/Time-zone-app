# Import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# Apply custom CSS for styling (including background color)
st.markdown("""
    <style>
        /* Full Page Background Color */
        body {
            background-color: #E6E6FA; /* Light Purple */
        }
        
        /* Adjust Main Content Background */
        .stApp {
            background-color: #E6E6FA; /* Light Purple */
        }
        
        /* Center Title */
        h1 {
            color: #4B0082;
            text-align: center;
            font-size: 2.5rem;
        }

        /* Styling for Selected Timezone Display */
        .time-box {
            background: rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            font-size: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Create app title
st.title("🌎 Time Zone Converter")

# Create a multi-select dropdown for choosing time zones
selected_timezone = st.multiselect(
    "📍 Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
st.subheader("⏳ Selected Timezones")
for tz in selected_timezone:
    # Get and format current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display timezone and its current time inside a styled box
    st.markdown(f"""
        <div class="time-box">
            <strong>🕒 {tz}:</strong> {current_time}
        </div>
    """, unsafe_allow_html=True)

# Create section for time conversion
st.subheader("🔄 Convert Time Between Timezones")
# Create time input field with current time as default
current_time = st.time_input("⏰ Current Time", value=datetime.now().time())
# Dropdown to select source timezone
from_tz = st.selectbox("🌍 From Timezone", TIME_ZONES, index=0)
# Dropdown to select target timezone
to_tz = st.selectbox("🌍 To Timezone", TIME_ZONES, index=1)

# Create convert button and handle conversion
if st.button("🚀 Convert Time"):
    # Combine today's date with input time and source timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    # Convert time to target timezone and format it with AM/PM
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display the converted time with success message
    st.success(f"🎯 Converted Time in {to_tz}: {converted_time}")
