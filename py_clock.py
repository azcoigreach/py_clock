#!/bin/env python
import click
from colorama import init, Fore
import datetime
from pyfiglet import Figlet
import time
import sys

init(convert=None)

@click.command()
def cli():
    click.clear()
    while True:
        try:
            now = datetime.datetime.now()
            try:
                fig = Figlet(font='future')
            except:
                fig = Figlet(font='future_1')
            click.echo(Fore.LIGHTCYAN_EX + fig.renderText(str(now)))
            time.sleep(0.2)
            click.clear()
        except KeyboardInterrupt:
            click.echo(Fore.LIGHTRED_EX + 'exiting.')
            sys.exit(-1)



