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
        const assignmentID = window.location.href.split('?')[1].split("=")[1];
        const url = window.location.href.split('?')[0];     

        var end_point_val = "";

        if (url.includes("sandbox")) {
            end_point_val = "https://workersandbox.mturk.com/mturk/externalSubmit";
        }else{
            end_point_val = "https://mturk.com/mturk/externalSubmit";
        }

        axios.post(url+ "/update",
            Object.assign({}, this.state, {instruction: 'advance', mturk: {assignment_id: assignmentID, end_point: end_point_val}})).then(res => {            
                this.setState(res.data);  
                this.props.advance();          
        })
    }
}


export default LoadMTurk;