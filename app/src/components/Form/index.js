import React, { Component } from 'react';

import './index.css';
import './../../media/btn.css';

class Form extends Component {
  constructor() {
    super();

    this.state = {
      repo: '',
      owner: ''
    };
  }

  get owner() {
    if (this.state.owner.trim().length > 0) {
      return (<span className='dark'>{this.state.owner}</span>)
    }

    return (<span className='light'>owner</span>);
  }

  get repo() {
    if (this.state.repo.trim().length > 0) {
      return (<span className='dark'>{this.state.repo}</span>)
    }

    return (<span className='light'>repo</span>);
  }

  handleClick() {
    let { owner, repo } = this.state;

    if (!(owner && repo)) {
      return;
    }

    location.pathname = `/${owner}/${repo}`;
  }

  handleKeyPress(target) {
    if (target.charCode === 13) {
      this.handleClick();
    }
  }

  render() {
    return (
      <div className="repoform">
        <div className="repoform--out">
          <p>https://github.com/{this.owner}/{this.repo}</p>
        </div>
        <div className="repoform--in">
          <input
            type="text"
            placeholder="owner"
            onChange={(e) => this.setState({owner: e.target.value.trim()})}
          />
          <input
            type="text"
            placeholder="repo"
            onChange={(e) => this.setState({repo: e.target.value.trim()})}
            onKeyPress={this.handleKeyPress.bind(this)}
          />
          <input
            type="button"
            className="btn btn-primary"
            value="Go"
            onClick={this.handleClick.bind(this)}
          />
        </div>
      </div>
    );
  }
}

export default Form;
