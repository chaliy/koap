import React from 'react';

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

function App(props) {
  const classes = useStyles();
  const { groups } = props || {};

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
        {groups.map(group => (
          <ListItem button key={group.key} component={Link} to={"/" + group.key } >{group.title}</ListItem>
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
            {groups.map(group => (
              <Route key={group.key} path={"/" + group.key }>
                <SwaggerUI url={group.apiSpec} />
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

export default App;
