import './App.css';
import {useState, useEffect} from 'react'; 
import { Component } from './Components/Component/Component'

function App() {
  
  const [initialState, setState] = useState([])
  const url = "/home"

  useEffect(()=> {
    fetch(url).then((response => {
      return response.json()
    }).then(data => setState(data))
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        NSA Malicious File Analyzer
      </header> 
      <div className="center">
        <h1>View preview and confirm</h1>
        <Component data={initialState}/>
        <input class="centerFileUpload" type="file"></input>
        <button type="button" id="preview-button">View Preview</button>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
      </div>
    </div>
  );
}

export default App;

// docker run --rm -p 3000:3000 reactapp