# tsudo

Tsundere wrapper for sudo command.

Spice up your sudo password prompt with cute remarks. Hand-picked from most
famous characters and internet memes. Also, you can add your own currated list
of insults (in the future).

## Installation

```
$ pip install tsudo --user
```

## Enable sudo insults

Uncomment this line from your `sudoers` file

```
# Defaults insults
```

## Enable credential caching

> sudoers uses per-user time stamp files for credential caching. Once a user
> has been authenticated, a record is written containing the user ID that was
> used to authenticate, the terminal session ID, the start time of the session
> leader (or parent process) and a time stamp (using a monotonic clock if one
> is available).

Since pexpect spawn another child process using pty, each `tsudo` call will
have different credentials. However, you can still use another tty creds by
turning off `tty_tickets`.

Add this line to your `sudoers` file

```
Defaults !tty_tickets
```

