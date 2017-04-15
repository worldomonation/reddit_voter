#!/usr/bin/env python3

'''This is an updated version of the reddit downvote bot.
praw 4.4.1 compatible.
Originally created by Kabalan over at https://redditbot.codeplex.com/
'''

import sys
import os
import json

import getpass
import praw

# from oauth2client.file import Storage
from prawcore.exceptions import OAuthException, Forbidden


class RedditClient:

    user = None
    keep_alive = True
    valid = {
        "yes": True,
        "y": True,
        "Y": True,
        "ye": True
    }

    def __init__(self, username, password):
        '''
        @param username:    the username of the account to log in
        @param password:    password for the account above
        '''

        self.user_agent = 'just_a_normal_user'
        self.client_id = self.client_secret = self.username = self.password = None

        with open('credentials.json') as credentials:
            data = json.load(credentials)
            self.client_id = data['client_id']
            self.client_secret = data['client_secret']
            self.username = data['username'] if 'username' in data else username
            self.password = data['password'] if 'password' in data else password

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
                print('---> Logged into Reddit.')
            else:
                raise OAuthException
        except (OAuthException, Forbidden) as e:
            print('---> Failed login due to {0}.'.format(type(e).__name__))
            sys.exit()

    def downvote(self):
        '''
        The downvote module.
        '''
        try:
            downvote_target = input('Username of redditor to downvote: ')
            num_comments_to_downvote = int(input('Number of comments to downvote: '))
            for comment in self.user.redditor(downvote_target).comments.new(limit=num_comments_to_downvote):
                comment.downvote()
        except:
            print('Failed to initialize downvote module!')

    def upvote(self):
        '''
        The upvote module.
        '''
        try:
            upvote_target = input('Username of redditor to upvote: ')
            num_comments_to_upvote = int(input('Number of comments to upvote: '))
            for comment in self.user.redditor(upvote_target).comments.new(limit=num_comments_to_upvote):
                comment.upvote()
        except Exception as e:
            raise

    def prompt_user(self, user_input):
        return user_input in self.valid


if __name__ == '__main__':
    username = input('Please provide your Reddit username: ')
    password = getpass.getpass()
    client = RedditClient(username, password)
    while client.keep_alive:
        module_to_run = int(input('Please select from the following options:\n1. upvote a user\n2. downvote a user\n'))
        if module_to_run == 1:
            client.upvote()
        elif module_to_run == 2:
            client.downvote()
        else:
            print('You have made an invalid selection.\n')
        client.keep_alive = client.prompt_user(input('Would you like to perform another action? [y/n]'))
    print('Goodbye!')
