import React from 'react';
import axios from 'axios';
import Button from '@material-ui/core/Button';


class RandomExample extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
    }

    componentDidMount() {      
        const url = window.location.href;            
        axios.get(url+ "/init").then(res => {
            this.setState(res.data);
        })      
    }

    render() {

      if (this.state.pipeline == undefined) return <p>Loading...</p>;     

      const data = this.state.pipeline[0].data;

      return (                    
        <Button onClick={this.printInBackend} variant="contained" color="primary">{data.button_name}</Button>        
      );
    }    

    printInBackend = () => {        
        const url = window.location.href;            
        axios.post(url+ "/update", Object.assign({}, this.state, {instruction: 'print'})).then(res => {
            this.setState(res.data);                     
        })
    }
}


export default RandomExample; //here