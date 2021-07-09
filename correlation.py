import json
from math import sqrt


def load_journal(fname):
    with open(fname, "r") as f:
        data=json.load(f)
    return data


def compute_phi(fname, event):
    l = load_journal(fname)
    n00 = n01 = n11 = n10 = nx1 = nx0 = n1x = n0x = 0
    for day in l:
        if event in day['events']:
            if day['squirrel'] == True:
                n11 += 1
            else:
                n10 += 1
        elif day['squirrel'] == True:
            n01 += 1
        else:
            n00 += 1
    nx0 = n00 + n10
    nx1 = n01 + n11
    n1x = n10 + n11
    n0x = n00 + n01
    return (n11 * n00 - n10 * n01) / sqrt(n1x * n0x * nx1 * nx0)


def compute_correlations(fname):
    l = load_journal(fname)
    events = []
    for day in l:
        events = list(set(events + day['events']))
    corr = {}
    for event in events:
        corr.update({event: compute_phi(fname, event)})
    return corr


def diagnose(fname):
    corr = compute_correlations(fname)

    values = list(corr.values())
    keys = list(corr.keys())
    l = []
    l.append(keys[values.index(max(values))])
    l.append(keys[values.index(min(values))])
    return l

