import React from "react";
import { NavLink } from "react-router-dom";

const CreateAccount = () => (
  <div>
    <div>
      Create your account
      <button>
       I already have an account 
      </button>
      <NavLink
      to="/results"
      >
      <button >
        Analyze my files without an account
      </button>
      </NavLink>
      
    </div>
    <form>
      <input type="text" name="name" />
      <input type="submit" value="Submit" />
    </form>
    
  </div>
);


export default CreateAccount;