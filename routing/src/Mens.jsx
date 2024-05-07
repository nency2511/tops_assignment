import React from 'react'
import { useNavigate } from 'react-router-dom'

const Mens = () => {

const navigate = useNavigate()
const GoToWomen = ()=>{
    navigate('/category/women')
}

  return (
    <><h1>Mens</h1>
        <button onClick={()=>{
            GoToWomen()   //function name
         }}>Go to women</button>
    </>

  )
}

export default Mens