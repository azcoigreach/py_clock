#!/bin/env python
import click
import datetime
from pyfiglet import Figlet
import time
import sys

@click.command()
def cli():
    click.clear()
    while True:
        try:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            try:
                fig = Figlet(font='future')
            except:
                fig = Figlet(font='future_1')

            click.echo(click.style(fig.renderText(str(now)),fg='cyan'))
            time.sleep(1)
            click.clear()
        except KeyboardInterrupt:
            click.echo(click.style('exiting.', fg='red'))
            sys.exit(-1)



