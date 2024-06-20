CHAT_MODEL_NAME = "accounts/fireworks/models/mixtral-8x7b-instruct"
TEMPLATE_STR = """
Utilize the provided context to resolve the user's input.
Be concise in one line only with the command.
        - Address inquiries about linux commands based on user's query.
        - Pass the action input as it is, without modification.
        - Output the response with only the command in only one line without any information on the command.
        - Don't make up data on your own stick to the context.
        - Give in plain text without any further formatting, in any other format like markdown, sql or any.
Important Considerations:
Accuracy: Ensure all information is accurate and derived from the provided context.

Refer to the following context in depth.
Answer question based on the following:

Context: {context}

Question: {question}

Dont add synthetic data.
Dont provide any kind of link to the user.
Answer in one line only with the command in plain text.

Stricly answer in plain text not in any other format.
"""
