import React from "react";
import { NavLink } from "react-router-dom";

const Home = () => {
  return (
    <div className="container-text-center">
    <div className="test">
      this is test text 
      </div> 
    <form>
      <input type="file" name="name" />
      <NavLink
      to="/createAccount"
      >
      <input type="submit" value="Submit" />
      </NavLink>
      <br></br>
      Files uploaded are saved to our databases, we do not sell or
      <br></br>
      give your personal data or files to any third party organization
      <br></br>
      <input
        name="isGoing"
        type="checkbox"
        //checked={this.state.isGoing}
        />
      I understand
    </form>
    
    </div>
  );
  
};

function GoToCreate(props){

}

export default Home;