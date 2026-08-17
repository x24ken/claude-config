#!/usr/bin/env python3
"""Statusline: Braille dots gauge + git info"""
import json, sys, subprocess, os
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

data = json.load(sys.stdin)

BRAILLE = ' ⣀⣄⣤⣦⣶⣷⣿'
R = '\033[0m'
DIM = '\033[2m'
BOLD = '\033[1m'
GREEN = '\033[38;2;80;200;80m'
YELLOW = '\033[38;2;212;193;0m'
RED = '\033[38;2;255;80;60m'
CYAN = '\033[38;2;100;200;255m'

def gradient(pct):
    if pct < 50:
        r = int(pct * 5.1)
        return f'\033[38;2;{r};200;80m'
    else:
        g = int(200 - (pct - 50) * 4)
        return f'\033[38;2;255;{max(g, 0)};60m'

def braille_bar(pct, width=8):
    pct = min(max(pct, 0), 100)
    level = pct / 100
    bar = ''
    for i in range(width):
        seg_start = i / width
        seg_end = (i + 1) / width
        if level >= seg_end:
            bar += BRAILLE[7]
        elif level <= seg_start:
            bar += BRAILLE[0]
        else:
            frac = (level - seg_start) / (seg_end - seg_start)
            bar += BRAILLE[min(int(frac * 7), 7)]
    return bar

def fmt(label, pct):
    p = round(pct)
    return f'{DIM}{label}{R} {gradient(pct)}{braille_bar(pct)}{R} {p}%'

def run_git(*args):
    try:
        result = subprocess.run(
            ['git'] + list(args),
            capture_output=True, text=True, timeout=3,
            cwd=data.get('cwd', os.getcwd())
        )
        return result.stdout.strip() if result.returncode == 0 else None
    except Exception:
        return None

def git_info():
    git_dir = run_git('rev-parse', '--git-dir')
    if git_dir is None:
        return None
    common_dir = run_git('rev-parse', '--git-common-dir')
    if git_dir and common_dir and os.path.realpath(git_dir) != os.path.realpath(common_dir):
        return '🌲'
    return None

def compact_path(p):
    if not p:
        return None
    home = os.path.expanduser('~')
    if p == home:
        return '~'
    if p.startswith(home + os.sep):
        return '~' + p[len(home):]
    return p

# Build output
sections = []

git = git_info()
if git:
    sections.append(git)

ctx = data.get('context_window', {}).get('used_percentage')
if ctx is not None:
    sections.append(fmt('ctx', ctx))

five = data.get('rate_limits', {}).get('five_hour', {}).get('used_percentage')
if five is not None:
    sections.append(fmt('5h', five))

week = data.get('rate_limits', {}).get('seven_day', {}).get('used_percentage')
if week is not None:
    sections.append(fmt('7d', week))

proj_dir = compact_path(data.get('workspace', {}).get('project_dir'))
if proj_dir:
    sections.append(f'{CYAN}{proj_dir}{R}')

print(f' {DIM}│{R} '.join(sections), end='')
