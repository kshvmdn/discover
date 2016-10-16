import React, { Component } from 'react';

import './index.css';

class Repo extends Component {
  constructor() {
    super();
    this.state = {}
  }

  render() {
    let {repo} = this.props;
    console.log(repo);
    return (
      <div className="results--repo">
      </div>
    );
  }
}

export default Repo;
