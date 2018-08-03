# -*- coding: utf-8 -*-
'''
    tsudo.py
    ~~~~~

    This module contains most of the tsudo functionality.

    :copyright: © 2018 by Giovan Isa Musthofa.
    :license: WTFPL, see LICENSE for more details.
'''

import sys
import re
import pexpect
from os import getlogin
from random import Random
from collections import deque

prompt = '[sudo] password for %s: ' % getlogin()
attempts_up_pat = re.compile(r'sudo: [0-9]+ incorrect password attempt')
rand = Random()
output_buffer = deque()

def main(args):
    sudo = pexpect.spawn('sudo', args)
    sudo.interact(output_filter=insults_filter_utf8)

def insults_filter(sudo_out):
    '''
    This function filters sudo outputs by catching insult lines and
    replace it with a random hand-picked tsundere line.
    '''

    global output_buffer

    if sudo_out == '\r\n' or attempts_up_pat.match(sudo_out):
        return sudo_out

    elif prompt in sudo_out:
        if output_buffer or sudo_out != prompt:
            if sudo_out == prompt:
                output_buffer.pop()
            return '%s\r\n%s' % (rand_tsun(), prompt)
        else:
            return prompt

    elif not output_buffer:
        output_buffer.append(sudo_out)
        return ''

    else:
        while output_buffer:
            print(output_buffer.pop(), end='')
        return sudo_out

def insults_filter_utf8(sudo_out_raw):
    '''
    This function wraps insults_filter by converting bytes and
    utf-8 encoded string back and forth to pexpect spawn instance.
    '''
    return insults_filter(sudo_out_raw.decode('utf-8')).encode('utf-8')

def rand_tsun():
    '''Return a random tsundere response from `tsun_lines`.'''
    return rand.choice(tsun_lines)

tsun_lines = (

    # Generic tsudere lines
    # source https://www.reddit.com/r/Tsunderes/wiki/tsunderelines<Paste>

    "N-No, it's not like I did it for you! I did it because I had freetime, that's all!",
    "I like you, you idiot!",
    "BAKAAAAAAAAAAAAAAA!!!!! YOU'RE A BAKAAAAAAA!!!!",
    "I'm just here because I had nothing else to do!",
    "Are you stupid?",
    "You're such a slob!",
    "You should be grateful!",
    "You're free anyways, right?",
    "Don't misunderstand, it's not like I like you or anything...",
    "H-Hey....",
    "....T-Thanks.....",
    "T-Tch! S-Shut up!",
    "I just had extra, so shut up and take it!",
    "Can you be ANY MORE CLUELESS?",
    "HEY! It's a privilege to even be able to talk to me! You should be honored!",
    "Geez, stop pushing yourself! You're going to get yourself hurt one day, you idiot!"
)

if __name__ == '__main__':
    main(sys.argv[1:])

