import logging
from logging_config import setup_logging
import os
import dotenv
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from src.chains.config import CHAT_MODEL_NAME, TEMPLATE_STR
from langchain_fireworks import Fireworks

setup_logging()
dotenv.load_dotenv()

class FAQChain:
    def __init__(self, retriever):
        try:
            self.chat_model = Fireworks(
                model=CHAT_MODEL_NAME,
                max_tokens=256
            )
            
            self.system_prompt = SystemMessagePromptTemplate(
                prompt=PromptTemplate(
                    input_variables=["context"],
                    template=TEMPLATE_STR,
                )
            )

            self.human_prompt = HumanMessagePromptTemplate(
                prompt=PromptTemplate(
                    input_variables=["question"],
                    template="{question}",
                )
            )

            self.messages = [self.system_prompt, self.human_prompt]

            self.prompt_template = ChatPromptTemplate(
                input_variables=["context", "question"],
                messages=self.messages,
            )

            self.faq_chain = self.create_faq_chain(retriever)
            
            logging.info("FAQChain initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing FAQChain: {e}")
            raise

    def create_faq_chain(self, retriever):
        try:
            faq_chain = (
                {"context": retriever, "question": RunnablePassthrough()}
                | self.prompt_template
                | self.chat_model
                | StrOutputParser()
            )
            return faq_chain
        except Exception as e:
            logging.error(f"Error creating FAQ chain: {e}")
            raise

    def get_chain(self):
        try:
            return self.faq_chain
        except Exception as e:
            logging.error(f"Error retrieving FAQ chain: {e}")
            raise

    def invoke_chain(self, query: str): 
        try:
            response = self.faq_chain.invoke({"input": query})
            return response
        except Exception as e:
            logging.error(f"Error invoking FAQ chain with query '{query}': {e}")
            return "There was an error processing your request. Please try again later."
