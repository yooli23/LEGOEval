import React from 'react';
import axios from 'axios';


class LoadMTurk extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
    }

    componentDidMount() {      
        // const url = window.location.href;    
        const url = window.location.href.split('?')[0];        
        axios.get(url+ "/init").then(res => {
            this.setState(res.data);
            this.requestMTurkInfo();
        })      
    }

    render() {
      return <p>Loading MTurk information...</p>;
    }    

    requestMTurkInfo = () => {
        // const url = window.location.href;     

        // Tmp test
        console.log("test!");
        console.log(window.location.href.split('?')[1]);

        const url = window.location.href.split('?')[0];       
        axios.post(url+ "/update", 
        Object.assign({}, this.state, {instruction: 'load_mturk'})).then(res => {            
            this.setState(res.data);             
            if (res.data.mturk != null) { // we assume they filled out mturk correctly
                this.popComponent()
            }else{
                // do nothing if error loading mturk data
                console.log(res.data);
            }
        })
    }

    popComponent = () => {        
        // const url = window.location.href;        
        const url = window.location.href.split('?')[0];        
        axios.post(url+ "/update", 
        Object.assign({}, this.state, {instruction: 'advance'})).then(res => {            
            this.setState(res.data);             
            this.props.advance();             
        })
    }
}


export default LoadMTurk;