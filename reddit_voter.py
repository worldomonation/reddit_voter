#!/usr/bin/env python3

'''This is an updated version of the reddit downvote bot.
praw 4.4.1 compatible.
Originally created by Kabalan over at https://redditbot.codeplex.com/

All prospective users should register a Script Type application at
https://www.reddit.com/prefs/apps/ to obtain Client Secret and Client ID keys.

Users are encouraged to store the credentials into a separate file in the base
directory. Filename should be 'credentials.json'. Please ensure it is formatted
correctly prior to use.

Example:
    $ python3 reddit_voter.py


'''

import sys
import os
import json

import getpass
import praw

from prawcore.exceptions import OAuthException, Forbidden


class RedditClient:
    '''RedditClient holds the instance of initialized reddit client.

    Attributes:
        user:       Initialized instance of the reddit client.
        keep_alive: As long as it is True, the script will continue to execute.
        valid:      List of acceptable user iputs used to determine keep_alive.
    '''

    user = None
    keep_alive = True
    valid = {
        "yes": True,
        "y": True,
        "Y": True,
        "ye": True
    }

    def __init__(self):
        '''This is the constructor of the RedditClient instance.
        When supplied with correct set of credentials, it will initialize an
        instance of the Reddit object using PRAW.
        Created instance is then assigned to the user variable for later use.

        Returns:
            None

        Raises:
            OAuthException:     If authentication fails using OAuth2.
            Forbidden:          If username is None.
        '''

        self.user_agent = 'just_a_normal_user'
        self.client_id = self.client_secret = self.username = self.password = None

        with open('credentials.json') as credentials:
            data = json.load(credentials)
            self.client_id = data['client_id']
            self.client_secret = data['client_secret']
            if self.has_parameters:
                self.username = sys.argv[1]
                self.password = sys.argv[2]
            else:
                self.username = data['username']
                self.password = data['password']

        '''
        Authentication phase.
        Creates an instance of a reddit user from credentials provided.
        '''
        print('---> Logging into Reddit.')
        try:
            self.user = praw.Reddit(    user_agent=self.user_agent,
                                        client_id=self.client_id,
                                        client_secret=self.client_secret,
                                        password=self.password,
                                        username=self.username)
            if self.user.user.me() == self.username:
                print('---> Logged into Reddit as {0}.'.format(self.user.user.me()))
            else:
                raise OAuthException
        except (OAuthException, Forbidden) as e:
            print('---> Failed login due to {0}.'.format(type(e).__name__))
            sys.exit()

    def downvote(self):
        '''The downvote module.

        Returns:
            None
        '''
        try:
            downvote_target = input('Username of redditor to downvote: ')
            num_comments_to_downvote = int(input('Number of comments to downvote: '))
            for comment in self.user.redditor(downvote_target).comments.new(
                                                limit=num_comments_to_downvote):
                comment.downvote()
        except:
            print('Failed to initialize downvote module!')

    def upvote(self):
        '''The upvote module.

        Returns:
            None
        '''
        try:
            upvote_target = input('Username of redditor to upvote: ')
            num_comments_to_upvote = int(input('Number of comments to upvote: '))
            for comment in self.user.redditor(upvote_target).comments.new(
                                                limit=num_comments_to_upvote):
                comment.upvote()
        except Exception as e:
            raise

    def prompt_user(self, user_input):
        return user_input in self.valid

    def has_parameters():
        if len(sys.argv) > 1:
            return True


def main():
    '''The main executable method of the program.
    By design, the program will stay alive until either user decides to exit.
    '''
    client = RedditClient()
    while client.keep_alive:
        module_to_run = int(input('Please select from the following options:\n'
                                    '1. upvote a user\n2. downvote a user\n'))
        if module_to_run == 1:
            client.upvote()
        elif module_to_run == 2:
            client.downvote()
        else:
            print('You have made an invalid selection.\n')
        client.keep_alive = client.prompt_user(input(
                            'Would you like to perform another action? [y/n]\n'))
    print('Goodbye!')


if __name__ == '__main__':
    '''Calls the main() function inside a try-catch to handle KeyboardInterrupt
    exceptions with a graceful exit.
    '''
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
