import React from 'react';
import Background from './Background';
export default class Home extends React.Component {
  render() {
    return (
    	<div>
      <Background/>
        <div className="clouds"></div>
	    	<span className="container emphasis">
  				<h1>Austin Ikerd</h1>
  				<p className="text-center">A Resume Website</p>
			  </span>
		</div>
    );
  }
}