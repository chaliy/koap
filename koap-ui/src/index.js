import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

import DemoAPIGroups from './demo/apigroups.json'

const groups = (window.API_GROUPS === '__API_GROUPS__')
  ? DemoAPIGroups.groups // Demo mode!
  : window.API_GROUPS.groups; // Groups injected to index page

ReactDOM.render(
  <App apiGroups={apiGroups} />,
  document.getElementById('root')
);

