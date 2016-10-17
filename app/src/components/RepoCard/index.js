import React, { Component } from 'react';

import './index.css';
import github from './../../media/github.svg';
import star from './../../media/star.svg';
import colours from './../../media/colors.json';

class RepoCard extends Component {
  constructor() {
    super();
    this.state = {}
  }

  render() {
    let {repo} = this.props;
    repo.slug = `${repo.owner}/${repo.name}`
    repo.color = colours.hasOwnProperty(repo.language) ? colours[repo.language].color : '#000';

    console.log(repo);
    return (
      <div className="results--repo">
        <div className="repo--name">
          <a href={`/${repo.slug}`}>{repo.slug}</a> ({repo.count})
        </div>
        <div className="repo--desc">{repo.description}</div>
        <div className="repo--meta">
          <div className="repo--lang" style={{color: repo.color}}>{repo.language}</div>
          <div className="repo--icons">
            <div className="repo--stargazercount">
              <img src={star} alt=""/> {repo.stargazers}
            </div>
            <div className="repo--link">
              <a href={`https://github.com/${repo.slug}`} target="_blank"><img src={github} alt="GitHub"/></a>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default RepoCard;
