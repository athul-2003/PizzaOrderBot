# 🤖 Pizza OrderBot 🍕

Welcome to the **Pizza OrderBot** project! This chatbot uses the **Google Gemini API** and **Streamlit** to create an interactive and fun pizza ordering experience. The chatbot guides customers through placing an order for pizza, including selecting toppings, sides, drinks, and payment methods. It generates an order summary and bill at the end, just like a real pizza ordering system!

## 🌟 Features

- **Order Pizza**: Customers can select pizza sizes, toppings, sides, and drinks.
- **Interactive Flow**: The bot interacts with the user step-by-step to ensure an enjoyable experience.
- **Customizable Menu**: The menu includes options like Pepperoni, Cheese, Eggplant Pizzas, Fries, and Drinks.
- **Order Summary**: The bot generates a summary of the order, including subtotals and total cost.
- **Interactive GUI**: Built using **Streamlit** to make the chatbot more engaging and user-friendly.

## 🎓 Demo Video

Check out the demo video of the Pizza OrderBot in action!  

[**Watch Demo Video**](https://github.com/user-attachments/assets/daa610e0-6e9a-4864-a68b-647c0eb38120)

## 🚀 Getting Started

### Prerequisites

To run this project locally, you'll need:

- Python 3.8+
- A **Google Gemini API** key (instructions below on how to get it).
- Streamlit installed for the interactive frontend.

### Steps to Run the Project

1. **Clone the repository**:

    ```bash
    git clone https://github.com/athul-2003/PizzaOrderBot.git
    cd PizzaOrderBot
    ```

2. **Install dependencies**:

    Install the required Python libraries via `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Google Gemini API**:

    You need to have a **Google Gemini API** key. If you don't have it already, follow these steps:

    - Create an account and get your API key from [Google Gemini](https://generativeai.google.com/).
    - Create a `.env` file in the root directory of the project.
    - Add your API key to the `.env` file like this:

      ```env
      GEMINI_API_KEY=your_google_gemini_api_key_here
      ```

4. **Run the Streamlit app**:

    Start the Streamlit app to launch the chatbot in your browser:

    ```bash
    streamlit run PizzaBot.py
    ```

5. Open your browser and go to `http://localhost:8501` to interact with the Pizza OrderBot!

## 🛠️ Tech Stack

- **Google Gemini API**: Used for natural language processing and generating the bot's responses.
- **Streamlit**: Provides an easy-to-use interface to display the chat interactions.
- **Python**: Core programming language used for developing the chatbot logic and interacting with APIs.
- **dotenv**: Loads the API key from the `.env` file for secure usage.

## 📄 Menu and Order Details

### Pizza Options:
- **Pepperoni Pizza**: ₹399 (Large), ₹299 (Medium), ₹199 (Small)
- **Cheese Pizza**: ₹349 (Large), ₹249 (Medium), ₹179 (Small)
- **Eggplant Pizza**: ₹369 (Large), ₹269 (Medium), ₹189 (Small)

### Sides:
- **Fries**: ₹129 (Large), ₹89 (Small)
- **Greek Salad**: ₹199

### Toppings:
- Extra Cheese: ₹49
- Mushrooms: ₹39
- Sausage: ₹69
- Canadian Bacon: ₹79
- AI Sauce: ₹39
- Peppers: ₹29

### Drinks:
- **Coke**: ₹82 (Large), ₹62 (Medium), ₹42 (Small)
- **Sprite**: ₹79 (Large), ₹59 (Medium), ₹39 (Small)
- **Bottled Water**: ₹25

## 🤖 How It Works

The bot walks users through the following steps:
1. **Greeting**: The bot welcomes the user and invites them to place their order.
2. **Order Collection**: The bot collects the pizza details like size, toppings, sides, and drinks.
3. **Order Summary**: The bot summarizes the order, including a bill breakdown with subtotals, taxes, and total cost.
4. **Payment Method**: The bot asks for the payment method (cash, card, or UPI).
5. **Confirmation**: The bot finalizes the order and thanks the customer.

## 💡 Key Takeaways

- **Prompt Engineering**: How to craft effective prompts for a chatbot.
- **LLM Implementation**: Practical implementation using Google Gemini API.
- **Interactive UI**: Built an engaging chat interface with Streamlit.
- **Creative Solutions**: Used Google Gemini in place of a paid OpenAI API subscription.

## 💬 Contact

If you have any questions or need help with the project, feel free to reach out to me on LinkedIn: [H Athulkrishnan](https://www.linkedin.com/in/h-athulkrishnan/).

---

Enjoy building and testing out the **Pizza OrderBot**! 🍕🤖

