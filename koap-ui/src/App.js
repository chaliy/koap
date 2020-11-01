import React from 'react';
import PropTypes from 'prop-types';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import SwaggerUI from "swagger-ui-react"
import "swagger-ui-react/swagger-ui.css"

import Drawer from '@material-ui/core/Drawer';
import CssBaseline from '@material-ui/core/CssBaseline';
import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles({
  app: {
    display: 'flex'
  },
  drawer: {
    width: 240,
    flexShrink: 0

  },
  drawerPaper: {
    width: 240
  },
  content: {
    flex: 2
  },
});

function App({ apis }) {
  const classes = useStyles();

  function Sidebar() {
    return <Drawer
      variant="permanent"
      anchor="left"
      className={classes.drawer}
      classes={{
        paper: classes.drawerPaper,
      }}
    >
      <Divider />
      <List>
        {Object.keys(apis).map(key => (
          <ListItem button key={key} component={Link} to={"/" + key } >{apis[key].title}</ListItem>
        ))}
      </List>
    </Drawer>
  }
  

  return (
    <Router>
      <div className={classes.app}>
        <CssBaseline />

        <aside>
          <Sidebar />
        </aside>

        <main className={classes.content}>
          <Switch>
            {Object.keys(apis).map(key => (
              <Route key={key} path={"/" + key }>
                <SwaggerUI url={apis[key].apiSpec} />
              </Route>
            ))}
            <Route path="/">
              <div>Select something</div>
            </Route>
          </Switch>
        </main>
        
      </div>
    </Router>
  );
}

App.propTypes = {
  groups: PropTypes.array.isRequired
}

export default App;
