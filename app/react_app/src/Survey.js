import React from 'react';
import axios from 'axios';

class Survey extends React.Component {    

    componentDidMount() {        
        // call init function
        const url = window.location.href;    
        var data;  
        axios.get(url+ "/init").then(res => {
          data = res.data;    // arguments will come from the data         
        })
    }  

    render() {  
        // Add HTML like stuff here for the survey            
      return <p>Loading...</p>;
    }    
}


export default Start;