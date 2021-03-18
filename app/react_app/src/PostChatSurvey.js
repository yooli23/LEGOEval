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


class PostChatSurvey extends React.Component {

    constructor(props) {
      super(props);
      this.state = {messages: [], text: ""};      
    }

    componentDidMount() {
        const url = window.location.href.split('?')[0];
        axios.get(url+ "/init").then(res => {
            this.setState(res.data, function() {
              // pass
            });
        })
    }

    render() {      
      return (
        <div>
          <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh', flexDirection: 'column'}}>
            <MessageList messages={this.state.messages} />
          </div>
            <Survey advance={this.props.advance} />
        </div>
      );
    }  
}


export default PostChatSurvey;