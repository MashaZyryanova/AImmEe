import React from 'react';
import ReactDOM from 'react-dom';
import AIboard from './AIboard';

class  Scene extends React.Component{

    constructor(props){
        super(props);
        
    }
    
    
    //after component renders call api and fetch the info 
    componentDidMount() {
        
        
    }
    

    render(){
        return(
           
            <div className="observationBoard">
                <AIboard/> 
                <AIboard/> 
                 
            </div>
        );
    };    
}

export default Scene;
