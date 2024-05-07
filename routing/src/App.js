import logo from './logo.svg';
import './App.css';
import { BrowserRouter,Router, Route, Routes } from 'react-router-dom';
import Womens from './Womens';
import Mens from './Mens';
import Common from './Common';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
          <Route path='/category' element={<Common/>}>
            <Route path='/category/men' element={<Mens/>}></Route>
            <Route path='/category/women' element={<Womens/>}></Route>
            <Route path='/category/women/:id' element={<Womens/>}></Route>

          </Route>

      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
