import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import {createBrowserRouter,RouterProvider} from "react-router-dom";

import deluxe1 from "./assets/deluxe1.jpg";
import deluxe2 from "./assets/deluxe2.jpg";
import family_suite1 from "./assets/family_suite1.jpg";
import family_suite2 from "./assets/family_suite2.webp";
import family_suite3 from "./assets/family_suite3.jpg";
import standard1 from "./assets/standard1.jpg";
import standard2 from "./assets/standard2.webp";


import { UserProvider } from './Components/UserContext.jsx';
import GuestRoute from './Components/GuestRoute.jsx';
import AuthForm from './Components/AuthFome.jsx';
import BookingComponent from './Components/BookingComponent.jsx';
import AllRooms from './Components/AllRooms.jsx';
import OccupiedDatesDisplay from './Components/OccupiedDatesDisplay.jsx';
const router=createBrowserRouter([
  {
    path:"/",
    element:<App/>,
    children:[
      {path:"/",
        element:<BookingComponent></BookingComponent>
      },
      {
        path:"/all-rooms",
        element:<AllRooms></AllRooms>
      },
      {
        path:"/auth",
        element:(
          <GuestRoute>
            <AuthForm/>
          </GuestRoute>
        )

      },
      {
        path:"/my-bookings",
        element:<OccupiedDatesDisplay></OccupiedDatesDisplay>
      }
    ]
  },
])
createRoot(document.getElementById('root')).render(
  <StrictMode>
      <UserProvider>
         <RouterProvider router={router}/>
      </UserProvider>
   </StrictMode>
)
