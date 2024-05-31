import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './Header';
import HomePage from './HomePage';
import AboutPage from './AboutPage';
import ResourcesPage from './ResourcesPage';
import NotFoundPage from './NotFoundPage';
import Progressbar from './Progressbar';
import { DataProvider } from './DataContext';
import './App.css';

const App = () => {
  return (
    <DataProvider>
      <Router>
        <div className="App">
          <Header />
          <Progressbar progress={50} />
          <Switch>
            <Route exact path="/" component={HomePage} />
            <Route path="/about" component={AboutPage} />
            <Route path="/resources" component={ResourcesPage} />
            <Route component={NotFoundPage} />
          </Switch>
        </div>
      </Router>
    </DataProvider>
  );
};

export default App;
