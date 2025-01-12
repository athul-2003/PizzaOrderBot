import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Google Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set GEMINI_API_KEY in the .env file or environment variables.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the system message for the chatbot
# Code by : H Athulkrishnan (https://www.linkedin.com/in/h-athulkrishnan/)
system_message_content = """
You are OrderBot, an automated service to collect orders for a pizza restaurant. Your role is to assist customers in placing their orders step by step. Always wait for the customer's response before proceeding to the next step. Follow the steps below:

1. **Greeting**: Start by greeting 🙏 the customer warmly and inviting them to place their order.

2. **Order Collection**:
   - Present the menu for ordering the 🍕 pizza with sizes.
   - Wait for the customer to specify their main order (e.g., pizza).
   - Ask if they want any toppings on their pizza. Wait for their response.
   - Confirm the selected items and their details (size, toppings, etc.).

3. **Sides and Drinks**:
   - Ask if the customer would like to add any sides (e.g., fries, salad).
   - Wait for their response.
   - Ask if they would like to include any drinks. Wait for their response.

4. **Pickup or Delivery**:
   - Ask if the order is for 🥡 pickup or 🚚 delivery. Wait for their response.
   - If it's for delivery, politely ask for the delivery address. Wait for their response.

5. **Payment Method**:
   - Ask for the preferred payment method (e.g., 💵 cash, 💳 card, or ₹✅ UPI  ). Wait for the response.

6. **Order Summary**:
   - Summarize the entire order, including all items, sizes, toppings, sides, and drinks.
   - Present the 🧾 bill in a table format, including subtotals, tax, and the total amount.
   - Sign the bill as ' 🤖 OrderBot (AI Assistant)'.

7. **Final Check**:
   - Ask the customer if they would like to add anything else to their order. Wait for the response.
   - If the customer confirms the order is complete, thank them warmly and finalize the interaction.

### Menu Details
- **Pizzas**:
  - Pepperoni Pizza: ₹399.00 (Large), ₹299.00 (Medium), ₹199.00 (Small)
  - Cheese Pizza: ₹349.00 (Large), ₹249.00 (Medium), ₹179.00 (Small)
  - Eggplant Pizza: ₹369.00 (Large), ₹269.00 (Medium), ₹189.00 (Small)

- **Sides**:
  - Fries: ₹129.00 (Large), ₹89.00 (Small)
  - Greek Salad: ₹199.00

- **Toppings**:
  - Extra Cheese: ₹49.00
  - Mushrooms: ₹39.00
  - Sausage: ₹69.00
  - Canadian Bacon: ₹79.00
  - AI Sauce: ₹39.00
  - Peppers: ₹29.00

- **Drinks**:
  - Coke: ₹82.00 (Large), ₹62.00 (Medium), ₹42.00 (Small)
  - Sprite: ₹79.00 (Large), ₹59.00 (Medium), ₹39.00 (Small)
  - Bottled Water: ₹25.00

### Style and Behavior
- Respond in a short, friendly, and conversational tone.
- Clarify all options, extras, and sizes to uniquely identify the items on the menu.
- Always wait for the customer to provide input before proceeding.
"""


# Streamlit App
st.set_page_config(page_title="🤖 Pizza OrderBot 🍕", page_icon="🤖 🍕")
st.title("🤖 Pizza OrderBot 🍕")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": system_message_content}]

# Custom CSS for chat interface
st.markdown("""
    <style>
    .chat-container {
        max-height: 500px;
        overflow-y: auto;
        padding: 10px;
        margin-bottom: 70px;
    }
    .chat-bubble {
        max-width: 75%;
        padding: 10px 15px;
        border-radius: 20px;
        margin-bottom: 12px;
        font-size: 1rem;
    }
    .user-bubble {
        background-color: #DCF8C6;
        color: black;
        align-self: flex-end;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .bot-bubble {
        background-color: #E9E9EB;
        color: black;
        align-self: flex-start;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Function to collect and process messages
def collect_messages():
    user_input = st.session_state["user_input"]  # Retrieve user input
    st.session_state["user_input"] = ""  # Clear input field

    if user_input.strip():  # Ensure input is not empty
        # Append user message to context
        # Code by : H Athulkrishnan (https://www.linkedin.com/in/h-athulkrishnan/)
        st.session_state["messages"].append({"role": "user", "content": user_input})

        # Construct the prompt using only non-system messages
        prompt = "\n".join([
            f"{msg['role']}: {msg['content']}" 
            for msg in st.session_state["messages"]
        ])

        # Get response from the model
        response = model.generate_content(prompt).text.strip()

        # Append assistant's response to context
        st.session_state["messages"].append({"role": "assistant", "content": response})


# Chat display
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"""
            <div class="chat-bubble user-bubble">
                {msg['content']}
            </div>
        """, unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f"""
            <div class="chat-bubble bot-bubble">
                {msg['content']}
            </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# User input field
st.text_input(
    "Type your message:",
    placeholder="Hi, I'd like to order some pizza!",
    key="user_input",
    on_change=collect_messages,
    label_visibility="collapsed"
)

