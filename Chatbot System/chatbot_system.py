import json
import random

def intro():
    """Prints the welcome message and introductory instructions for the chatbot system."""
    print("\t\t\t\tWelcome to the chatbot system of the University of Poppleton.")
    print("\t\t\tI am your chatbot agent to help you with any questions related to the university.")
    print("\t\t\t\t\t\t\tlet’s get started!")


def load_json_file(file):
    """Loads the chatbot responses and configurations from the specified JSON file."""
    with open(file, "r") as json_file:
        print("\n\n|JSON File loaded successfully.|")
        data = json.load(json_file)
        return data
    

def random_agent_names(data):
    """Selects and returns a random agent name from the list in the data."""
    agent_names = data["agent_names"]
    return random.choice(agent_names)


def print_agent_name(agent_name):
    """Prints a greeting message introducing the chatbot agent to the user."""
    print(f"\n\nHello, I am your agent {agent_name}. Nice to meet you!")
    print()
    print(f"{agent_name}: How can I help you today?")
    print("-----------------------------------")


def user_input():
    """Prompts the user for input and returns it in lowercase."""
    user_response = input("You: ")
    user_response = user_response.lower()
    return user_response


def random_responses(data):
    """Selects and returns a random response from the list of random responses in the data."""
    random_response = data["random_responses"]
    return random.choice(random_response) 


def response_from_bot(user_input_data, data):
  """Returns a bot response based on the user's input by checking for matching keywords."""
    for response in data["bot_responses"]:
        for keyword in response["user_input"]:
            if keyword in user_input_data:
                return response["bot_response"]

    return random_responses(data)


def log_responses(user_query, bot_answer, file_name):
    """Logs the user's question and the bot's response to a text file."""
    with open(file_name, "a") as log_file:
        log_file.write(f"user question: {user_query}\n")
        log_file.write(f"bot response: {bot_answer}\n")


def conversation(data, agent_name, file_name):
    """Handles the conversation flow between the user and the bot, including logging responses."""
    boolean_value = True
    while boolean_value:
        user_question = user_input()  
        if user_question in data["exit_commands"]:  
            goodbye_response = f"{agent_name}: Thank you for your time! Hoping to meet you again!"
            print(goodbye_response)
            log_responses(user_question, goodbye_response, file_name)
            boolean_value = False  
        else:
            bot_response = response_from_bot(user_question, data) 
            print(f"{agent_name}: {bot_response}")
            print("------------------------------------------------------------------------------------------------------------------------")
            log_responses(user_question, bot_response, file_name)
    print("\n\n|Logged into txt file successfully.|")


def call_functions():
    """Starts the chatbot system by calling the necessary functions for loading data and initiating the conversation."""
    intro()

    json_file_name = "chatbot_responses.json"
    json_data = load_json_file(json_file_name)

    bot_name = random_agent_names(json_data)
    
    print_agent_name(bot_name)

    log_file_name = "log_responses.txt"
    conversation(json_data, bot_name, log_file_name)

call_functions()
