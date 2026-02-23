import { useState,useContext,useEffect} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Navbar from './Components/NavBar'
import { UserContext } from "./Components/UserContext";
import { Outlet } from 'react-router-dom'

function App() {
  const { user, setUser } = useContext(UserContext);
  const [loading,setLoading]=useState(true)
  useEffect(()=>{
      const storedUser=localStorage.getItem("user")
      if(storedUser){
        setUser(JSON.parse(storedUser))
      }
      else{
        setUser(null)
      }
      setLoading(false)
  },[])
  if(loading){
    return <div>Loading....</div>
  }
  return (
    <>
      <Navbar/>
      <Outlet/>
    </>
  )
}

export default App
