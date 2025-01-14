import openai
import os

# Set up OpenAI API key from environment variable
openai.api_key = "your-api-key-here"

def ask_openai(prompt):
    """
    Send a prompt to OpenAI's GPT model and get a response.
    Handles errors gracefully.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the GPT model optimized for chat
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,  # Limit response length
            temperature=0.7  # Adjust creativity
        )
        return response.choices[0].message['content'].strip()
    except openai.error.AuthenticationError:
        return "Authentication error: Please check your OpenAI API key."
    except openai.error.OpenAIError as e:
        return f"OpenAI API error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def start_chat():
    """
    Start the interactive chatbot loop.
    Users can type queries and exit using specific commands.
    """
    print("\nWelcome to the Chatbot!")
    print("Type your queries below. Type ':q', 'quit', or 'exit' to end the conversation.\n")

    exit_conditions = (":q", "quit", "exit")

    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in exit_conditions:
                print("Goodbye! Have a great day 😊")
                break
            elif not user_input:
                print("Please enter a valid question.")
            else:
                response = ask_openai(user_input)
                print(f"🌱 {response}")
        except KeyboardInterrupt:
            print("\nGoodbye! Have a great day 😊")
            break
        except Exception as e:
            print(f"Oops! Something went wrong: {e}")

if __name__ == "__main__":
    # Your code here

    if not openai.api_key:
        print("Error: OpenAI API key not found. Please set the 'OPENAI_API_KEY' environment variable.")
    else:
        start_chat()