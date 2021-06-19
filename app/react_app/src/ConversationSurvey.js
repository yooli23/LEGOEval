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
      this._callBackFun = this._callBackFun.bind(this);  
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
              //   axios.post(url+ "/update", Object.assign({}, this.state, {instruction: 'load_single_conversation'})).then(result => {            
              //     this.setState(result.data);     
              // });
            });
        })
    }
    
    _callBackFun(res_data) {
      const data = res_data.data.pipeline[0].data
      if (data.hasOwnProperty("messages")) {
        this.setState(res_data.data, function() {
        });
      }
    }

    render() {
      if (this.state.pipeline == undefined) return <p>Loading...</p>;      
      const data = this.state.pipeline[0].data;      
      return (
        <div>

          <p style={{fontSize: 20, fontWeight: 'bold', textAlign: 'left'}}>{data.paragraph}</p>
           
          <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', flexDirection: 'column'}}>
            <MessageList messages={data.messages} />
          </div>
            <Survey advance={this.props.advance} _callBackFun={this._callBackFun}/>
        </div>
      );
    }  
}


export default ConversationSurvey;