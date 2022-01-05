import Header from './Components/Header';
import HomeScreen from './Screens/HomeScreen';
import ProfileScreen from './Screens/ProfileScreen/ProfileScreen';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Container } from '@mui/material';

function App() {
  return (
    <div className="App">
      <Router>
        <Header />
        <main>
          <Container>
            <Route exact path="/" component={HomeScreen} />
            <Route path="/page/:pageNumber" component={HomeScreen} />
            <Route exact path="/search/:keyword" component={HomeScreen} />
            <Route path="/search/:keyword/page/:pageNumber" component={HomeScreen} />
            <Route exact path="/profile/:id" component={ProfileScreen} />
          </Container>
        </main>
      </Router>
    </div>
  );
}

export default App;
