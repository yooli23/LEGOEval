import React from 'react';
import axios from 'axios';
import Survey from './Survey'


class MessageList extends React.Component {
    render() {
      return (      
          <div className="message-list" style={{width: 500}}>                 
              {this.props.messages.map(message => {
                  return (
                    <div class="bubbleWrapper">
                      <div class={"You" == message.senderId ? "inlineContainer own" : "inlineContainer"}>
                        <div className={"You" != message.senderId ?"otherBubble other" : "ownBubble own"}>{message.text}</div>
                      </div>
                      <span className={"You" != message.senderId ?"other" : "own"}>{message.senderId}</span>
                    </div>
                  )
                })
              }
        </div>
      )
    }
  }


class ConversationSurvey extends React.Component {

    constructor(props) {
      super(props);
      this.state = {messages: [], text: ""};      
    }

    componentDidMount() {

        // URL
        const url = window.location.href.split('?')[0];

        // Get the state from backend
        axios.get(url+ "/init").then(res => {

            // Set the state
            this.setState(res.data, function() {

              // Send instruction
              // Ask backend for the conversation
                axios.post(url+ "/update", Object.assign({}, this.state, {instruction: 'load_single_conversation'})).then(result => {            
                  this.setState(result.data);     
              });
            });
        })
    }

    render() {      
      return (
        <div>

          <p style={{fontSize: 30, fontWeight: 'bold'}}>{this.state.paragraph}</p>
           
          <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '50vh', flexDirection: 'column'}}>
            <MessageList messages={this.state.messages} />
          </div>
            <Survey advance={this.props.advance} />
        </div>
      );
    }  
}


export default ConversationSurvey;