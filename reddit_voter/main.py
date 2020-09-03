import os
import sys
from argparse import ArgumentParser

from reddit_voter.client import RedditClient

action = {
    1: 'upvote',
    0: 'downvote'
}

def main():
    """The main executable method of the program.
    """

    args = build_parser()
    client = RedditClient(args)

    if args.downvote or args.upvote:
        # Non-interactive command line
        try:
            pass
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        print('Welcome to interactive reddit voter.\n')
        # Interactive command line
        while True:
            try:
                module_to_run = int(input('Select from the following options:\n'
                                          '1. upvote a user\n2. downvote a user\n')) % 2
                target = str(input('Target username: '))
                num_comments = int(input('Number of comments: '))

                client.vote(action.get(module_to_run, None), target, num_comments)
            except KeyboardInterrupt:
                sys.exit(0)
            except ValueError as e:
                invalid_literal = e.args[0].split(': ')[1]
                print(f'Invalid input detected: {invalid_literal}\n')

            user_input = str(input('Perform another action? [y/n]\n'))
            keep_alive = client.prompt_user(user_input)

            if not keep_alive:
                sys.exit(0)


def default_credentials_exist():
    """Determines if credentials file exists in the current working directory.

    If one of the following is found, it returns the path to the file:
        - credentials.json
        - praw.ini

    If both files are found, by default `praw.ini` is used.

    Args:
        None

    Returns:
        path (str):     String representation of the path to located credential file.
    """
    credentials_in_cwd = [
        os.path.join(os.getcwd(), 'credentials.json'),
        os.path.join(os.getcwd(), 'praw.ini')
    ]
    credentials_exists = list(map(os.path.exists, credentials_in_cwd))
    if all(credentials_exists):
        return credentials_in_cwd[-1]
    else:
        return credentials_in_cwd[credentials_exists.index(True)]


def build_parser():
    """Builds a parser, used to accept user-specified parmeters.

    Returns:
        args (Namespace):   Parsed command line arguments.
    """
    parser = ArgumentParser()
    parser.add_argument('-d', '--downvote',
                        action='store_true', help="Initiate downvote.")
    parser.add_argument('-u', '--upvote', action='store_true',
                        help="Initiate upvote.")
    parser.add_argument('-n', '--count', action='store',
                        default=5, help=" ".join([
                            "Number of posts to upvote/downvote.",
                            "Defaults to 5."
                        ]))
    parser.add_argument('-cj', '--json', action='store',
                        default=None, help=" ".join([
                            "Imports credentials from credentials.json file."
                        ]))
    parser.add_argument('-ci', '--ini', action='store',
                        default=None, help=" ".join([
                            "Imports specified configuration name from praw.ini file.",
                        ]))

    args, _ = parser.parse_known_args()
    return args


if __name__ == '__main__':
    main()
