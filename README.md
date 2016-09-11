## explore-github

> Explore GitHub repositories.

### Installation

- Clone repository.

  ```sh
  $ git clone https://github.com/kshvmdn/explore-github.git && cd $_ && pip install -r ./requirements.txt
  ```

- [Create new developer application](https://github.com/settings/developers) (for Client ID / Client Secret - you can use the app w/o these, but the 60 requests / hr generally isn't enough).

### Usage

- Start server & application (all runtime variables are completely optional).

  ```sh
   PORT=<port> HOST=<host> DEBUG=<debug> CLIENT_ID=<client_id> CLIENT_SECRET=<client_secret> ./app.py
  ```

- Should be running at the specified host/port (default is [`http://0.0.0.0:3000`](http://0.0.0.0:3000)).

- Access the API at `/api/<owner>/<repo>` (this is the only endpoint right now), response should look something like this:

  ```js
  {
    data: [
      ...,
      {
        id: Number,
        name: String,
        owner: String,
        slug: String,
        description: String,
        stargazers_count: Number,
        watchers_count: Number,
        fork_count: Number,
        language: String,
        starred_by: [String],
        count: Number
      }
    ],
    meta: {
      message: String,
      status: Number
    }
  }
  ```

### Contribute

This project is completely open source. Feel free to open an [issue](https://github.com/kshvmdn/github-list/issues) or submit a [pull request](https://github.com/kshvmdn/github-list/pulls). :smile:

Before submitting a PR, please ensure:

  - Python complies with [PEP 8](https://www.python.org/dev/peps/pep-0008/)
  - JavaScript complies with [Standard](https://github.com/feross/standard)
  - You've recompiled CSS (if applicable), you can do this with:

    ```sh
    $ sass static/styles/main.scss:static/styles/main.css
    ```

### License

MIT © [Kashav Madan](http://kshvmdn.com).
