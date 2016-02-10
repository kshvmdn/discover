# GitHub List
Generate a list of a users' GitHub repositories in various formats, including `json`, `csv`, `markdown`, or `plaintext`.

## Usage
### Install

+ Clone project

    ```sh
    git clone http://github.com/kshvmdn/github-list && cd github-list
    ```

+ Install requirements

    ```sh
    pip install -r requirements.txt
    ```

### Run

+ Run `__main__.py` (Python 3!)

    ```sh
    $ python __main__.py [-h] [user1, user2, ...] [-f [<json|csv|md|raw.txt|tbl.txt|all>, ...]]
    $ python __main__.py kshvmdn -f all  # check ./out/kshvmdn for output
    ```

    Output format defaults to tbl.txt. At least one user is required.

+ Output types

    + json
    + csv
    + md (markdown)
    + raw.txt (raw plaintext)
    + tbl.txt (plaintext formatted as table)
    + [_sample output_](https://github.com/kshvmdn/github-list/tree/master/out/)

## Contribute
This project is completely open source; feel free to open an [issue](https://github.com/kshvmdn/github-list/issues) or make a [PR](https://github.com/kshvmdn/github-list/pulls).
