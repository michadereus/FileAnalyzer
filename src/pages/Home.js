import React from "react";
import Button from 'react-bootstrap/Button';

const Home = () => (
  <div class="container-text-center">
   <form>
    <input type="file" name="name" />
    <input type="submit" value="Submit" />
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

function GoToCreate(props){
  
}

export default Home;