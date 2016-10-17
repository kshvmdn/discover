## explore-github

### Setup

##### Requirements:

  - Python 3+
  - Redis
  - Node.js (for development)

##### Installation

- Clone project.

  ```sh
  git clone https://git@github.com/kshvmdn/explore-github.git
  cd explore-github
  ```

- Install dependencies.

  ```sh
  pip install -r ./server/requirements.txt
  cd app && npm install && cd ..
  ```

### Usage

- You'll need to be running the server, front-end application, and Redis separately. I recommend [tmux](https://tmux.github.io/) / [iTerm 2](https://www.iterm2.com/), but multiple terminal windows will work just as well.

- Start Redis.

  ```sh
  $ redis-server # add --daemonize yes to run Redis in the background
  ```

- Start the Flask server. It'll be running on port 3001. Refer to [this](#api)for the API reference.

  ```sh
  $ DEBUG=<True|False> ./server/app.py
  ```

- Start the React application. It'll be running on port 3000.

  ```sh
  cd app && npm start
  ```

#### API

- __`/api/1.0/{owner}/{repo}`__
  + Return a list of repositories starred by stargazers of the repository provided. Will return a maximum of 200 stargazers by 100 repositories (i.e. 20k repos).

### Contribute

This project is completely open source. Feel free to [open an issue](#issue) for bugs/requests or [submit a pull request](#pr) for code contributions.

### License

[MIT](LICENSE) © [Kashav Madan](http://kshvmdn.com).
