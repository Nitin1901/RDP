import Header from "./Components/Header";
import HomeScreen from "./Screens/HomeScreen";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Container } from "@mui/material";

function App() {
  return (
    <div className="App">
      <Router>
        <Header />
        <main>
          <Container>
            <Route exact path="/" component={HomeScreen} />
          </Container>
        </main>
      </Router>
    </div>
  );
}

export default App;
