import argparse
import json
import csv
import os
from gain_the_right_words import get_top_words_selected_part_of_speech


def output_file(file, format_file='csv'):
    with open('output_file.' + format_file, 'w', encoding='utf-8') as file_to_write:
        if format_file == 'csv':
            writer = csv.writer(file_to_write)
            writer.writerow(["name file", "count"])
            for key, value in file.items():
                writer.writerow([key, value])
        elif format_file == 'json':
            json.dump(file, file_to_write)
        else:
            file_to_write.write(file)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="str: download this url")
    parser.add_argument("count", help="int: count of words")
    parser.add_argument("item", help="var or def or noun or verb")
    parser.add_argument("format_file", help="json or csv format")
    parser.add_argument("directory", help="output file destination")
    args = parser.parse_args()
    parser.parse_args()
    most_common_words = get_top_words_selected_part_of_speech(searched_item=args.item,
                                                              top_size=int(args.count), git_url=args.url,
                                                              directory=args.directory)
    print("Cлова найдены")
    output_file(file=dict(most_common_words), format_file=args.format_file)
    print("Файлы созданы")
    os.remove("temporary.txt")
