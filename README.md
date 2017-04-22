# `reddit_voter`
`reddit_voter` is a command-line tool implemented in Python 3.6 designed to make mass-voting on Reddit a breeze!

## How does it work?

Run `reddit_voter` by invoking the script via a command line:

~~~~
python3 `reddit_voter`.py
~~~~

## Dependencies

reddit_voter depends on PRAW, or [Python Reddit API Wrapper](https://github.com/praw-dev/praw) project to function.

Simply install PRAW for Python 3.6 by invoking it from your favorite shell:

~~~~
pip3 install praw
~~~~

If any issues are encountered during installation of PRAW, please refer to their repository for some troubleshooting steps.

## Authenticating

With dependencies installed and this repository cloned, you must now log into Reddit front-end to access the [apps](https://www.reddit.com/prefs/apps/) setting menu.

Here, create a new *script-type* application. Name it whatever you want, it does not matter.

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
