"""
This is a re-written & updated version of the reddit downvote bot.
PRAW 4.4.1 compatible.
Original idea created by Kabalan over at https://redditbot.codeplex.com/

All prospective users should register a Script Type application at
https://www.reddit.com/prefs/apps/ to obtain Client Secret and Client ID keys.

For information on how to use, please see the README file at the root of this
repository.
"""

import json
import sys
from argparse import ArgumentError

import praw

from praw.exceptions import ClientException
from prawcore.exceptions import Forbidden, OAuthException, ResponseException

import progressbar


class RedditClient():
    """RedditClient is a class which represents a unique client instance that
    is able to interact with Reddit.
    """

    user = None
    prog_bar = progressbar.ProgressBar()
    valid = {
        "yes": True,
        "y": True,
        "Y": True,
        "ye": True
    }
    args = None

    def __init__(self, args):
        """Initializes an instance of Reddit client.

        Given a set of credentials, it will first attempt to validate the file.

        Once validated the credentials are piped into the PRAW constructor which
        handles interaction with Reddit. If the response is as expected, various
        internal attributes are set.

        Args:
            args (Namespace):   Parsed command line arguments.

        Returns:
            None

        Raises:
            OAuthException:     If authentication fails using OAuth2.
            Forbidden:          If username is None.
            KeyError:           If dictionary keys are not found.
        """

        self.user_agent = 'just_a_normal_user'
        self.ini = None
        self.client_id = None
        self.client_secret = None
        self.username = None
        self.password = None

        if args.json:
            try:
                with open(args.credentials) as credentials:
                    data = json.load(credentials)
                    self.client_id = data['client_id']
                    self.client_secret = data['client_secret']
                    self.username = data.get('username')
                    self.password = data.get('password')
            except FileNotFoundError:
                print(f'Specified credentials file at {args.credentials} does not exist.')
                sys.exit(1)
        elif args.ini:
            self.ini = args.ini
        else:
            self.ini = 'DEFAULT'

        self.authenticate()

    def authenticate(self):
        """Authenticates against Reddit.

        This will create an instance of a reddit user from credentials provided.
        """
        print('---> Authenticating against Reddit.')

        try:
            if self.ini:
                self.user = praw.Reddit(site_name=self.ini,
                                        user_agent=self.user_agent)
            else:
                self.user = praw.Reddit(user_agent=self.user_agent,
                                        client_id=self.client_id,
                                        client_secret=self.client_secret,
                                        password=self.password,
                                        username=self.username)
        except ClientException as e:
            print(" ".join([
                "DEFAULT credentials missing from praw.ini.",
                "Either define DEFAULT credentials or specify a credential set using --ci flag."
            ]))
            sys.exit(1)
        except (OAuthException, Forbidden) as e:
            print(f'Failed authentication: {e.error}')
            sys.exit(1)
        except ResponseException as e:
            print(f'Failed authentication: {e.response.reason}')
            sys.exit(1)

        if self.user.user.me() is not None:
            print('---> Successfully authenticated against Reddit as {0}.'.format(
                self.user.user.me())
            )

    def downvote(self):
        """The downvote module.

        Returns:
            None
        """
        try:
            downvote_target = input('Username of redditor to downvote: ')
            num_comments_to_downvote = int(input('Number of comments to downvote: '))
            for comment in self.prog_bar(
                    self.user.redditor(downvote_target).comments.new(
                        limit=num_comments_to_downvote)):
                comment.downvote()
        except ValueError:
            print('Number of comments must be an integer.')
        except:
            print('Failed to downvote user: {0}. Check your inputs and try again.'.format(downvote_target))

    def upvote(self):
        """The upvote module.

        Returns:
            None
        """
        try:
            upvote_target = input('Username of redditor to upvote: ')
            num_comments_to_upvote = int(input('Number of comments to upvote: '))
            for comment in self.prog_bar(self.user.redditor(upvote_target).comments.new(
                                                limit=num_comments_to_upvote)):
                comment.upvote()
        except ValueError:
            print('Number of comments must be an integer.')
        except:
            print('Failed to upvote user: {0}. Check your inputs and try again.'.format(upvote_target))

    def prompt_user(self, user_input):
        return user_input in self.valid
