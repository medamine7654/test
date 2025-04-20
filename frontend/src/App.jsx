import { useState } from 'react'
import "./App.css"
import Dashboard1 from '../components/dashboard1'
import Dashboard2 from '../components/dashboard2'
import { Routes, Route } from "react-router-dom"
import Navbar from '../components/navbar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Navbar
        content={
          <Routes>
            <Route path="/" element={<Dashboard1/>}/>
            <Route path="/dashboard2" element={<Dashboard2/>}/>
          </Routes>
        }
      />
      
    </>
  )
}

export default App