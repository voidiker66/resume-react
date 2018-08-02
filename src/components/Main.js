import { Route, NavLink,  HashRouter } from "react-router-dom";
import { Switch } from 'react-router'
import React from 'react';
import Home from "./Home";
import Projects from "./Projects";
import Project from "./Project";
import Experiences from "./Experiences";
import Experience from "./Experience";
import PageNotFound from "./PageNotFound";

export default class Main extends React.Component {
    render() {
      return (
        <HashRouter>
          
      <div>
      <div className="navbar navbar-inverse">
        <ul className="nav navbar-nav">
              <li><NavLink exact to="/">Home</NavLink></li>
              <li><NavLink exact to="/work">Work Experience</NavLink></li>
              <li><NavLink exact to="/projects">Projects</NavLink></li>
              <li><NavLink exact to="/hackathon">Hackathon</NavLink></li>
              {/* <li><NavLink exact to="/search" style={{color:'white'}} activeClassName='wow' activeStyle={{backgroundColor:'#5f6268'}}>Search</NavLink></li> */}
            </ul>
            </div>
            <div className="content">
              <Switch>
                <Route exact path="/" component={Home}/>
                <Route path="/experience" component={Experience}/>
                <Route exact path="/projects" component={Projects}/>
                <Route path="/projects/:project_id" component={Project}/>
                <Route exact path="/work" component={Experiences}/>
                <Route path="/work/:work_id" component={Experience}/>
                <Route component={PageNotFound} />
              </Switch>
            </div>
          </div>
        </HashRouter>
      );
    }
  }