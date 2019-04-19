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

Once created, Reddit will generate two sets of seemingly random strings for you. One is a 27 character string and is named *client_secret*. The other is unlabeled on the front end, but is called *client_id* and is shown below the title of your application.

Copy the two strings and save them into a file called `credentials.json` in the working directory of the script. reddit_voter will look for the file, and extract necessary login information to log in.

## *Optional Credentials*

At a minimum, reddit_voter only requires that users save their *client_id* and *client_secret* keys into `credentials.json`. However, if users so desire, it is possible to create two additional keys in the file called *password* and *username*.

`reddit_voter` will look for both the username and password of the Reddit account if run without command line arguments.

It is possible to specify the username and password by directly supplying them as command line arguments when invoking the script as follows:

~~~~
python3 reddit_voter.py username password
~~~~

If invoked this way, reddit_voter will use supplied credentials instead. However, keep in mind the *client_secret* and *client_id* keys are tied to the account.

# Disclaimer

This tool is intended to be used for educational and/or proof-of-concept use only. Do not use this tool to commit malicious and/or criminal acts.
