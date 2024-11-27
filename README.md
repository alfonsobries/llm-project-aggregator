# LLM Project Aggregator

`project-aggregator.py` is a Python script that aggregates all the relevant files in your project into a single file, excluding hidden files, git-ignored files, and binary files. This aggregated file is ideal for sharing or feeding into an AI prompt.

## Features

- **Aggregates project files into one file**
- **Excludes hidden, git-ignored, and binary files**
- **Automatically generates an introduction and index**
- **Ideal for AI analysis or code review**
- **Allows specifying output file name and project directory**

## Installation

Clone the repository:

```bash
git clone https://github.com/alfonsobries/llm-project-aggregator.git
```

Navigate to the directory:

```bash
cd llm-project-aggregator
```

Make the script executable (optional):

```bash
chmod +x project-aggregator.py
```

## Usage

Run the script from any directory, specifying the project directory and output file if needed:

```bash
python project-aggregator.py -d /path/to/project -o /path/to/output.txt
```

Or if you made it executable:

```bash
./project-aggregator.py -d /path/to/project -o /path/to/output.txt
```

### Options

- `-d`, `--directory`: The directory of the project to aggregate. Defaults to the current directory.
- `-o`, `--output`: The output file path and name. Defaults to `aggregated_project.txt` in the current directory.

### Examples

- **Aggregate the current directory and use the default output file:**

```bash
python project-aggregator.py
```

- **Specify a project directory and output file:**

```bash
python project-aggregator.py -d /path/to/project -o /path/to/output.txt
```

- **Using the script as a global command:**

```bash
project-aggregator -d /path/to/project -o /path/to/output.txt
```

## Output

The `aggregated_project.txt` file (or the specified output file) will have the following structure:

- **Introduction:** Brief description and instructions.
- **Index:** Numbered list of all included files.
- **File Contents:** Each file's content separated by clear headers.

### Example Output Structure

```
Introduction:
This file contains the aggregated content of the project files.
Please review the code and provide any suggestions for improvement.

Index:
1. main.py
2. utils/helpers.py
3. README.md

==================================================
=== 1. main.py ===
==================================================

# Contents of main.py

==================================================
=== 2. utils/helpers.py ===
==================================================

# Contents of helpers.py

...
```

## Adding as a Global Command

To use `project-aggregator.py` as a global command:

1. **Move the script to a directory in your PATH:**

For Unix/Linux systems, you can move the script to `/usr/local/bin`:

```bash
sudo mv project-aggregator.py /usr/local/bin/project-aggregator
```

2. **Ensure it has execute permissions:**

```bash
sudo chmod +x /usr/local/bin/project-aggregator
```

3. **Run from anywhere:**

Now you can run the script from any directory:

```bash
project-aggregator -d /path/to/project -o /path/to/output.txt
```

## How It Works

- **File Selection:**
  - Uses `git ls-files` to get a list of tracked and unignored files in the specified directory.
  - Skips hidden files and directories (those starting with `.`).
  - Excludes binary files based on MIME type detection.

- **Content Aggregation:**
  - Reads each file's content using UTF-8 encoding.
  - Collects file paths and contents for index and aggregation.

- **Output Generation:**
  - Writes an introduction and index at the beginning of the output file.
  - Separates each file's content with clear headers and separators.

## Dependencies

- **Python 3**
- **Git**

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is in the public domain. Feel free to use it as you see fit.
