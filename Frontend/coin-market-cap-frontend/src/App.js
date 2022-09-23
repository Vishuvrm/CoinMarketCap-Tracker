import logo from './logo.svg';
import './App.css';
import ShowData from './components/ShowData';

function App() {
  const url = "http://127.0.0.1:8000/scrap/fetch-data"
  return (
    <div className="App">
      <ShowData url={url}/>
    </div>
  );
}

export default App;
