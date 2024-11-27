#!/usr/bin/env python3

import os
import sys
import subprocess
import mimetypes
import argparse

def is_binary_file(path):
    mime_type, _ = mimetypes.guess_type(path)
    if mime_type:
        return not mime_type.startswith('text/')
    else:
        return False

def get_valid_files(directory):
    # Use git to get a list of tracked and unignored files
    try:
        result = subprocess.check_output(
            ['git', 'ls-files'],
            cwd=directory,
            stderr=subprocess.STDOUT
        )
        files = result.decode('utf-8').split('\n')
        files = [f for f in files if f]  # Remove empty strings
        return files
    except subprocess.CalledProcessError:
        print("Error executing 'git ls-files'. Ensure this is a git repository.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Aggregate project files into a single file.')
    parser.add_argument('-d', '--directory', type=str, default=os.getcwd(),
                        help='The directory of the project (default: current directory)')
    parser.add_argument('-o', '--output', type=str, default='aggregated_project.txt',
                        help='The output file path and name (default: aggregated_project.txt)')
    args = parser.parse_args()

    project_dir = os.path.abspath(args.directory)
    output_filename = args.output

    valid_files = get_valid_files(project_dir)

    # Collect file information for the index
    file_info_list = []

    # Collect file contents
    file_contents = []

    for idx, relative_path in enumerate(valid_files, 1):
        # Ignore hidden files
        if '/.' in relative_path or relative_path.startswith('.'):
            continue

        absolute_path = os.path.join(project_dir, relative_path)

        # Ignore binary files
        if is_binary_file(absolute_path):
            continue

        try:
            with open(absolute_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            file_info_list.append(f"{idx}. {relative_path}")
            file_contents.append({
                'index': idx,
                'path': relative_path,
                'content': content
            })
        except Exception as e:
            print(f"Could not read file {relative_path}: {e}")
            continue

    # Write to the output file
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        # Write the introduction
        output_file.write("Introduction:\n")
        output_file.write("This file contains the aggregated content of the project files.\n")
        output_file.write("Please review the code and provide any suggestions for improvement.\n\n")

        # Write the index
        output_file.write("Index:\n")
        for file_info in file_info_list:
            output_file.write(f"{file_info}\n")
        output_file.write("\n")

        # Write the file contents
        for file_data in file_contents:
            output_file.write("=" * 50 + "\n")
            output_file.write(f"=== {file_data['index']}. {file_data['path']} ===\n")
            output_file.write("=" * 50 + "\n\n")
            output_file.write(file_data['content'])
            output_file.write("\n\n")

    print(f"Aggregated file generated successfully: {output_filename}")

if __name__ == '__main__':
    main()
