import React, { useState } from "react";
import { NavLink } from "react-router-dom";

const Navbar = () => {
  const [isOpen, setOpen] = useState(false);
  return (
    <nav
      className="navbar is-primary"
      role="navigation"
      aria-label="main navigation"
    >
    <div className="header-text">
        <NavLink 
            to="/"
            id = "app-header"
        >
            File Analyzer-
        </NavLink>
        <a>protect yourself from malicious files online </a>
        <NavLink
            id = "login-button"
            to="/login"
        >
            Login
        </NavLink>
    </div>
    </nav>
  );
};

export default Navbar;