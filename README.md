# Ethereum Analytics

This repository contains analytics notebooks used in the *End-user Comprehension of Usage Risks in Smart Contracts* paper.

Other resources can be found at the [linktree](https://linktr.ee/tethersurvey).

Note that specific numbers may differ from the paper itself, due to more source code being added to [Etherscan](https://etherscan.io/).

# Requirements
## Dependencies
- Python version 3.9.17
- The `poetry` dependency manager (`pip install poetry`)
- The `surya` [command line tool](https://github.com/Consensys/surya) (used for extracting ASTs from Solidity source code). This is installed with node (`npm install -g surya`)

## Data
Download the **Ethereum Transaction Data** from the [linktree](https://linktr.ee/tethersurvey) and extract it into this root folder (so that the `./data/blocks-reduced` path appears.

This contains ethereum transaction data for each block in JSON over our analysis period, reduced to only the following fields: `timestamp`, `block_number` , `to`, `from`.

## API Keys
The API keys are free to obtain. Please place them in a `.env` file in the root of this directory, as such:

```
ETHERSCAN_API_TOKEN="XXXXXXXX"
ALCHEMY_API_KEY="XXXXXXXX"
```

- [Etherscan API key registration](https://etherscan.io/apis)
- [Alchemy API key registration](https://docs.alchemy.com/docs/alchemy-quickstart-guide)

Note: For Alchemy, just the key is sufficient (do not give the whole URL.)

# Running the code
1. Run the `Process` notebook to generate required files
2. Run `ERC-20 Analytics` or `Check addresses for bytecode` as you see fit
