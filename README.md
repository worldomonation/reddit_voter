# `reddit_voter`
`reddit_voter` is a command-line tool for Python 3 designed to make mass-voting on Reddit a breeze!

## Installation

Use the provided `setup.py` script:

~~~~
python3 setup.py
~~~~

## Run

If installed as a package, run via:

~~~~
voter
~~~~

Otherwise, invoke script manually:

~~~~
python3 reddit_voter.py
~~~~

## Dependencies

`setup.py` will take care of the dependencies, but if desired, it is possible to install them yourself:

~~~~
pip3 install praw
pip3 install progressbar
~~~~

## Credentials

Prior to use, create a new `script` type applicaton on Reddit.

Create `credentials.json` as follows:

~~~~
{
    "client_id": <client_id_from_reddit>,.
    "client_secret": <client_secret_from_reddit>,
    "username": <reddit_username>,
    "password": <reddit_password>
}
~~~~

`reddit_voter` does not store or transmit your username/password in any way. Your credentials are safe and only used to authenticate with Reddit, which is a requirement.

# Disclaimer

This tool is intended to be used for educational and/or proof-of-concept use only. Do not use this tool to commit malicious and/or criminal acts.
