import React from 'react';
import axios from 'axios';

import * as Surveys from "survey-react";
import "survey-react/survey.css";

class Survey extends React.Component {

    constructor(props) {
      super(props);
      this.state = {};
    }

    componentDidMount() {
        const url = window.location.href.split('?')[0];
        axios.get(url+ "/init").then(res => {
            this.setState(res.data);
        })
    }

    render() {
        if (this.state.pipeline == undefined) return <p>Loading...</p>;

        const data = this.state.pipeline[0].data;
        let json = {};
        if (data.hasOwnProperty("questions")) {
            json = {title: data.title, showProgressBar: "top", questions: []}
            for (var i = 0; i < data.questions.length; i++) {
                json.questions.push(this.parseQuestion(JSON.parse(data.questions[i])));
            }
        }
        let model = new Surveys.Model(json);

        return (
          <Surveys.Survey model={model} onComplete={this.popComponent}/>
        );
    }

    parseQuestion(question) {
        let parsed;
        switch (question["type"]){
            case "radiogroup":
                parsed = { type: question["type"], name: question["name"], title: question["title"],
                        isRequired: question["isRequired"], colCount: question["colCount"],
                        choices: question["choices"]};
                break;
            case "checkbox":
                parsed = { type: question["type"], name: question["name"], title: question["title"],
                        isRequired: question["isRequired"], colCount: question["colCount"],
                        hasNone: question["hasNone"], choices: question["choices"]};
                break;
            case "text":
                parsed = { type: question["type"], name: question["name"], title: question["title"],
                        isRequired: question["isRequired"], placeHolder: question["placeHolder"],
                        autoComplete: question["autoComplete"]};
                break;
            case "rating":
                parsed = { type: question["type"], name: question["name"], title: question["title"],
                        minRateDescription: question["minRateDescription"],
                        maxRateDescription: question["maxRateDescription"]};
                break;
            case "comment":
                parsed = { type: question["type"], name: question["name"], title: question["title"]};
                break;
            case "matrix":
                parsed = { type: question["type"], name: question["name"], title: question["title"],
                        columns: question["columns"], rows: question["rows"]};
                break;
            default:
                parsed = {};
        }
        return parsed;
    }

    popComponent = (survey, options) => {

        const data = this.state.pipeline[0].data;

        var surveyTitleStr = data.title;
        var surveyData = JSON.stringify(survey.data);

        var updateVal = {};
        updateVal['instruction'] = 'advance';
        updateVal[surveyTitleStr] = surveyData

        const url = window.location.href.split('?')[0];
        axios.post(url+ "/update", Object.assign({}, this.state, updateVal)).then(res => {
            this.setState(res.data);
            this.props.advance();
        })
    }

}

export default Survey;