import React, { Component } from 'react';

import './index.css';
import Repo from './../Repo';

class Results extends Component {
  constructor() {
    super();

    this.state = {
      repos: []
    };
  }

  componentDidMount() {
    this.setState({ repos: this.props.response.data.data })
  }

  render() {
    return (
      <div className="app--results">
        {this.state.repos.map((repo, i) => (
          <Repo key={i} repo={repo}/>
        ))}
      </div>
    );
  }
}

export default Results;
