import React from 'react';
import ReactDOM from 'react-dom';
import ReactDelayRender from 'react-delay-render';


class Frame extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            waiting: true,
          };
    }
    getData(){
        setTimeout(() => {
          console.log('Our data is fetched');
          
        }, 500)
      }

    componentDidMount() {
        this.timer = setTimeout(() => {
            this.setState({
              waiting: false
            });
          }, 3000);
       
    }

    render(){
        if (!this.state.waiting)
        
       {
        return (
            <div className={ this.props.result ? "framenofire" : "framefire"}  >
                
            </div>
            
        );
       }
       return null;
    }
}




export default Frame;