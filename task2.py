import datetime
import webbrowser
import os

def get_response(user_input):
    """Match user input to a command and return a response."""
    command = user_input.lower().strip()

    # Greetings
    if command in ["hello", "hi", "hey"]:
        return "Hello! I'm your personal assistant. Type 'help' to see what I can do."

    # Tell time
    elif "time" in command:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."

    # Tell date
    elif "date" in command:
        today = datetime.datetime.now()
        return f"Today's date is {today.strftime('%A, %B %d, %Y')}."

    # Open browser
    elif "open browser" in command or "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google in your browser..."

    # Open YouTube
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube for you!"

    # Play music (opens YouTube Music)
    elif "play music" in command:
        webbrowser.open("https://music.youtube.com")
        return "Opening YouTube Music... Enjoy!"

    # Tell a joke
    elif "joke" in command:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 😄"

    # Calculator
    elif "calculate" in command or "calculator" in command:
        webbrowser.open("https://www.google.com/search?q=calculator")
        return "Opening calculator in your browser!"

    # Weather
    elif "weather" in command:
        webbrowser.open("https://www.google.com/search?q=weather+today")
        return "Opening weather info in your browser!"

    # Help menu
    elif command == "help":
        return (
            "\n📋 Available Commands:\n"
            "  hello / hi        → Greet the assistant\n"
            "  time              → Get current time\n"
            "  date              → Get today's date\n"
            "  open browser      → Open Google\n"
            "  youtube           → Open YouTube\n"
            "  play music        → Open YouTube Music\n"
            "  joke              → Hear a joke\n"
            "  calculate         → Open a calculator\n"
            "  weather           → Check today's weather\n"
            "  quit / exit       → Close the assistant\n"
        )

    # Exit
    elif command in ["quit", "exit", "bye"]:
        return "EXIT"

    # Unknown command
    else:
        return f"Sorry, I don't understand '{user_input}'. Type 'help' to see available commands."


def main():
    print("=" * 55)
    print("  🤖  Rule-Based Personal Assistant")
    print("=" * 55)
    print("Type 'help' to see commands. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        response = get_response(user_input)

        if response == "EXIT":
            print("Assistant: Goodbye! Have a great day! 👋")
            break
        else:
            print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()