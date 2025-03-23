#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Create knowledge base from the docs data.

This script is used to create a knowledge base from the markdown docs data.
"""

import io
import os
import sys
import logging
import argparse

# エラー対策: 文字コード処理をすべて UTF-8 で行うように変更
# UnicodeDecodeError: 'cp932' codec can't decode byte 0x9d in position 433: illegal multibyte sequence
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

KNOWLEDGE_BASE = "knowledge-list.txt"
KNOWLEDGE_FILE_DIR = "docs"
KNOWLEDGE_OUTPUT_DIR = "enb"
KNOWLEDGE_FILE_PREFIX = "ENB_"
MAX_CHUNK_SIZE = 2048 * 4  # 8KB 1-char = 2byte


def create_knowledge_file(filename: str) -> None:
    """
    Create knowledge base from the markdown data.

    Args:
        filename: The filename of the markdown data.
    """
    print(f"> Creating knowledge file from {filename}")

    def split_file(filename: str) -> None:
        """
        Split the file into smaller files.

        Args:
            filename: The filename of the markdown data.
        """
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()
            data = data.split("\n")
            chunks = []
            current_size = 0
            chunk = ""
            main_title = ""
            cid_code = ""
            for chunk_index in range(len(data)):
                chunk += data[chunk_index] + "\n"
                if "cid:" in data[chunk_index]:
                    cid_code = data[chunk_index]
                    print(f"= CID code: {cid_code}")
                if data[chunk_index].startswith("# "):
                    main_title = data[chunk_index]
                    print(f"= {main_title}")
                if data[chunk_index].startswith("## "):
                    print(f"= {data[chunk_index]}")
                if data[chunk_index].startswith("### "):
                    print(f"= {data[chunk_index]}")
                if data[chunk_index] == "---":
                    # セパレータが見つかったら、セクションサイズの確認
                    current_size += len(chunk)
                    if current_size >= MAX_CHUNK_SIZE:
                        print(f"= Section size: {current_size}")
                        # セクションサイズが最大サイズを超えたら、チャンクを保存
                        chunks.append(chunk)
                        chunk = ""
                        current_size = 0
                        continue
            if chunk != "" and "#" in chunk:
                # チャンクが空でなく、タイトルが含まれている場合は、チャンクを保存
                chunks.append(chunk)

            if chunks:
                total = len(chunks)
                print(f"= Total chunks: {total}")
                for chunk_index in range(total):
                    chunk_filename = os.path.join(
                        KNOWLEDGE_OUTPUT_DIR,
                        f"{KNOWLEDGE_FILE_PREFIX}{os.path.basename(filename)}_{chunk_index}.md",
                    )
                    with open(chunk_filename, "w", encoding="utf-8") as chunk_file:
                        print(f"= Creating {chunk_filename}")
                        # title & cid code
                        if chunk_index != 0:
                            chunk_file.write(f"{main_title}-{chunk_index+1}/{total}\n")
                            (
                                chunk_file.write(f"\n{cid_code}\n")
                                if cid_code != ""
                                else None
                            )
                        # content
                        chunk_file.write(chunks[chunk_index])

    # Split the file into smaller files
    split_file(filename)
    return


def create_knowledge_base(knowledge_base_list: str) -> None:
    """
    Create knowledge file from the markdown data.

    Args:
        knowledge_base: The filename of the knowledge base.
    """
    with open(knowledge_base_list, "r") as file:
        print(f"> Reading knowledge base list from {knowledge_base_list}")
        data = file.read()
        data = data.split("\n")
        for i in range(len(data)):
            filename = os.path.join(KNOWLEDGE_FILE_DIR, data[i])
            if filename == "":
                continue
            if not os.path.isfile(filename):
                logging.error(f"File {filename} does not exist.")
                continue
            create_knowledge_file(filename)


def main() -> None:
    """
    Main function.
    """
    parser = argparse.ArgumentParser(
        description="Create knowledge base from the markdown docs data."
    )
    parser.add_argument(
        "-k",
        default=KNOWLEDGE_BASE,
        dest="knowledge_base",
        help="The filename of the knowledge base.",
    )
    parser.add_argument(
        "-d",
        default=KNOWLEDGE_FILE_DIR,
        dest="knowledge_file_dir",
        help="The directory of the markdown docs data.",
    )
    args = parser.parse_args()

    print("Knowledge base creation process started.")
    print(f"= Knowledge base: {args.knowledge_base}")
    print(f"= Knowledge file directory: {args.knowledge_file_dir}")

    create_knowledge_base(args.knowledge_base)

    print("Knowledge base creation process completed.")


if __name__ == "__main__":
    main()
