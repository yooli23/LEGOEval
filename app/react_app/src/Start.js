import React from 'react';
import axios from 'axios';


import Page from './Page';
import RandomExample from './RandomExample';
import LoadMTurk from './LoadMTurk';
import SubmitMTurk from './SubmitMTurk';
import Survey from './Survey'
import MyChatbot from "./chatbot/Chatbot";
import CompareChats from "./CompareChats";
import CompareChatsSurvey from "./CompareChatsSurvey";
import PostChatSurvey from "./PostChatSurvey";
import ConversationSurvey from "./ConversationSurvey";
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
      // const url = window.location.href;
      const url = window.location.href.split('?')[0];
      axios.get(url+ "/init").then((res) => {        
        if (res != null) {
          this.setState(res.data);
        }         
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

              case 'LoadMTurk':
                return <LoadMTurk advance={this.getLatestState}/>;

              case 'SubmitMTurk':
                return <SubmitMTurk advance={this.getLatestState}/>;

              case 'Survey':
                return <Survey advance={this.getLatestState}/>;

              case 'MyChatbot':
                return <MyChatbot advance={this.getLatestState}/>;

              case 'CompareChats':
                return <CompareChats showButtons={true} advance={this.getLatestState}/>;

              case 'CompareChatsSurvey':
                return <CompareChatsSurvey advance={this.getLatestState} />;

              case 'PostChatSurvey':
                return <PostChatSurvey advance={this.getLatestState} />;

              case 'ConversationSurvey':
                return <ConversationSurvey advance={this.getLatestState} />;

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