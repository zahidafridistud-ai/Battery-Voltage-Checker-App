import math
import streamlit as st

# ---------- Page setup ----------
st.set_page_config(page_title="Battery Voltage Checker", page_icon="🔋", layout="centered")

# ---------- Simple styling (responsive) ----------
st.markdown(
    """
    <style>
    .main-title {text-align: center; font-size: clamp(1.8rem, 6vw, 2.8rem); font-weight: 800; margin-bottom: 0;}
    .sub-title {text-align: center; color: #6b7280; margin-bottom: 1.5rem;}
    .result-box {border-radius: 14px; padding: 1.2rem; text-align: center; margin-top: 1rem; border: 2px solid;}
    .result-value {font-size: 1rem; margin-bottom: 0.3rem;}
    .result-status {font-size: clamp(1.8rem, 7vw, 2.6rem); font-weight: 800; margin: 0;}
    .result-message {font-size: 1.1rem; margin-top: 0.4rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Rules ----------
def get_condition(value):
    """Return (status, message, text color, background color)."""
    if value > 80:
        return "EXCELLENT", "Your battery condition is excellent!", "#146c2e", "#e6f6ea"
    elif value > 50:
        return "GOOD", "Your battery condition is good.", "#8a6d00", "#fff8db"
    else:
        return "BAD", "Your battery condition is bad. Please check or replace the battery.", "#a11a1a", "#fdeaea"

# ---------- Heading and input ----------
st.markdown('<p class="main-title">🔋 Battery Voltage Checker</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Enter the battery voltage or value below</p>', unsafe_allow_html=True)

user_text = st.text_input("Battery voltage or value", placeholder="Example: 75")
check = st.button("Check Battery", use_container_width=True)

# ---------- Show result only after the button is clicked ----------
if check:
    text = user_text.strip()

    if text == "":
        st.error("Please enter a value before clicking the button.")
    else:
        try:
            value = float(text)
        except ValueError:
            st.error("Invalid input. Please enter a number only, such as 75 or 62.5.")
        else:
            if not math.isfinite(value):
                st.error("Invalid input. Please enter a normal number.")
            elif value < 0:
                st.error("Invalid input. The value cannot be negative.")
            else:
                status, message, color, background = get_condition(value)
                st.markdown(
                    f"""
                    <div class="result-box" style="color:{color}; background:{background}; border-color:{color};">
                        <div class="result-value">Entered value: <b>{value:g}</b></div>
                        <p class="result-status">{status}</p>
                        <div class="result-message">{message}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

st.caption("Note: These rules treat the input as a score or percentage, not a real voltage in volts.")
