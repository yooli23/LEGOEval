import React from 'react';
import CompareChats from "./CompareChats";
import Survey from './Survey'


class CompareChatsSurvey extends React.Component {

    constructor(props) {
      super(props);      
    }

    render() {      
      return (
        <div>
            <CompareChats advance={this.props.advance} showButtons={false} />
            <Survey advance={this.props.advance} />
        </div>
      );
    }  
}


export default CompareChatsSurvey;