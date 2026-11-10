#!/usr/bin/env python3
"""Independent checker for the synthetic practice. No third-party dependencies."""
import argparse
import csv
import json
from pathlib import Path


def verify(jobs_path, schedule_path, maintenance):
    with open(jobs_path, newline='', encoding='utf-8-sig') as f:
        jobs = list(csv.DictReader(f))
    if not jobs:
        raise ValueError('jobs must not be empty')
    ids = set()
    for job in jobs:
        ident = job['job_id']
        if not ident or ident in ids:
            raise ValueError('empty or duplicate job_id')
        ids.add(ident)
        for key in ('release', 'duration', 'due', 'weight'):
            job[key] = int(job[key])
        if job['family'] not in ('A', 'B'):
            raise ValueError('unknown family')
        if min(job['release'], job['due']) < 0 or min(job['duration'], job['weight']) <= 0:
            raise ValueError('invalid job values')
    rows = json.loads(Path(schedule_path).read_text(encoding='utf-8'))
    if not isinstance(rows, list):
        raise ValueError('schedule must be a JSON array')
    scheduled = {}
    intervals = {'M1': [], 'M2': []}
    for row in rows:
        ident, machine, start, end = (row[k] for k in ('job_id', 'machine', 'start', 'end'))
        if ident not in ids or ident in scheduled:
            raise ValueError('unknown or duplicate scheduled job')
        if machine not in intervals or type(start) is not int or type(end) is not int:
            raise ValueError('invalid machine/time')
        scheduled[ident] = row
        intervals[machine].append((start, end, ident))
    if set(scheduled) != ids:
        raise ValueError('every valid job must be scheduled exactly once')
    score = 0
    for job in jobs:
        row = scheduled[job['job_id']]
        m, s, e = row['machine'], row['start'], row['end']
        if s < job['release'] or e - s != job['duration']:
            raise ValueError('release/duration violation: ' + job['job_id'])
        if m == 'M2' and job['family'] != 'A':
            raise ValueError('machine compatibility violation')
        if m == 'M1' and s < maintenance[1] and e > maintenance[0]:
            raise ValueError('maintenance overlap: ' + job['job_id'])
        score += job['weight'] * max(0, e - job['due'])
    for entries in intervals.values():
        entries.sort()
        for left, right in zip(entries, entries[1:]):
            if left[1] > right[0]:
                raise ValueError('job overlap')
    return {'feasible': True, 'weighted_tardiness': score, 'jobs': len(jobs),
            'maintenance': list(maintenance), 'optimality': 'not checked'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('schedule', help='JSON array: job_id, machine, start, end')
    parser.add_argument('--jobs', default=str(Path(__file__).resolve().parents[1] / 'practice/data/jobs.csv'))
    parser.add_argument('--maintenance', nargs=2, type=int, default=[40, 60], metavar=('START', 'END'))
    args = parser.parse_args()
    try:
        if not 0 <= args.maintenance[0] < args.maintenance[1]:
            raise ValueError('invalid maintenance interval')
        print(json.dumps(verify(args.jobs, args.schedule, args.maintenance), ensure_ascii=False))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, 'INVALID: ' + str(exc) + '\n')
