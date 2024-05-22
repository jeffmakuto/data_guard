import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <h1>Dataguard</h1>
      <nav className="navbar">
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/resources">Resources</a>
      </nav>
    </header>
  );
};

export default Header;
