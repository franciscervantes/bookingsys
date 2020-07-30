import React from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Login from './Login.js'
import Homepage from './Homepage.js'


function App() {

  return (

    <>

   <div className="App">  

     <Router>    
      <div className="container">   

        <Switch>    

          <Route exact path='/' component={Login} ></Route> 
          <Route exact path='/Homepage' component={Homepage} ></Route>    
          

        </Switch>    

      </div>    

    </Router>    

    </div>  

   </>

  );

}

export default App;