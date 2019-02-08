import subprocess


def bash(cmd, **kwargs):
    std_kwargs = dict(
        encoding='utf-8',
        capture_output=True,
        check=True)
    if isinstance(cmd, str):
        cmd = cmd.strip()
    std_kwargs.update(kwargs)
    return subprocess.run(cmd, **std_kwargs).stdout.rstrip('\n')


def ls(path=None, flags=None, **kwargs):
    return bash('ls {} {}'.format(flags2str(flags), path or ''))


def pwd(flags=None, **kwargs):
    return bash('pwd {}'.format(flags2str(flags)))


def flags2str(flags):
    if isinstance(flags, str):
        if not flags.startswith('-') and flags:
            flags = '-' + flags
        return flags
    elif isinstance(flags, (list, tuple)):
        if isinstance(flags, tuple):
            flags = list(flags)
        return '-' + ''.join(flags)
    elif flags is None:
        return ''
    else:
        raise ValueError('Unable to convert flags to str.')
