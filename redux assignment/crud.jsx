// Create Login registration with CRUD Application using API (Redux)


// src/redux/store.js
import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';
import authReducer from './reducers/authReducer';
import crudReducer from './reducers/crudReducer';

const rootReducer = combineReducers({
  auth: authReducer,
  crud: crudReducer
});

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;



// src/redux/reducers/authReducer.js
const initialState = {
    user: null,
    token: null,
    isAuthenticated: false,
    loading: false,
    error: null
  };
  
  const authReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'LOGIN_SUCCESS':
        return { ...state, user: action.payload.user, token: action.payload.token, isAuthenticated: true, loading: false };
      case 'LOGIN_FAIL':
      case 'REGISTER_FAIL':
        return { ...state, error: action.payload, loading: false };
      case 'REGISTER_SUCCESS':
        return { ...state, loading: false };
      case 'LOGOUT':
        return { ...state, user: null, token: null, isAuthenticated: false };
      case 'AUTH_LOADING':
        return { ...state, loading: true };
      default:
        return state;
    }
  };
  
  export default authReducer;

  
  // src/redux/reducers/crudReducer.js
const initialState = {
    items: [],
    loading: false,
    error: null
  };
  
  const crudReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'FETCH_SUCCESS':
        return { ...state, items: action.payload, loading: false };
      case 'CREATE_SUCCESS':
        return { ...state, items: [...state.items, action.payload], loading: false };
      case 'UPDATE_SUCCESS':
        return { ...state, items: state.items.map(item => item.id === action.payload.id ? action.payload : item), loading: false };
      case 'DELETE_SUCCESS':
        return { ...state, items: state.items.filter(item => item.id !== action.payload), loading: false };
      case 'CRUD_LOADING':
        return { ...state, loading: true };
      case 'CRUD_ERROR':
        return { ...state, error: action.payload, loading: false };
      default:
        return state;
    }
  };
  
  export default crudReducer;

  

  // src/redux/actions/authActions.js
import axios from 'axios';

export const login = (email, password) => async (dispatch) => {
  dispatch({ type: 'AUTH_LOADING' });
  try {
    const res = await axios.post('/api/login', { email, password });
    dispatch({ type: 'LOGIN_SUCCESS', payload: res.data });
  } catch (error) {
    dispatch({ type: 'LOGIN_FAIL', payload: error.message });
  }
};

export const register = (name, email, password) => async (dispatch) => {
  dispatch({ type: 'AUTH_LOADING' });
  try {
    const res = await axios.post('/api/register', { name, email, password });
    dispatch({ type: 'REGISTER_SUCCESS', payload: res.data });
  } catch (error) {
    dispatch({ type: 'REGISTER_FAIL', payload: error.message });
  }
};

export const logout = () => (dispatch) => {
  dispatch({ type: 'LOGOUT' });
};




// src/redux/actions/crudActions.js
import axios from 'axios';

export const fetchItems = () => async (dispatch) => {
  dispatch({ type: 'CRUD_LOADING' });
  try {
    const res = await axios.get('/api/items');
    dispatch({ type: 'FETCH_SUCCESS', payload: res.data });
  } catch (error) {
    dispatch({ type: 'CRUD_ERROR', payload: error.message });
  }
};

export const createItem = (item) => async (dispatch) => {
  dispatch({ type: 'CRUD_LOADING' });
  try {
    const res = await axios.post('/api/items', item);
    dispatch({ type: 'CREATE_SUCCESS', payload: res.data });
  } catch (error) {
    dispatch({ type: 'CRUD_ERROR', payload: error.message });
  }
};

export const updateItem = (id, updatedItem) => async (dispatch) => {
  dispatch({ type: 'CRUD_LOADING' });
  try {
    const res = await axios.put(`/api/items/${id}`, updatedItem);
    dispatch({ type: 'UPDATE_SUCCESS', payload: res.data });
  } catch (error) {
    dispatch({ type: 'CRUD_ERROR', payload: error.message });
  }
};

export const deleteItem = (id) => async (dispatch) => {
  dispatch({ type: 'CRUD_LOADING' });
  try {
    await axios.delete(`/api/items/${id}`);
    dispatch({ type: 'DELETE_SUCCESS', payload: id });
  } catch (error) {
    dispatch({ type: 'CRUD_ERROR', payload: error.message });
  }
};


// src/components/Login.js
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { login } from "../redux/actions/authActions";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const dispatch = useDispatch();
  const { loading, error } = useSelector((state) => state.auth);

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(login(email, password));
  };

  return (
    <div>
      <h2>Login</h2>
      {error && <p>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit" disabled={loading}>Login</button>
      </form>
    </div>
  );
};

export default Login;


// src/components/Dashboard.js
import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchItems, createItem, updateItem, deleteItem } from "../redux/actions/crudActions";

const Dashboard = () => {
  const dispatch = useDispatch();
  const { items, loading, error } = useSelector((state) => state.crud);

  useEffect(() => {
    dispatch(fetchItems());
  }, [dispatch]);

  const handleCreate = () => {
    const newItem = { name: "New Item", description: "New Description" };
    dispatch(createItem(newItem));
  };

  const handleUpdate = (id) => {
    const updatedItem = { name: ""}


        // src/components/Register.js
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { register } from "../redux/actions/authActions";

const Register = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const dispatch = useDispatch();
  const { loading, error } = useSelector((state) => state.auth);

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(register(name, email, password));
  };

  return (
    <div>
      <h2>Register</h2>
      {error && <p>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit" disabled={loading}>Register</button>
      </form>
    </div>
  );
};

export default Register;
