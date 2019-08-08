import React from 'react';
import Stats from './Stats'

class StatsContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state ={
        fire:0,
        nofire:1
    };
}
  render(){
    return (
      <div className="statsContainer">
          <Stats name="FIRE DETECTED" result = {this.state.fire}/>
          <Stats name="NO FIRE" result={this.state.nofire}/>
      </div>
  
  );
  }
}

export default StatsContainer;