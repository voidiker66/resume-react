import React from 'react';
import Background from './Background';

export default class PageNotFound extends React.Component{   

render() {
    return (
        <div>
        <Background/>
          <h1 style={{textAlign:'center'}} >Page Not Found</h1>
        </div>
    );
}
}