import sys
from argparse import ArgumentParser

from reddit_voter.client import RedditClient


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
        # Interactive command line
        while True:
            try:
                module_to_run = None
                try:
                    module_to_run = int(input('Please select from the following options:\n'
                                              '1. upvote a user\n2. downvote a user\n'))
                except ValueError:
                    pass
                if module_to_run == 1:
                    client.upvote()
                elif module_to_run == 2:
                    client.downvote()
                else:
                    print('You have made an invalid selection.\n')
                keep_alive = client.prompt_user(
                    input('Would you like to perform another action? [y/n]\n')
                )
                if not keep_alive:
                    sys.exit(0)
            except KeyboardInterrupt:
                sys.exit(0)


def build_parser():
    """Builds a parser, used to accept user-specified parmeters.
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
    parser.add_argument('-c', '--credentials', action='store',
                        default="credentials.json", help=" ".join([
                            "Import credentials from file.",
                            "Defaults to credentials.json in the current directory."
                        ]))

    args, _ = parser.parse_known_args()
    return args


if __name__ == '__main__':
    main()
