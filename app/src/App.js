import React, { Component } from 'react';
import { Router, Route, browserHistory } from 'react-router';

import Header from './components/Header';
import Footer from './components/Footer';

import Home from './containers/Home';
import Repository from './containers/Repository';

class App extends Component {
  render() {
    return (
      <div className="app">
        <Header />
        <Router history={browserHistory}>
          <Route path="/" component={Home} />
          <Route path="/:owner/:repo" component={Repository} />
          <Route path="*" component={Home} />
        </Router>
        <Footer />
      </div>
    );
  }
}

export default App;
