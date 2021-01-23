import React from 'react';
import axios from 'axios';


import Page from './Page';
import RandomExample from './RandomExample';
// Import your new components here!


class Start extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
    }

    componentDidMount() {      
      this.getLatestState();
    }    
        
    getLatestState = () => {      
      const url = window.location.href;
      axios.get(url+ "/init").then((res) => {        
        this.setState(res.data);        
      }).catch((error)=>{
        console.log(error);
     });
    }

    render() {      
      return (
        <div>
          {(() => {
            
            if (this.state.pipeline == undefined) return <p>Loading...</p>;

            const name = this.state.pipeline[0].name; 
            
            switch (name) {

              case 'Page':
                return <Page advance={this.getLatestState}/>;

              case 'RandomExample':
                return <RandomExample advance={this.getLatestState}/>;

              // Add more components here :)

              default:
                return <p>Unknown component!</p>;
            }
          })()}
        </div>
      );
    }   
}


export default Start;