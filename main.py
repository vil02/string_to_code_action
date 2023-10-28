import os

from string_to_code import string_to_code


def _prepare_output_str(output_name, output_value):
    return "\n".join([f"{output_name}<<EOF", output_value, "EOF\n"])


def _set_output(output_name, output_value):
    with open(
        os.path.abspath(os.environ["GITHUB_OUTPUT"]), mode="a", encoding="utf-8"
    ) as _:
        _.write(_prepare_output_str(output_name, output_value))

def _save_code(file_name, code):
    with open(file_name, mode="a", encoding="utf-8") as _:
        _.write(code)


def main():
    target_language = os.environ["INPUT_TARGETLANGUAGE"]

    assert target_language in string_to_code.get_target_languages()
    code = string_to_code.proc(target_language, os.environ["INPUT_INPUTSTR"])

    _set_output("targetLanguage", target_language)
    _set_output("code", code)
    _save_code(os.environ["INPUT_OUTPUTFILE"], code)


if __name__ == "__main__":
    main()
