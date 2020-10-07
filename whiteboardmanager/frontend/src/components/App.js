import React, { Component } from 'React';
import ReactDOM from 'react-dom';
import Sketch from './Sketch'

class App extends Component {
    render() {
        return( 
            <div>
                <canvas id='paper-canvas' height='500' width='500' />
                <Sketch />
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'))