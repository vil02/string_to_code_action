# `string_to_code_action`

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=vil02_string_to_code_action&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=vil02_string_to_code_action)
[![CodeFactor](https://www.codefactor.io/repository/github/vil02/string_to_code_action/badge)](https://www.codefactor.io/repository/github/vil02/string_to_code_action)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2d2282499b7c45d7b840baba70b7eb14)](https://app.codacy.com/gh/vil02/string_to_code_action/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

This GitHub Action utilizes the
[`string_to_code`](https://github.com/vil02/string_to_code_proj) Python package
to generate messy code that displays a given string.

## Inputs

- `targetLanguage` (optional): Language of the generated code.
   If set to `""` the resulting code will be in a randomly selected language.
   Default: `""`.
- `inputStr` (required): The string which should be displayed
   by the generated program.
- `outputFile` (optional): The file to store the generated code.
  Default: `"out.txt"`.

## Outputs

- `targetLanguage`: Language of the generated code.
- `code`: The generated messy code.

## Example Usage

```yaml
---
name: Generate Messy Code

on:
  workflow_dispatch:
  push:

jobs:
  generate_code:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Generate Messy Code
      id: generate_code
      uses: vil02/string_to_code_action
      with:
        targetLanguage: "python3"
        inputStr: "Hello, World!"
        outputFile: "generated_code.py"

    - name: Display Generated Code
      run: cat ${{ steps.generate_code.outputs.outputFile }}
...
```

In this example, the GitHub Action generates messy code in
the Python3 that displays the string `Hello, World!`.
The generated code is stored in the file `generated_code.py`
and then displayed using the `cat` command.
