import argparse
import asyncio

from pathlib import Path

from conventor import Conventor


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'input_path', 
        type=str, 
        help='YAML path to process'
    )
    parser.add_argument(
        'output_dir', 
        type=str, 
        help='Path to dump output RST files'
    )

    arguments = parser.parse_args()

    conventor = Conventor(Path(arguments.input_path))
    conventor.process(Path(arguments.output_dir))

