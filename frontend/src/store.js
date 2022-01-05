import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";
import {
  professorDetailsReducer,
  setProfessorSepcialisationReducer,
  professorDetailReducer,
} from "./Reducers/profReducers";

//All the list of reducers which hold the state and pass it to components
const reducer = combineReducers({
  professorDetails: professorDetailsReducer,
  setProfessorSpecialisation: setProfessorSepcialisationReducer,
  professorDetail: professorDetailReducer,
});

//To get the user info from localstorage and add them to the initial state
const professorInfoFromLocalStorage = localStorage.getItem("professorInfo")
  ? JSON.parse(localStorage.getItem("professorInfo"))
  : null;

//An object to have the initial state if required
const initialState = {
  professorDetails: {
    loading: false,
    professorInfo: professorInfoFromLocalStorage,
  },
  setProfessorSpecialisation: {
    specialisation: "",
  },
  professorDetail: {
    loading: true,
    professorInfo: null,
  },
};

// An aarray of middlewares to be used in the store
const middleware = [thunk];

//The main store which takes the reducders, initialState, and all the middlewares
const store = createStore(
  reducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware)) //applyMiddleware takes all the middlewares so spreading the array here
);

export default store;
