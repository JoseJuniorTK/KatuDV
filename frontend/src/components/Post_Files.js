import React, {Component } from 'react';
import axios from 'axios';

var fileLocation;

class App extends Component {
  state = {
    files: []

  }
    componentDidMount() {
      axios.get('http://127.0.0.1:8000/uploads/').then(response => response.data)
          .then((data) => {
              this.setState({files: data})
              console.log(this.state.files)
          })
      alert(JSON.stringify({fileLocation}));
               
  }
  render() {
    return (
       <div className="container">
        <div className="col-xs-8">
        <h6>Uploaded Files</h6>


  {this.state.files.map((file, i) => {
        console.log(i);
        fileLocation = file.file_license
      })}
    
<label>
      {fileLocation}
</label>
        </div>
       </div>
    );
  }
}
export default App;