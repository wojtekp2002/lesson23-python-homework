"""Program do prostej analizy tekstu podanego przez użytkownika."""

from __future__ import annotations

import re
import string
from collections import Counter


WORD_PATTERN = re.compile(r"[^\W\d_]+", re.UNICODE)
SENTENCE_ENDINGS = ".!?"


def extract_words(text: str) -> list[str]:
    """Zwraca słowa bez znaków interpunkcyjnych, zapisane małymi literami."""
    return WORD_PATTERN.findall(text.lower())


def count_characters_without_spaces(text: str) -> int:
    """Liczy znaki z pominięciem białych znaków, nie tylko zwykłej spacji."""
    return sum(1 for char in text if not char.isspace())


def analyze_text(text: str) -> dict[str, object]:
    """Zwraca statystyki wymagane w zadaniu domowym."""
    words = extract_words(text)
    word_counter = Counter(words)
    max_count = max(word_counter.values(), default=0)
    most_common_words = sorted(
        word for word, count in word_counter.items() if count == max_count
    )

    return {
        "characters_with_spaces": len(text),
        "characters_without_spaces": count_characters_without_spaces(text),
        "word_count": len(words),
        "sentence_count": sum(1 for char in text if char in SENTENCE_ENDINGS),
        "longest_word": max(words, key=len, default=""),
        "most_common_words": most_common_words,
        "most_common_count": max_count,
    }


def print_statistics(stats: dict[str, object]) -> None:
    """Wyświetla statystyki w czytelnej formie."""
    most_common_words = stats["most_common_words"]
    common_text = ", ".join(most_common_words) if most_common_words else "brak"

    print("\nStatystyki tekstu:")
    print(f"Liczba znaków (ze spacjami): {stats['characters_with_spaces']}")
    print(f"Liczba znaków (bez spacji): {stats['characters_without_spaces']}")
    print(f"Liczba słów: {stats['word_count']}")
    print(f"Liczba zdań: {stats['sentence_count']}")
    print(f"Najdłuższe słowo: {stats['longest_word'] or 'brak'}")
    print(
        "Najczęściej występujące słowo/słowa: "
        f"{common_text} ({stats['most_common_count']} razy)"
    )


def main() -> None:
    print("Analiza tekstu")
    text = input("Podaj tekst do analizy: ")
    print_statistics(analyze_text(text))


if __name__ == "__main__":
    main()
