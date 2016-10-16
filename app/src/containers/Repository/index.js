import React, { Component } from 'react';
import axios from 'axios';

import './index.css';
import PageHead from './../../components/PageHead';

const BASE_URL = 'http://0.0.0.0:3001/api/1.0'

class Repository extends Component {
  constructor() {
    super();

    this.state = {
      owner: '',
      repo: '',
      results: []
    };
  }

  componentDidMount() {
    this.setState({
      owner: this.props.params.owner,
      repo: this.props.params.repo
    }, () => {
      let { owner, repo } = this.state;
      let url = `${BASE_URL}/${owner}/${repo}`;

      axios.get(url)
        .then(results => this.setState({ results }))
        .catch(err => console.error(err));
    });
  }

  render() {
    console.log(this.state.results)
    let {owner, repo, results} = this.state
    return (
      <div className="app--body">
        <PageHead>
          <h1 className="body--repository">
            <a href={`https://github.com/${owner}`} className="repository--owner">{owner}</a>
            &nbsp;<span className="repository--path-divider">/</span>&nbsp;
            <a href={`https://github.com/${owner}/${repo}`} className="repository--name">{repo}</a>
          </h1>
        </PageHead>
      </div>
    );
  }
}

export default Repository;
