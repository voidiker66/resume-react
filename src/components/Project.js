import React from 'react';
import Background from './Background';

const API_URL = "http://localhost:5000/api/project/";

export default class Project extends React.Component {

  constructor() {
    super();
   
    this.state = {
        project: [],
        work: [],
    };
  }

componentDidMount() {
  fetch(API_URL + this.props.match.params.project_id)
  .then(results => {
    return results.json();
  }).then(data=> {
    this.setState({
      project: data
  })
    });
  fetch("http://localhost:5000/api/company")
  .then(r => {
    return r.json();
  }).then(d => {
    this.setState({
      work: d.objects
    })
  });
}

  render() {
    return (
      <div>
      <Background/>
        <h1>{this.state.project.project_name}</h1>
        <p>{this.state.project.project_languages}</p>
        <p dangerouslySetInnerHTML={{ __html: this.state.project.project_description}}></p>
      </div>
    );
  }
}