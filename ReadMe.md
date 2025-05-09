# Project 2: Chat Bot
## Cooking Help
### Authors: Robbie Wetzel and Aidan Brownell
<br/>
<br/>

## Goal:
To create a chatbot to aid in cooking, coming up with recipes, solutions to cooking problems, and to overall aid in creating a more pleasant cooking environment.

## Getting a Response:
role: sytem
<br/>
content: "You are are a cooking and recipe assistant. Help the user with cooking-related questions, recipe suggestions, and culinary tips."
<br/>
When passing the user_response to get_llm_response, a conversation_history list is passed, which is then called using messages.extend.

## Maintaing Memory:
When the user enters their information, {"role": "user", "content": user_input} is appended to conversation_history, when the chatpot gives its response, {"role": "assistant", "content": response} is appended to conversation_history. This provides the chatbot with historical context to the conversation.