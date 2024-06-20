# cmdX

An AI tool that converts natural language instructions into shell commands for the command line interface (CLI).


This is a CLI tool to provide commands based on the task in the cli itself. This is works on RAG with a custom knowledge base.


## Install and Run
```
# In the project repository after setting up the env
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python api.py  #to start the server
$ python cli.py "task" or python cli.py #to query
```

## Usage

Simply run  the app  followed by your query in natural language:

    python cli.py "find all txt files in the current directory"
or

    python cli.py

It will interpret your command and offer a shell command suggestion with its explaination, which you can:

-   **Edit**  to make adjustments
-   **Run**  the command.
-   **Exit**  if it's not what you were looking for

## Features

-   **Natural Language Understanding**: Easily convert your English sentences into shell commands.
 -  **Command Editing**: Directly edit the suggested command before execution, giving you full control.
-   **Cross-Platform Support**: Whether you're on Linux, macOS, or Windows, NaturalShell works seamlessly.

## Workflow

![Sequence Diagram](https://i.ibb.co/dkw3gpW/Screenshot-2024-06-20-at-3-57-20-PM.jpg)

## Contributing

We welcome contributions to cmdX! Whether it's adding new features, improving documentation, or reporting bugs, please feel free to make a pull request or open an issue.


