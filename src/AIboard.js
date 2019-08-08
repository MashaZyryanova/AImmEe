import React from 'react';
import ReactDOM from 'react-dom';
import Frame from './Frame';


class  AIboard extends React.Component{

    constructor(props){
        super(props);
        this.state ={
            results: [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],   
        };
    }
    
    //to do
    DataApi() {
           
        
    }
    //after component renders call api and fetch the info 
    componentDidMount() {
        
        
    }
    

    render(){
        return(
           
            <div className="aiboard">
                {this.state.results.map((result) => (
                    
                        <Frame result = {result}/>
                        
                    
                    
                   
                ))}    
            </div>
        );
    };    
}

export default AIboard;
