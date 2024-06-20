import sys
import asyncio
import readline
import subprocess
import shlex
from prompt_toolkit.shortcuts import radiolist_dialog, message_dialog, input_dialog
from prompt_toolkit.shortcuts.progress_bar import ProgressBar
import requests

async def call_api(query: str):
    if query:
        url = "http://0.0.0.0:8000/query-agent"
        response = None
        with ProgressBar() as pb:
            for i in pb(range(100), label="Fetching response..."):
                if i < 90:
                    await asyncio.sleep(0.05)  # Simulate progress
                else:
                    break

            response = requests.post(url, json={"input": query})
            if response.status_code == 200:
                return response.json()
            else:
                message_dialog(
                    title="Error",
                    text=f"An error occurred: {response.text}"
                ).run()
                return None
    else:
        return "There seems to be some issue with this query, can you try this again?"

def edit_command(initial_command):
    readline.set_startup_hook(lambda: readline.insert_text(initial_command))
    try:
        edited_command = input_dialog(
            title="Edit Command",
            text="Edit the command:",
            default=initial_command
        ).run()
    finally:
        readline.set_startup_hook()
    return edited_command

def execute_command(command):
    try:
        result = subprocess.run(shlex.split(command), capture_output=True, text=True)
        output = f"Command output:\n{result.stdout}"
        if result.stderr:
            output += f"\nError output, if any:\n{result.stderr}"
        message_dialog(
            title="Command Execution Result",
            text=output
        ).run()
    except Exception as e:
        message_dialog(
            title="Error",
            text=f"An error occurred while executing the command: {e}"
        ).run()

def choose_action():
    result = radiolist_dialog(
        title="Choose Action",
        text="What would you like to do?",
        values=[
            ("edit", "Edit the command"),
            ("run", "Run the command"),
            ("quit", "Quit")
        ],
    ).run()
    return result

def main():
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = input_dialog(
            title="Input Query",
            text="Enter your query:"
        ).run()

    response = asyncio.run(call_api(query))
    if response is None:
        return
        
    tool = response['tool']

    if tool == 'Queries':
        command_to_run = response['message']
        message_dialog(
            title="Suggested Command",
            text=f"The suggested command is: {command_to_run}"
        ).run()

        action = choose_action()

        if action == 'edit':
            command_to_run = edit_command(command_to_run)
            execute_command(command_to_run)
        elif action == 'run':
            execute_command(command_to_run)
        elif action == 'quit':
            message_dialog(
                title="Exit",
                text="Exiting the application."
            ).run()
            sys.exit(0)

    elif tool == 'Greet':
        message_dialog(
            title="Greeting",
            text=response['message']
        ).run()

    else:
        message_dialog(
            title="Info",
            text="Can't help you right now. Please try again later."
        ).run()

if __name__ == '__main__':
    main()
