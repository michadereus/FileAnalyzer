import React from "react";

const About = () => (
  <div>
    <div>
      Create your account
      <button>
       I already have an account 
      </button>
      <button >
        Analyze my files without an account
      </button>
    </div>
    <form>
      <input type="text" name="name" />
      <input type="submit" value="Submit" />
    </form>
    
  </div>
);


export default About;