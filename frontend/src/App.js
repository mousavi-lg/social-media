import Home from './components/home.js';
import React from 'react';
import Login from './components/login.js';
import {BrowserRouter as  Router, Route} from 'react-router-dom';
import Register from './components/register.js';
import Terms from './components/terms.js';

function App() {
  return (
    <Router>
      <Route exact path="/">
        <Home /> 
      </Route>
      <Route path="/register">
        <Register /> 
      </Route>
      <Route path="/login">
        <Login />
      </Route>
      <Route path="/terms">
        <Terms />
      </Route>
    </Router>
  );
}

export default App;
