import React, {Component} from 'react'
import Uploads from "./upload";
import Post_Files from "./Post_Files";
class  App extends Component{
    render() {
        return(
            <div className = "App">
                <header className= 'App-header'>
                    <h1 className='App-title'>Katu D.V Prototype 0.1</h1>
                </header>
                <Uploads/>
            <Post_Files/>
            </div>
        );
    }
}

export default App;