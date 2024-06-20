import logging
from logging_config import setup_logging
from src.chains.faqChain import FAQChain

setup_logging()

class GetChain:
    def __init__(self, retriever):
        self.chain_instance = FAQChain(retriever)
        self.chain = self.chain_instance.get_chain()
        logging.info("Chain initialized successfully")

    def get_chain(self, query: str):
        """
        Processes the given query using the initialized chain.
        """
        try:
            logging.info(f"Received query: {query}")
            response = self.chain.invoke(query)
            return response
        except Exception as e:
            logging.error(f"Error processing query '{query}': {e}")
            return "There was an error processing your request. Please try again later."
