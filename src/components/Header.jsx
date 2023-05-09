import React, { useContext } from "react";
import { Link } from "react-router-dom";
// import DarkTheme from "./dark/DarkTheme";
// import AuthContext from "../utils/AuthContext";

function Header() {

  // const {user,logoutUser}= useContext(AuthContext)

  // console.log(user)

    return (
      <header className=" dark:bg-slate-400 bg-red-400 px-2 border-b flex items-center justify-between h-14" >
      {/* <a className="uppercase font-bold text-purple-900"  href="/">{user ? user.username : 'Noname'}</a> */}
      <a className="uppercase font-bold text-purple-900"><Link to='/' className='header-link'>Label</Link></a>

      <nav className="hidden md:flex items-center">
          <ul className="text-gray-500 font-semibold inline-flex items-center">
              <br />
              <li><Link to='/employees' className='header-link'>Employees</Link></li>
              <br />
              <li><Link to='/api' className='header-link'>API</Link></li>


              {/* {user ? (
                <li><Link to='/' onClick={logoutUser} className='header-link'>logout</Link></li>
              ):(
                <li><Link to='/login' className='header-link'>login</Link></li>
              )} */}

              {/* <DarkTheme/> */}
              {/* <li><Link to='/calculator' className='header-link'>Calculator</Link></li> */}

          </ul> 
      </nav>
  </header>
    )
  }

export default Header;