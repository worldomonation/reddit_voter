from reddit_voter.client import RedditClient

from argparse import ArgumentParser

def main():
    """The main executable method of the program.
    """
    args = build_parser()
    client = RedditClient(args)

    while client.keep_alive:
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
        client.keep_alive = client.prompt_user(input(
            'Would you like to perform another action? [y/n]\n'))


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('-d', '--downvote',
                        action='store_true', help="Initiate downvote.")
    parser.add_argument('-u', '--upvote', action='store_true',
                        help="Initiate upvote.")
    parser.add_argument('-c', '--credentials', action='store',
                        default="credentials.json", help="Import credentials from file.")

    args, _ = parser.parse_known_args()
    return args


if __name__ == '__main__':
    main()
