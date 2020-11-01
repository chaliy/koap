import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

import DemoManifest from './demo/manifest.json'

const apis = (window.API_MANIFEST === '__API_MANIFEST__')
  ? DemoManifest.apis // Demo mode!
  : window.API_MANIFEST.apis; // Groups injected to index page

ReactDOM.render(
  <App apis={apis} />,
  document.getElementById('root')
);

