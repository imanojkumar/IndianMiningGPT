"""
IndianMiningGPT
Phase 8.1
Interactive CLI Assistant
"""

from pathlib import Path
import sys

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parents[2]
)

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from src.rag.pipeline import (
    IndianMiningGPT
)


def print_banner():

    print(
        "\n"
        + "=" * 70
    )

    print(
        "IndianMiningGPT"
    )

    print(
        "Mining Regulations & Compliance Assistant"
    )

    print(
        "=" * 70
    )

    print(
        "\nType 'exit' to quit\n"
    )


def main():

    print_banner()

    bot = IndianMiningGPT()

    while True:

        try:

            query = input(
                "\nQuestion > "
            ).strip()

            if not query:
                continue

            if query.lower() in [
                "exit",
                "quit",
                "q"
            ]:

                print(
                    "\nGoodbye.\n"
                )

                break

            print(
                "\nSearching corpus..."
            )

            result = bot.ask(
                query
            )

            print(
                "\n"
                + "=" * 70
            )

            print(
                "ANSWER\n"
            )

            print(
                result["answer"]
            )

            print(
                "\n"
                + "=" * 70
            )

        except KeyboardInterrupt:

            print(
                "\n\nInterrupted."
            )

            break

        except Exception as e:

            print(
                "\nERROR:"
            )

            print(
                str(e)
            )


if __name__ == "__main__":

    main()
