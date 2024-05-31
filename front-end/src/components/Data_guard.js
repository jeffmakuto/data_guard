import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import './Data_guard.css';

const HomePage = () => {
  return (
    <section className="home">
      <h2 className="home__title">Welcome to Dataguard</h2>
      <p className="home__description">Your one-stop platform to understand and exercise your data privacy rights.</p>
    </section>
  );
};

const AboutPage = () => {
  return (
    <section className="about">
      <h2 className="about__title">About Dataguard</h2>
      <p className="about__description">Dataguard is an educational platform and toolkit designed to empower individuals to understand and exercise their data privacy rights.</p>
    </section>
  );
};

const ResourcesPage = () => {
  return (
    <section className="resources">
      <h2 className="resources__title">Data Privacy Resources</h2>
      <ul className="resources__list">
        <li className="resources__item"><a href="https://www.privacypolicies.com/blog/" className="resources__link">Privacy Policies Blog</a></li>
        <li className="resources__item"><a href="https://www.eff.org/issues/privacy" className="resources__link">Electronic Frontier Foundation: Privacy</a></li>
        <li className="resources__item"><a href="https://gdpr.eu/" className="resources__link">GDPR.eu</a></li>
      </ul>
    </section>
  );
};

const NotFoundPage = () => {
  return (
    <section className="not-found">
      <h2 className="not-found__title">Page Not Found</h2>
      <p className="not-found__description">Sorry, the page you are looking for does not exist.</p>
    </section>
  );
};

const Navigation = () => {
  return (
    <nav className="navigation">
      <ul className="navigation__list">
        <li className="navigation__item">
          <Link to="/" className="navigation__link">Home</Link>
        </li>
        <li className="navigation__item">
          <Link to="/about" className="navigation__link">About</Link>
        </li>
        <li className="navigation__item">
          <Link to="/resources" className="navigation__link">Resources</Link>
        </li>
      </ul>
    </nav>
  );
};

const App = () => {
  return (
    <Router>
      <div className="app">
        <header className="app__header">
          <h1 className="app__title">Dataguard</h1>
          <Navigation />
        </header>
        <main className="app__main">
          <Switch>
            <Route exact path="/" component={HomePage} />
            <Route path="/about" component={AboutPage} />
            <Route path="/resources" component={ResourcesPage} />
            <Route component={NotFoundPage} />
          </Switch>
        </main>
        <footer className="app__footer">
          <p>&copy; 2024 Dataguard. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  );
};

export default App;
