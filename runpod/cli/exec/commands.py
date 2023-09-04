'''
RunPod | CLI | Exec | Commands
'''

import click

from .functions import python_over_ssh
from ..utils.userspace import get_or_prompt_for_pod_id

@click.group('exec')
def exec_cli():
    '''A collection of CLI functions for Exec.'''

@exec_cli.command('python')
@click.option('--pod_id', default=None, help='The pod ID to run the command on.')
@click.argument('file', type=click.Path(exists=True), required=True)
def remote_python(pod_id, file):
    '''
    Runs a remote Python shell.
    '''
    if pod_id is None:
        pod_id = get_or_prompt_for_pod_id()

    click.echo('Running remote Python shell...')
    python_over_ssh(pod_id, file)