# Cooking Help Chatbot

Cooking Help Chatbot is an AI-powered assistant that provides recipe suggestions, cooking tips, meal planning, and personalized diet recommendations. It interacts in real-time with users and maintains context throughout the conversation to deliver relevant and continuous responses.

---

## 📌 Features

* **Recipe Suggestions:** Get personalized recipe ideas based on your preferences and dietary needs.
* **Meal Planning:** Receive structured meal plans for various goals like weight loss, muscle gain, or balanced nutrition.
* **Ingredient Substitutions:** Find suitable ingredient swaps for dietary restrictions.
* **Contextual Memory:** Maintains the context of the conversation to deliver more personalized responses.

---

## 🚀 Getting Started

### Prerequisites

> **⚠️ Important:** This project requires an **OpenAI API Key** for functionality. Do **not** hardcode your OpenAI API key directly in the script or push it to your repository. Exposing API keys can lead to unauthorized usage and security risks.

The recommended approach is to store it in a **secure environment variable** or reference it from a **`.env` file**:

```bash
export OPENAI_API_KEY='your_openai_api_key_here'
```

Alternatively, use a `.env` file and load it using `dotenv`:

1. Install `python-dotenv`:

   ```bash
   pip install python-dotenv
   ```

2. Create a `.env` file:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. Load it in your script:

   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()
   openai_api_key = os.getenv('OPENAI_API_KEY')
   ```

**Never** push `.env` files to version control. Add it to `.gitignore`:

```plaintext
.env
```

Ensure you have Python installed:

```bash
sudo apt-get update
sudo apt-get install python3
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Dependencies:

* `openai`
* `dotenv`
* `json`

---

## 📂 Directory Structure

```
.
├── cookingHelp.py            # Main chatbot logic
├── test_prompt.txt           # Example prompts and conversations
├── requirements.txt          # Dependencies
├── ReadMe.md                 # Project documentation
```

---

## 📝 Maintaining Memory

When the user enters their information, the chatbot appends:

```json
{"role": "user", "content": user_input}
```

to `conversation_history`. When the chatbot responds, it appends:

```json
{"role": "assistant", "content": response}
```

This structure allows the chatbot to remember past interactions and provide more contextually aware responses during the conversation.

---

## 💡 Usage

To start the chatbot:

```bash
python3 cookingHelp.py
```

---

### Example:

```plaintext
User: What should I cook with chicken and spinach?
Chatbot: How about a creamy chicken and spinach pasta? I can provide you with a recipe if you'd like!
```

---

## 🔍 Advanced Usage

* **Custom Prompt Files:** You can create custom prompt scripts to simulate conversations.
* **Extend the Memory:** Memory can be saved and loaded from JSON files to maintain state between sessions.
* **Real-Time Weather Awareness:** Future extensions can allow the bot to suggest meals based on weather conditions.

---

## 🛠️ Error Handling and Debugging

* **Missing API Key:** Ensure your OpenAI API key is set in your environment variables.
* **Dependencies Missing:** Run `pip install -r requirements.txt` if you encounter import errors.
* **JSON Parsing Issues:** Check the structure of your `.json` files if parsing errors occur.

---

## 🤝 Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.
