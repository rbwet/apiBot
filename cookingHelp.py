#by Robbie Wetzel and Aidan Brownell 


""" 1. Introduction
Chatbots have been around for decades and were one of the early successes with NLP in that the convinced some people that the future of AI was NOW (in the 1960s) and before we knew it, we'd have walking, talking robots. Unfortunately, these were built on a house of cards that required a lot of custom programming to develop for specialized cases, and either didn't work well if any inputs deviated from the expected, or just had limited understanding of the task at hand.

With LLMs, we have a system built on deep neural networks that has a prompt window of around 4k tokens. This window allows the LLM to focus on relevant tasks, in essence, to "pay attention" to what the user is asking, or has talked about recently. But further, they have encoded concepts of logic and instructions within the models, allowing them to follow tasks. This makes the job of building a chatbot easier, in many respects, though building a chatbot that behaves by staying on task, not forgetting relevant information, and follows the given instructions are where the challenge lies.

In this assignment, you'll build a chatbot specific to a task using your LLM! Using the techniques you've learned about prompting and LLMs up to this point, you'll build on those to create a chatbot for your needs.

2. Objectives
By the end of this project, you will be able to:

Use the LLM APIs and their concept of memory to build a chatbot that responds to prior interactions.
Develop the prompts needed to respond and react to a specific task
Create a chatbot specific to a task that stay on task and keep track of relevant information.
3. Materials Needed
You will need your computer, Visual Studio Code, git (and possibly a graphical git client), and access to your LLM API.

4. Setup
Graduates may not work with or form teams with undergraduates on this assignment.

You may work in groups of up to 3 people, but groups are not necessary.

5. What to Do
This lab requires some creativity. You will need to come up with a topic that your chatbot will be tailored for. To help you, here are a list of ideas that you could pursue, so pick something that is interesting and remember that your idea does not need to be listed here as these are just suggestions.

Customer service support: design an agent to provide answers to frequently asked questions on some product or other service and provide support to them--it could be technical support for example. You'd probably want to find some kind of FAQ related to whatever you're planning or ask your LLM to create an FAQ on some fictional product that you design.
Sales agent: design an agent that will help a customer by answering questions about products, pricing and features. You would need to specify multiple products, prices, and the descriptions of those products. This is an extension of what we did in class with CuppaCosmos!
git support: create an agent that helps answer questions specifically about git problems. You can refer to numerous websites that give you information about git.
Beginner python support: design an agent that helps answer questions about 1st-year python assignments. The agent shouldn't solve the problems, but should ask the student questions to determine what problems they're having and then guide them to answers without giving away the problems. You'll want to look back at a first-year assignment.
AI for a game: design a chatbot for a non-player character in a game that can respond in character to questions from players and in relation to particular knowledge the AI might have.
A chatbot for advising CS courses: this would of course be specific to DU and could question the student on courses they've taken so it could make good recommendations.
In all of these cases, you must:

Prevent prompt injections
Respond only in the area your chatbot is limited to--this means your prompting must include everything the chatbot needs.
Be "safe"
Be tested
In all of these cases, you are not allowed to upload lots of documents, etc., that the chatbot has to work through, even if you know how to code that. The intent of the assignment is to improve your prompting abilities, not your ability to string tools together (that will be the next project). The only memory your chatbot can have is its prompts--so no databases or other techniques, though you can write your own python to save and store prompts internally to the program and decide what prompts to send to the LLM.

Note you should use categories and chain-of-thought prompting to successfully prompt your chatbot, we'll be looking for that.

Finally, we will do presentations of the chatbots in class, so please be prepared to do that.

## my idea for prompt 

Cooking and Recipe Guide
Topic: Assisting users in the kitchen.
Features:
Suggest recipes based on available ingredients
Provide step-by-step cooking instructions
Offer tips for substitutions and dietary modifications


"""


from openai import OpenAI

client = OpenAI()

def get_llm_response(client: OpenAI, conversation_history: list) -> str:
    messages = [{"role": "system", "content": "You are a cooking and recipe assistant. Help the user with cooking-related questions, recipe suggestions, and culinary tips."}]
    messages.extend(conversation_history)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message.content

def start():
    print("Welcome to the Cooking and Recipe Guide Chatbot")
    print("Type 'exit' anytime to end the conversation")
    conversation_history = []
    stop = False

    while not stop:
        user_input = input("Chat with the cooking bot: ")
        if user_input.lower() == 'exit':
            stop = True
        else:
            conversation_history.append({"role": "user", "content": user_input})
            response = get_llm_response(client, conversation_history)
            print("Chatbot:", response)
            print("\n\n")
            conversation_history.append({"role": "assistant", "content": response})

def main():
    start()

if __name__ == "__main__":
    main()
