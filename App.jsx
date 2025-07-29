import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import MRIViewer from './components/MRIViewer';

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/viewer" component={MRIViewer} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;