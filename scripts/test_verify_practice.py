"""Run with: python3 -m unittest discover -s scripts -p 'test_*.py'"""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from verify_practice import verify

ROOT = Path(__file__).resolve().parents[1]


class PracticeCheckerTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name) / 'schedule.json'
        self.jobs = ROOT / 'practice/data/jobs.csv'
        self.rows = [dict(job_id=j, machine=m, start=s, end=e) for j, m, s, e in [
            ('J1', 'M2', 40, 70), ('J2', 'M1', 0, 25), ('J3', 'M2', 10, 30),
            ('J4', 'M1', 25, 40), ('J5', 'M2', 30, 40), ('J6', 'M1', 60, 80)]]

    def check(self, rows, maintenance=(40, 60)):
        self.output.write_text(json.dumps(rows))
        return verify(self.jobs, self.output, maintenance)

    def test_valid_boundary_and_score(self):
        self.assertEqual(self.check(self.rows)['weighted_tardiness'], 30)

    def test_changed_maintenance_invalidates_old_schedule(self):
        with self.assertRaises(ValueError):
            self.check(self.rows, (20, 60))

    def test_missing_and_duplicate_jobs(self):
        for rows in (self.rows[:-1], self.rows + [self.rows[0]]):
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                self.check(rows)

    def test_overlap(self):
        rows = copy.deepcopy(self.rows)
        rows[0].update(start=30, end=60)
        with self.assertRaisesRegex(ValueError, 'overlap'):
            self.check(rows)

    def test_compatibility_release_duration_and_types(self):
        for index, change in [(1, {'machine': 'M2'}), (2, {'start': 0, 'end': 20}),
                              (0, {'end': 71}), (0, {'start': True})]:
            rows = copy.deepcopy(self.rows)
            rows[index].update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.check(rows)

    def test_invalid_job_data(self):
        original = self.jobs.read_text()
        for content in (original.replace('J1,A,0,30', 'J1,A,0,0'),
                        original.replace('J2,B', 'J1,B'),
                        original.replace('J1,A', 'J1,C')):
            self.jobs = Path(self.temp.name) / 'jobs.csv'
            self.jobs.write_text(content)
            with self.subTest(content=content), self.assertRaises(ValueError):
                self.check(self.rows)


if __name__ == '__main__':
    unittest.main()
