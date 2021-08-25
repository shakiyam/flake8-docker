import re
import subprocess
import unittest


class TestFlake8(unittest.TestCase):

    def do_test(self, filename: str):
        with open(filename, 'r') as f:
            lines = f.readlines()
        expectations = []
        for i, line in enumerate(lines):
            match = re.search(r'# *([A-Z]+[0-9]+ *,* *)*\n', line)
            if match:
                for expectation in re.split(r'\W+', match.group()[1:].strip()):
                    expectations.append((i + 1, expectation))
        result = subprocess.run(
            ['flake8', filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdout_lines = result.stdout.splitlines()
        self.assertEqual(result.stderr, b'', 'STDERR is not empty.')
        self.assertEqual(len(stdout_lines), len(expectations),
                         'Mismatch in number of outputs.')
        for i, (num, expectation) in enumerate(expectations):
            self.assertRegex(
                stdout_lines[i],
                f'{filename}:{num}:[0-9]+: {expectation}'.encode())

    def test_flake8_builtins(self):
        self.do_test('./test/example_flake8-builtins.py')

    def test_flake8_comprehensions(self):
        self.do_test('./test/example_flake8-comprehensions.py')

    def test_flake8_import_order(self):
        self.do_test('./test/example_flake8-import-order.py')

    def test_flake8_quotes(self):
        self.do_test('./test/example_flake8-quotes.py')

    def test_flake8_use_fstring(self):
        self.do_test('./test/example_flake8-use-fstring.py')

    def test_pep8_naming(self):
        self.do_test('./test/example_pep8-naming.py')


if __name__ == '__main__':
    unittest.main()
