import React from 'react';
import './index.css';

const PageHead = ({ children }) => (
  <div className="pagehead">
    <div className="pagehead--container">
      {children}
    </div>
  </div>
);

export default PageHead;
