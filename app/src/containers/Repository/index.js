import React, { Component } from 'react';
import axios from 'axios';

import './index.css';
import ring from './../../media/ring.svg';
import PageHead from './../../components/PageHead';
import Results from './../../components/Results';

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
    let {owner, repo, results} = this.state

    if (results.length === 0) {
      return (
        <div className="app--body-loading">
          <img src={ring} className="body--loadingicon" alt="Loading"/>
        </div>
      );
    }

    return (
      <div className="app--body">
        <PageHead>
          <h1 className="body--repository">
            <a href={`https://github.com/${owner}`} className="repository--owner">{owner}</a>
            &nbsp;<span className="repository--path-divider">/</span>&nbsp;
            <a href={`https://github.com/${owner}/${repo}`} className="repository--name">{repo}</a>
          </h1>
        </PageHead>
        <div className="body--results">
          <Results response={results}/>
        </div>
      </div>
    );
  }
}

export default Repository;
