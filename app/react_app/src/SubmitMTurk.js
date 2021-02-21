import React from 'react';
import axios from 'axios';


class SubmitMTurk extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
    }

    componentDidMount() {      
        this.setState({complete: false});
        // const url = window.location.href;            
        const url = window.location.href.split('?')[0];
        axios.get(url+ "/init").then(res => {
            this.setState(res.data, function() {
                this.submitTask();
            });            
        })      
    }

    render() {
        if (this.state.pipeline == undefined) return <p>Loading...</p>;        
        return (
            <form name="mturk_form" method="post" id="mturk_form" action={this.state.mturk.production_end_point}>
              <input type="hidden" value='' name="assignmentId" id={this.state.mturk.assignment_id}/>
              <input type="submit"/>
            </form>
        );
        // if (this.state.complete == true) {
        //      return <p>Submitting your task, please be patient...</p>;        
        // }else{
        //     return <p>Task Complete!</p>;
        // }        
    }    

    submitTask = () => {
        if (this.state.pipeline == undefined) {console.log("Error submitting task!"); return;}

        var bodyFormData = new FormData();
        bodyFormData.append('assignmentId', this.state.mturk.assignment_id);
        bodyFormData.append('foo', 'boo');

        axios({
            method: 'post',
            url: this.state.mturk.sandbox_end_point,
            data: bodyFormData,
            headers: {'Content-Type': 'multipart/form-data' }
            })
            .then(function (response) {
                //handle success
                console.log(response);
                this.setState({complete: true});
                this.notifyBackendToCompleteTask();
            })
            .catch(function (response) {
                //handle error
                console.log(response);
        });

        axios({
            method: 'post',
            url: this.state.mturk.production_end_point,
            data: bodyFormData,
            headers: {'Content-Type': 'multipart/form-data' }
            })
            .then(function (response) {
                //handle success
                console.log(response);
                this.setState({complete: true});
                this.notifyBackendToCompleteTask();
            })
            .catch(function (response) {
                //handle error
                console.log(response);
        });        
    }

    notifyBackendToCompleteTask = () => {
        console.log("trying to notify backend");
        // const url = window.location.href;           
        const url = window.location.href.split('?')[0]; 
        axios.post(url+ "/update", 
        Object.assign({}, this.state, {instruction: 'mark_complete'})).then(res => {            
            this.setState(res.data);            
        })
    }
}


export default SubmitMTurk;