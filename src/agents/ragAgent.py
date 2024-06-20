import logging
import dotenv
import os
from logging_config import setup_logging
from langchain.agents import create_react_agent, Tool, AgentExecutor
from langchain import hub
from langchain_fireworks import Fireworks
from src.agents.toolDesc import ToolDescriptions
from src.tools.getChain import GetChain
from src.tools.getDefault import GetDefault
from src.tools.getGreet import GetGreet
from src.agents.config import AGENT_MODEL, AGENT_PROMPT, CHAT_MODEL_NAME

setup_logging()
dotenv.load_dotenv()

class LC_AgentExecutor:
    def __init__(self, retriever):
        try:
            self.faq_chain = GetChain(retriever)
            self.default_instance = GetDefault()
            self.greet_instance = GetGreet()

            self.agent_tools = [
                Tool(
                    name="Queries",
                    func=self.faq_chain.get_chain,
                    description=ToolDescriptions.QUERIES
                ),
                Tool(
                    name="Greet",
                    func=self.greet_instance.get_greet,
                    description=ToolDescriptions.GREET
                ),
                Tool(
                    name="Default",
                    func=self.default_instance.get_default,
                    description=ToolDescriptions.DEFAULT
                )
            ]

            self.agent_prompt = hub.pull(AGENT_PROMPT)
            self.agent_chat_model = Fireworks(
                model=AGENT_MODEL,
                max_tokens=256
            )
            
            self.custom_agent = self.create_agent()
            self.agent_executor = self.create_executor()
            logging.info("LC_AgentExecutor initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing LC_AgentExecutor: {e}")
            raise

    def create_agent(self):
        try:
            custom_agent = create_react_agent(
                llm=self.agent_chat_model,
                prompt=self.agent_prompt,
                tools=self.agent_tools,
            )
            logging.info("React agent created successfully")
            return custom_agent
        except Exception as e:
            logging.error(f"Error creating React agent: {e}")
            raise

    def create_executor(self):
        try:
            executor = AgentExecutor(
                agent=self.custom_agent,
                tools=self.agent_tools,
                return_intermediate_steps=True,
                verbose=True,
                handle_parsing_errors=True,
            )
            
            logging.info("AgentExecutor created successfully")
            return executor
        except Exception as e:
            logging.error(f"Error creating AgentExecutor: {e}")
            raise

    def get_executor(self):
        try:
            return self.agent_executor
        except Exception as e:
            logging.error(f"Error getting AgentExecutor: {e}")
            raise
