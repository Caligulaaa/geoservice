import './App.css';
import Header from './components/Header';
import Group from './pages/Group';
import Employee from './pages/Employee';

import { Route,Routes,BrowserRouter } from "react-router-dom";
import LoginPage from './pages/LoginPage';

import ProtectedRoute from './utils/ProtectedRoute';
import { AuthProvider } from './utils/AuthContext';

function App() {
  return (
    // <AuthProvider>
      <BrowserRouter>
        <div className="App">
          <Header />

          <Routes>
            <Route path='/' element={<Group/>}/>
            <Route path='/employees' element={<Employee/>}/>

              {/* <Route path='/' element={<ProtectedRoute/>}> */}
                {/* <Route path='/' element={<Group/>}/> */}
                {/* <Route path='/' element={<Group/>}/> */}

                {/* <Route path='/employees' element={<Employee/>}/> */}
              {/* </Route> */}
              
              {/* <Route path='/register' element={<Register/>}/> */}
              {/* <Route path='/login' element={<LoginPage/>}/> */}

          </Routes>
          
        </div>
      </BrowserRouter>
    // </AuthProvider>
  );
}

export default App;
