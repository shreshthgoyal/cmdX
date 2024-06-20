class ToolDescriptions:
    QUERIES = """
        Purpose:
        Use this tool to handle general user inquiries.        
        This tool is helpful when the user queries regarding any task they want to perform in shell or terminal.
        Guidelines:
        - Address inquiries about linux commands based on user's query.
        - Pass the action input as it is, without modification.
        - Output the response with only the command in only one line without any information on the command.
        - Don't make up data on your own stick to the context.
        - Give in plain text without any further formatting, in any other format like markdown, sql or any.

        Example:
        - User Query: "Display hello world"
        - Pass it to the function as it is: "echo "hello world""

        OUTPUT only in plain text, not in any other format. - mandatory
        OUTPUT WHATEVER FUNCTION RETURNS, DONT THINK TWICE
    """
    GREET = """
    Use this query type when the user is greeting specific only and not asking about anything.

    You are here to help the user for any doubts related to commands for shell specifically linux.
    Keep it short and friendly and without any emojis or any form of rich text strictly.
    """

    DEFAULT = """
        use this when the user is asking irrelevant information which is not related to linux commands and not greeting.
        For salutations and greetings use Greet tool.
        Use this when user's queries doesn't fall in any other action provided and the Action is None. Rather than remaining silent, respond to the user by saying you can't answer the following question.
    """
