# Blockchain Application

# Imports
import streamlit as st
import datetime as datetime
from dataclasses import dataclass
from typing import Any, List
import pandas as pd
import datetime as datetime
import hashlib


# Creates the Block and PyChain data classes

@dataclass
class Block:
    data: Any
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        return sha.hexdigest()

# Create the data class PyChain


@dataclass
class PyChain:
    chain: List[Block]

    def add_block(self, block):
        self.chain += [block]

####################
## Streamlit Code ##
####################

# Add the cache decorator for Streamlit


@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block(data="Genesis", creator_id=0)])


pychain = setup()

st.markdown("# PyChain: A Python Blockchain Application")
st.markdown("## Store Data in the Chain")

input_data = st.text_input("Block Data")

# Add the button
if st.button("Add Block"):

    # @TODO:
    # Select the previous block in the chain
    prev_block = pychain.chain[-1]

    # @TODO:
    # Hash the previous block in the chain
    prev_block_hash = prev_block.hash_block()

    # @TODO:
    # Create a new block in the chain
    new_block = Block(data=input_data, creator_id=42, prev_hash=prev_block_hash)

    # @TODO:
    # Add the new block to the chain
    pychain.add_block(new_block)

 
# Display the the `PyChain` ledger data on the Streamlit webpage
st.markdown("## PyChain Ledger")

# @TODO:
# Create a Pandas DataFrame to display the `PyChain` ledger
pychain_df = pd.DataFrame(pychain.chain)

# @TODO:
# Use the Streamlit `write` function to display the `PyChain` DataFrame
st.write(pychain_df)