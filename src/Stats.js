import React from 'react';
import Frame from './Frame'


function Stats(props) {
    
  
 
  
  return (
      <div className="stats">
          <h3>{props.name}</h3>;
          <Frame result={props.result}/>
          
      </div>
  
  );
}

export default Stats;