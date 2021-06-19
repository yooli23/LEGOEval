import React from 'react';
import axios from 'axios';
import Button from '@material-ui/core/Button';


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
        if (this.state.pipeline == undefined) return <p>Loading...</p>;      
        const data = this.state.pipeline[0].data;
        return (
          <div>            
              <h1>{data.title}</h1>            
              <p style={{fontSize:40, "white-space":"pre-line", "text-align":"left"}}>{data.description}</p>
              <Button onClick={this.requestMTurkInfo} variant="contained" color="primary">Start Task</Button>
          </div>
        );        
    }    

    requestMTurkInfo = () => {
        const url = window.location.href.split('?')[0];     
        const assignmentID = window.location.href.split('?')[1].split('&')[0].split("=")[1];
        if (assignmentID.includes("ASSIGNMENT_ID_NOT_AVAILABLE")) return;                
        var end_point_val = window.location.href.split('?')[1].split("&")[3].split("=")[1] + "/mturk/externalSubmit";        
        end_point_val = decodeURIComponent(end_point_val);
        console.log(end_point_val);
        axios.post(url+ "/update",
            Object.assign({}, this.state, {instruction: 'advance', mturk: {assignment_id: assignmentID, end_point: end_point_val}})).then(res => {            
                this.setState(res.data);  
                this.props.advance();          
        })
    }
}


export default LoadMTurk;