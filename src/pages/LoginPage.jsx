import { useRef, useEffect,useState, useContext } from 'react';
import {useNavigate } from 'react-router-dom';

import AuthContext from '../utils/AuthContext';

const LoginPage = () => {
  const userRef = useRef()
  const passRef = useRef()

  const [errMsg, setErrMsg] = useState('')
  const navigate = useNavigate()

  const {login} = useContext(AuthContext);


  // useEffect(() => {
  //     setErrMsg('')
  // }, [user, pwd])



  const loginHendler = async (e) => {
    e.preventDefault();

    let playload = {
      username: userRef.current.value,
      password: passRef.current.value,
    }
    await login(playload);
    navigate('/')
    // try {

    //   await login(playload);

    // } catch (err) {
    //     if (!err?.response) {
    //         setErrMsg('No Server Response');
    //     } else if (err.response?.status === 400) {
    //         setErrMsg('Missing Username or Password');
    //     } else if (err.response?.status === 401) {
    //         setErrMsg('Unauthorized');
    //     } else {
    //         setErrMsg('Login Failed');
    //     }
    // }
  }
  
  return  (
      <div>
        <p>{errMsg }</p>
        <h1>Employee Login</h1>
        <form onSubmit={loginHendler}>
          <input 
          type="text" 
          id='username' 
          placeholder='Enter Username' 
          ref={userRef}
          autoComplete='off'
          required
          />
          <br />
          <input 
          type="password" 
          id='password' 
          placeholder='Enter Password'
          ref={passRef}
          required
          />
          <br />
          <button>login</button>

        </form>
      </div>
)}

export default LoginPage