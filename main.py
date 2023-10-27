import os

from string_to_code import string_to_code


def _set_output(output_name, output_value):
    with open(
        os.path.abspath(os.environ["GITHUB_OUTPUT"]), mode="a", encoding="utf-8"
    ) as _:
        _.write(f"{output_name}=\"{output_value}\"")


def main():
    target_language = os.environ["INPUT_TARGETLANGUAGE"]

    assert target_language in string_to_code.get_target_languages()
    code = string_to_code.proc(target_language, os.environ["INPUT_INPUTSTR"])

    _set_output("targetLanguage", target_language)
    _set_output("code", "some_tmp_code")


if __name__ == "__main__":
    main()
