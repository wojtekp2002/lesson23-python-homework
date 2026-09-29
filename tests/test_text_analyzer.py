import unittest

from src.text_analyzer import analyze_text, extract_words


class TextAnalyzerTest(unittest.TestCase):
    def test_extract_words_ignores_punctuation_and_case(self):
        self.assertEqual(extract_words("Ala, ala! Kot?"), ["ala", "ala", "kot"])

    def test_analyze_text_returns_expected_statistics(self):
        stats = analyze_text("Ala ma kota. Ala lubi Python!")

        self.assertEqual(stats["characters_with_spaces"], 29)
        self.assertEqual(stats["characters_without_spaces"], 24)
        self.assertEqual(stats["word_count"], 6)
        self.assertEqual(stats["sentence_count"], 2)
        self.assertEqual(stats["longest_word"], "python")
        self.assertEqual(stats["most_common_words"], ["ala"])
        self.assertEqual(stats["most_common_count"], 2)

    def test_analyze_empty_text(self):
        stats = analyze_text("")

        self.assertEqual(stats["word_count"], 0)
        self.assertEqual(stats["sentence_count"], 0)
        self.assertEqual(stats["longest_word"], "")
        self.assertEqual(stats["most_common_words"], [])


if __name__ == "__main__":
    unittest.main()
