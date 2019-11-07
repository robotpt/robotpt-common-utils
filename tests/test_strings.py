import unittest

from robotpt_common_utils import strings


class TestStrings(unittest.TestCase):

    def test_generate_random_string(self):

        length = 8
        for _ in range(100):
            str1 = strings.random_string(length)
            str2 = strings.random_string(length)
            for s in [str1, str2]:
                self.assertEqual(
                    length,
                    len(s),
                )
            self.assertNotEqual(
                str1, str2
            )

    def test_wildcard_search_list(self):

        pattern = 'abc'
        true_solutions = ['abc']
        not_solutions = ['abcde', 'dabc', 'a', 'ab', 'adef', 'abd', '', 'none']
        results = strings.wildcard_search_in_list(pattern, true_solutions + not_solutions)
        for s in true_solutions:
            self.assertTrue(
                s in results
            )
        for s in not_solutions:
            self.assertFalse(
                s in results
            )

        pattern = 'abc*'
        true_solutions = ['abc', 'abcde']
        not_solutions = ['dabc_', 'a_', 'ab', 'adef', 'abd', '', 'none']
        results = strings.wildcard_search_in_list(pattern, true_solutions + not_solutions)
        for s in true_solutions:
            self.assertTrue(
                s in results
            )
        for s in not_solutions:
            self.assertFalse(
                s in results
            )

        pattern = '*abc'
        true_solutions = ['abc', 'deabc']
        not_solutions = ['abcd', 'a', 'ab', 'adef', 'abd', '', 'none']
        results = strings.wildcard_search_in_list(pattern, true_solutions + not_solutions)
        for s in true_solutions:
            self.assertTrue(
                s in results
            )
        for s in not_solutions:
            self.assertFalse(
                s in results
            )

        pattern = 'abc*e'
        true_solutions = ['abce', 'abcde', 'abcddddde']
        not_solutions = ['abcdef', 'abcdddddef', 'a', 'ab', 'adef', 'abd', '', 'none']
        results = strings.wildcard_search_in_list(pattern, true_solutions + not_solutions)
        for s in true_solutions:
            self.assertTrue(
                s in results
            )
        for s in not_solutions:
            self.assertFalse(
                s in results
            )

        pattern = 'abc*e*f'
        true_solutions = ['abcef', 'abcdef', 'abcdddddeeeeeeef']
        not_solutions = ['abcdefg', 'abcdddddefg', 'a', 'ab', 'adef', 'abd', '', 'none']
        results = strings.wildcard_search_in_list(pattern, true_solutions + not_solutions)
        for s in true_solutions:
            self.assertTrue(
                s in results
            )
        for s in not_solutions:
            self.assertFalse(
                s in results
            )

    def test_bad_entry_to_wildcard_match(self):
        special_chars = [
            '^', '$', '.', '+', '?', '{', '}', '/', '\\',
            '|', '[', ']', '(', ')', ':', '<', '>', '*'
        ]
        for i in range(1, len(special_chars)):
            wildcard = special_chars[i]
            text = 'text' + wildcard
            search_str = 'textfoo'
            self.assertTrue(
                strings.is_wildcard_match(
                    text,
                    search_str,
                    wildcard
                )
            )
            self.assertRaises(
                ValueError,
                strings.is_wildcard_match,
                special_chars[i-1],
                text,
                wildcard
            )

