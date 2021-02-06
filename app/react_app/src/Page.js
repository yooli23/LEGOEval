import React from 'react';
import axios from 'axios';
import Button from '@material-ui/core/Button';


class Page extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
    }

    componentDidMount() {      
        const url = window.location.href;            
        axios.get(url+ "/init").then(res => {
            this.setState(res.data);
        })      
    }

    render() {
      if (this.state.pipeline == undefined) return <p>Loading...</p>;      
      const data = this.state.pipeline[0].data;
      return (
        <div>            
            <h1>{data.title}</h1>            
            <p>{data.description}</p>
            <Button onClick={this.popComponent} variant="contained" color="primary">{data.button_name}</Button>            
        </div>
      );
    }    

    popComponent = () => {        
        const url = window.location.href;            
        axios.post(url+ "/update", 
        Object.assign({}, this.state, {instruction: 'advance'})).then(res => {            
            this.setState(res.data);             
            this.props.advance();             
        })
    }
}


export default Page;