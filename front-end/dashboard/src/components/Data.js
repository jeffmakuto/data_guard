import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './Data.css';

import HomePage from './components/HomePage';
import AboutPage from './components/AboutPage';
import ResourcesPage from './components/ResourcesPage';
import NotFoundPage from './components/NotFoundPage';

const Data = () => {
  return (
    <Router>
      <div>
        <header>
          <h1>Dataguard</h1>
          <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/resources">Resources</a>
          </nav>
        </header>
        <main>
          <Switch>
            <Route exact path="/" component={HomePage} />
            <Route path="/about" component={AboutPage} />
            <Route path="/resources" component={ResourcesPage} />
            <Route component={NotFoundPage} />
          </Switch>
        </main>
        <footer>
          <p>&copy; 2024 Dataguard. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  );
};

export default Data;
