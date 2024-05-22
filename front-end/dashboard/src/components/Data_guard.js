import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import './Data_guard.css';

import HomePage from './components/HomePage';
import AboutPage from './components/AboutPage';
import ResourcesPage from './components/ResourcesPage';
import NotFoundPage from './components/NotFoundPage';

const App = () => {
  return (
    <Router>
      <div>
        <header>
          <h1>Dataguard</h1>
          <nav>
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
            <Link to="/resources">Resources</Link>
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

export default App;


import React from 'react';

const HomePage = () => {
  return (
    <section>
      <h2>Welcome to Dataguard</h2>
      <p>Your one-stop platform to understand and exercise your data privacy rights.</p>
    </section>
  );
};

export default HomePage;


import React from 'react';

const AboutPage = () => {
  return (
    <section>
      <h2>About Dataguard</h2>
      <p>Dataguard is an educational platform and toolkit designed to empower individuals to understand and exercise their data privacy rights.</p>
    </section>
  );
};

export default AboutPage;


import React from 'react';

const ResourcesPage = () => {
  return (
    <section>
      <h2>Data Privacy Resources</h2>
      <ul>
        <li><a href="https://www.privacypolicies.com/blog/">Privacy Policies Blog</a></li>
        <li><a href="https://www.eff.org/issues/privacy">Electronic Frontier Foundation: Privacy</a></li>
        <li><a href="https://gdpr.eu/">GDPR.eu</a></li>
      </ul>
    </section>
  );
};

export default ResourcesPage;


import React from 'react';

const NotFoundPage = () => {
  return (
    <section>
      <h2>Page Not Found</h2>
      <p>Sorry, the page you are looking for does not exist.</p>
    </section>
  );
};

export default NotFoundPage;
