import React from 'react';
import github from './../../github.svg';
import './index.css';

const Header = () => (
  <div className="header">
    <div className="header--container">
      <div className="container--name">
        <a href="/">Explore GitHub</a>
      </div>
      <div className="container--logo right">
        <a href="https://github.com/kshvmdn/explore-github" title="GitHub">
          <img src={github} alt="logo" />
        </a>
      </div>
    </div>
  </div>
);

export default Header;
