import { createContext, useState, useEffect } from 'react'
import jwt_decode from "jwt-decode";
import axios from 'axios';

const AuthContext = createContext()

export default AuthContext;

export const AuthProvider = ({children}) => {
    const [user, setUser] = useState(()=> localStorage.getItem('authToken') ? jwt_decode(localStorage.getItem('authToken')) : null)
    const [authToken, setAuthToken] = useState(()=> localStorage.getItem('authToken') ? JSON.parse(localStorage.getItem('authToken')) : null)
    const [loading,setLoading] = useState(true)


    //
    // Login
    //
    const login = async (payload) => {
        let response = await axios.post("http://localhost:8000/api/auth/token/", payload);
        console.log(response.data.access)

        if (response.status === 200){
            setAuthToken(response.data)
            setUser(jwt_decode(response.data.access))
            localStorage.setItem('authToken',JSON.stringify(response.data))
        } else {
            alert('wrong')
        }

      };

    //
    // LogOut
    //
    const logoutUser = () => {
        setAuthToken(null)
        setUser(null)
        localStorage.removeItem('authToken')
    }


    //
    // UpdateToken
    //
    const updateToken = async () => {
        console.log('udateTOken')
        let response = await axios.post("http://localhost:8000/api/auth/token/refresh/", 
        {'refresh':authToken?.refresh});
        
        console.log(response)
        if (response.status === 200){
            setAuthToken(response.data)
            setUser(jwt_decode(response.data.access))
            localStorage.setItem('authToken',JSON.stringify(response.data))
        }else{
            logoutUser()
        }
        if(loading){
            setLoading(false)
        }
    }


    let constextData = {
        user:user,
        authToken:authToken,
        login:login,
        logoutUser:logoutUser,
    }


    useEffect(() => {
        if(loading){
            updateToken()
        }

        let fiveMinutes = 1000 * 60 *5
        setInterval(() =>{
            if(authToken){
                updateToken()
            }
        },fiveMinutes)

        return () => clearInterval()

    }, [authToken,loading])
    
    return(
        <AuthContext.Provider value={constextData} >
            {loading ? null : children}
        </AuthContext.Provider>
    )
}