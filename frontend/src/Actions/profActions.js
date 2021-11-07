import {
  PROFESSOR_DETAILS_REQUEST,
  PROFESSOR_DETAILS_SUCCESS,
  PROFESSOR_DETAILS_FAIL,
  SET_PROFESSOR_SPECIALISATION,
} from "../Constants/profConstants";
import axios from "axios";

export const getProfessorDetails = () => async (dispatch) => {
  try {
    dispatch({ type: PROFESSOR_DETAILS_REQUEST });
    const { data } = await axios.get("/api/professors");

    dispatch({
      type: PROFESSOR_DETAILS_SUCCESS,
      payload: data,
    });

    localStorage.setItem("professorInfo", JSON.stringify(data));
  } catch (error) {
    dispatch({
      type: PROFESSOR_DETAILS_FAIL,
      //Checking for error.response and error.response.data.message to check the errors coming from backen
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};

export const setProfessorSepcialisation =
  (specialisation) => async (dispatch) => {
    dispatch({
      type: SET_PROFESSOR_SPECIALISATION,
      payload: specialisation,
    });
  };
