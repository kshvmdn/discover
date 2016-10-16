import React, { Component } from 'react';

import './index.css'
import PageHead from './../../components/PageHead';
import RepoForm from './../../components/RepoForm';

class Home extends Component {
  render() {
    return (
      <div className="app--body">
        {/* <PageHead>
          <h1>Welcome.</h1>
          <h3>Begin by entering a repository.</h3>
        </PageHead> */}
        <div className="body--content">
          <RepoForm/>
        </div>
      </div>
    );
  }
}

export default Home;
